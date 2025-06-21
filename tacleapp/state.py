import reflex as rx
import httpx
import os
import base64  # Para la autenticación de Spotify

# Leer variables de entorno. Asegúrate de que estén configuradas.
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")


# Asegúrate de que SPOTIFY_PLAYLIST_ID se inicialice como un rx.Var si se va a modificar o usar en computed vars
# O simplemente léelo y úsalo directamente en la computed var.
# Para este caso, leerlo directamente en la computed var es más simple.

class State(rx.State):
    """The app state."""

    # Navigation state
    is_mobile_menu_open: bool = False

    # Contact form state
    contact_name: str = ""
    contact_email: str = ""
    contact_subject: str = ""
    contact_message: str = ""
    form_submitted: bool = False

    # Spotify tracks state
    spotify_tracks: list[dict] = []
    is_loading_spotify_tracks: bool = False
    spotify_error: str = ""
    _spotify_token: str | None = None  # Para almacenar el token de acceso

    # Esta variable de estado almacenará el ID de la playlist.
    # Se inicializa desde la variable de entorno.
    # Si no se encuentra la variable de entorno, usa el placeholder.
    spotify_playlist_id: str = os.getenv("SPOTIFY_PLAYLIST_ID", "5uGYoNGFfm9jB1Mm9PHHaj")

    @rx.var
    def spotify_playlist_full_url(self) -> str:
        """Devuelve la URL completa de la playlist de Spotify o la URL base de Spotify."""
        if self.spotify_playlist_id and self.spotify_playlist_id != "5uGYoNGFfm9jB1Mm9PHHaj":
            return f"https://open.spotify.com/playlist/{self.spotify_playlist_id}"
        return "https://open.spotify.com"

    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    def close_mobile_menu(self):
        self.is_mobile_menu_open = False

    def submit_contact_form(self):
        if self.contact_name and self.contact_email and self.contact_message:
            print(
                f"Contact form: {self.contact_name}, {self.contact_email}, {self.contact_subject}, {self.contact_message}")
            self.form_submitted = True
            self.contact_name = ""
            self.contact_email = ""
            self.contact_subject = ""
            self.contact_message = ""
        else:
            print("Form submission failed: Missing fields")

    def reset_form_status(self):
        self.form_submitted = False

    async def _get_spotify_token(self):
        """Obtiene un token de acceso de Spotify usando Client Credentials."""
        if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
            self.spotify_error = "Spotify Client ID o Secret no configurados."
            print("Error: Spotify Client ID o Secret no configurados.")
            return False

        auth_url = "https://accounts.spotify.com/api/token"
        auth_header = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
        auth_data = {"grant_type": "client_credentials"}

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    auth_url,
                    headers={"Authorization": f"Basic {auth_header}"},
                    data=auth_data
                )
                response.raise_for_status()
                token_data = response.json()
                self._spotify_token = token_data.get("access_token")
                if not self._spotify_token:
                    self.spotify_error = "No se pudo obtener el token de Spotify."
                    return False
                return True
        except Exception as e:
            self.spotify_error = f"Error obteniendo token de Spotify: {str(e)}"
            print(f"Spotify token error: {e}")
            return False

    async def fetch_spotify_tracks(self):
        """Obtiene hasta 4 pistas de la playlist configurada en Spotify."""
        if not self.spotify_playlist_id or self.spotify_playlist_id == "5uGYoNGFfm9jB1Mm9PHHaj":
            self.spotify_error = "Spotify Playlist ID no configurado."
            print("Error: Spotify Playlist ID no configurado.")
            return

        self.is_loading_spotify_tracks = True
        self.spotify_error = ""
        self.spotify_tracks = []

        if not self._spotify_token:
            if not await self._get_spotify_token():
                self.is_loading_spotify_tracks = False
                return

        api_url = f"https://api.spotify.com/v1/playlists/{self.spotify_playlist_id}/tracks?limit=4&fields=items(track(name,artists(name),album(images),duration_ms,external_urls(spotify)))"

        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    api_url,
                    headers={"Authorization": f"Bearer {self._spotify_token}"}
                )
                if response.status_code == 401:
                    print("Spotify token expirado o inválido, obteniendo uno nuevo...")
                    if not await self._get_spotify_token():
                        self.is_loading_spotify_tracks = False
                        return
                    response = await client.get(
                        api_url,
                        headers={"Authorization": f"Bearer {self._spotify_token}"}
                    )

                response.raise_for_status()
                playlist_data = response.json()

                processed_tracks = []
                for item in playlist_data.get("items", []):
                    track_data = item.get("track")
                    if not track_data:
                        continue

                    duration_ms = track_data.get("duration_ms", 0)
                    minutes = (duration_ms // (1000 * 60)) % 60
                    seconds = (duration_ms // 1000) % 60
                    formatted_duration = f"{minutes:02d}:{seconds:02d}"

                    images = track_data.get("album", {}).get("images", [])
                    image_url = images[1].get("url") if len(images) > 1 else (
                        images[0].get("url") if images else "/placeholder.svg?height=300&width=300")

                    processed_tracks.append({
                        "title": track_data.get("name", "Sin título"),
                        "artists": ", ".join([artist.get("name", "") for artist in track_data.get("artists", [])]),
                        "duration": formatted_duration,
                        "image": image_url,
                        "url": track_data.get("external_urls", {}).get("spotify", "#")
                    })
                self.spotify_tracks = processed_tracks
                if not self.spotify_tracks:
                    self.spotify_error = "No se encontraron canciones en la playlist o la respuesta está vacía."

        except httpx.HTTPStatusError as e:
            self.spotify_error = f"Error HTTP {e.response.status_code} al contactar Spotify. Revisa tu Playlist ID y credenciales."
            print(f"Spotify HTTPStatusError: {e}")
        except Exception as e:
            self.spotify_error = f"Error procesando datos de Spotify: {str(e)}"
            print(f"Spotify Generic Exception: {e}")
        finally:
            self.is_loading_spotify_tracks = False
