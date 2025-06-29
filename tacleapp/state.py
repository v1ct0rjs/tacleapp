import reflex as rx


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
        self.form_submitted = True

    def set_form_submitted(self, status: bool):
        """Sets the form submission status."""
        self.form_submitted = status