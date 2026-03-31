import reflex as rx
import os
import smtplib
import logging
from pathlib import Path
from email.message import EmailMessage
from dotenv import load_dotenv


logger = logging.getLogger(__name__)

# Carga explicita de .env para asegurar variables en backend de Reflex.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def _clean_env(value: str) -> str:
    """Normalize env values copied with quotes/spaces from shell snippets."""
    return (value or "").strip().strip("\"'")


class State(rx.State):
    """The app state."""

    # --- General UI State ---
    is_mobile_menu_open: bool = False

    # --- Contact Form State ---
    contact_name: str = ""
    contact_email: str = ""
    contact_subject: str = ""
    contact_message: str = ""
    form_submitted: bool = False
    form_error: str = ""

    # --- Static Music Links ---
    # Hardcoded Spotify playlist ID.
    spotify_playlist_id: str = "5uGYoNGFfm9jB1Mm9PHHaj"

    @rx.var
    def spotify_playlist_full_url(self) -> str:
        """The full URL to the Spotify playlist."""
        return f"https://open.spotify.com/playlist/{self.spotify_playlist_id}"

    # --- UI Methods ---
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    def close_mobile_menu(self):
        self.is_mobile_menu_open = False

    # --- Form Methods ---
    def handle_contact_submit(self, form_data: dict):
        """Handles the contact form submission."""
        print(f"[CONTACT] submit keys={sorted(form_data.keys())}", flush=True)
        logger.warning("Contact submit received. keys=%s", sorted(form_data.keys()))
        self.contact_name = form_data.get("name", "")
        self.contact_email = form_data.get("email", "")
        self.contact_subject = form_data.get("subject", "")
        self.contact_message = form_data.get("message", "")
        self.form_submitted = False
        self.form_error = ""

        if not self.contact_name or not self.contact_email or not self.contact_message:
            self.form_error = "Please complete all required fields before sending."
            print("[CONTACT] missing required fields", flush=True)
            logger.warning("Contact submit rejected: missing required fields")
            return

        try:
            self._send_contact_email()
            self.form_submitted = True
            print("[CONTACT] email sent successfully", flush=True)
            logger.warning("Contact email sent successfully")
        except Exception as exc:
            print(f"[CONTACT] send failed: {type(exc).__name__}: {exc}", flush=True)
            logger.exception("Contact form email send failed")
            debug_errors = os.environ.get("CONTACT_DEBUG_ERRORS", "false").lower() in {"1", "true", "yes"}
            if debug_errors:
                self.form_error = f"SMTP error: {type(exc).__name__}: {exc}"
            else:
                self.form_error = "We couldn't send your message right now. Please try again later."

    def set_form_submitted(self, status: bool):
        """Sets the form submission status."""
        self.form_submitted = status

    def _send_contact_email(self) -> None:
        smtp_host = _clean_env(os.environ.get("CONTACT_SMTP_HOST", ""))
        smtp_port = int(_clean_env(os.environ.get("CONTACT_SMTP_PORT", "587")) or "587")
        smtp_user = _clean_env(os.environ.get("CONTACT_SMTP_USER", ""))
        # Gmail muestra App Password en bloques con espacios; se normaliza para SMTP login.
        smtp_password = _clean_env(os.environ.get("CONTACT_SMTP_PASSWORD", "")).replace(" ", "")
        smtp_use_tls = _clean_env(os.environ.get("CONTACT_SMTP_USE_TLS", "true")).lower() in {"1", "true", "yes"}
        to_email = _clean_env(os.environ.get("CONTACT_TO_EMAIL", "")) or smtp_user
        from_email = _clean_env(os.environ.get("CONTACT_FROM_EMAIL", "")) or smtp_user or to_email

        if not smtp_host or not smtp_user or not smtp_password or not to_email or not from_email:
            raise ValueError("Missing SMTP configuration.")

        logger.warning(
            "SMTP config ready host=%s port=%s user=%s to=%s tls=%s",
            smtp_host,
            smtp_port,
            smtp_user,
            to_email,
            smtp_use_tls,
        )
        print(
            f"[CONTACT] SMTP host={smtp_host} port={smtp_port} user={smtp_user} to={to_email} tls={smtp_use_tls}",
            flush=True,
        )

        message = EmailMessage()
        message["Subject"] = f"[Contacto] {self.contact_subject or 'Sin asunto'}"
        message["From"] = from_email
        message["To"] = to_email
        message["Reply-To"] = self.contact_email
        message.set_content(
            "\n".join(
                [
                    f"Name: {self.contact_name}",
                    f"Email: {self.contact_email}",
                    f"Subject: {self.contact_subject or 'Sin asunto'}",
                    "",
                    self.contact_message,
                ]
            )
        )

        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.ehlo()
            if smtp_use_tls:
                server.starttls()
            if smtp_user and smtp_password:
                server.login(smtp_user, smtp_password)
            server.send_message(message)