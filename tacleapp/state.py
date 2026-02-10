import reflex as rx
import os
import smtplib
from email.message import EmailMessage


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
        self.contact_name = form_data.get("name", "")
        self.contact_email = form_data.get("email", "")
        self.contact_subject = form_data.get("subject", "")
        self.contact_message = form_data.get("message", "")
        self.form_submitted = False
        self.form_error = ""

        if not self.contact_name or not self.contact_email or not self.contact_message:
            self.form_error = "Please complete all required fields before sending."
            return

        try:
            self._send_contact_email()
            self.form_submitted = True
        except Exception:
            self.form_error = "We couldn't send your message right now. Please try again later."

    def set_form_submitted(self, status: bool):
        """Sets the form submission status."""
        self.form_submitted = status

    def _send_contact_email(self) -> None:
        smtp_host = os.environ.get("CONTACT_SMTP_HOST", "")
        smtp_port = int(os.environ.get("CONTACT_SMTP_PORT", "587"))
        smtp_user = os.environ.get("CONTACT_SMTP_USER", "")
        smtp_password = os.environ.get("CONTACT_SMTP_PASSWORD", "")
        smtp_use_tls = os.environ.get("CONTACT_SMTP_USE_TLS", "true").lower() in {"1", "true", "yes"}
        to_email = os.environ.get("CONTACT_TO_EMAIL", "")
        from_email = os.environ.get("CONTACT_FROM_EMAIL", smtp_user or to_email)

        if not smtp_host or not to_email or not from_email:
            raise ValueError("Missing SMTP configuration.")

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