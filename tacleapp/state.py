import reflex as rx


class State(rx.State):

    is_mobile_menu_open: bool = False
    spotify_playlist_id: str = "5uGYoNGFfm9jB1Mm9PHHaj"

    @rx.var
    def spotify_playlist_full_url(self) -> str:
        return f"https://open.spotify.com/playlist/{self.spotify_playlist_id}"

    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    def close_mobile_menu(self):
        self.is_mobile_menu_open = False
