import reflex as rx
import httpx
import os
import base64
from dotenv import load_dotenv

load_dotenv()

# --- Variables de Entorno ---
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_PLAYLIST_ID_FROM_ENV = os.getenv("SPOTIFY_PLAYLIST_ID", "YOUR_PLAYLIST_ID_HERE")


# --- Excepción Personalizada ---
class SpotifyError(Exception):
    """Excepción personalizada para errores de la API de Spotify."""
    pass


class State(rx.State):
    """The app state."""
    is_mobile_menu_open: bool = False
    contact_name: str = ""
    contact_email: str = ""
    contact_subject: str = ""
    contact_message: str = ""
    form_submitted: bool = False

    spotify_tracks: list[dict] = []
    is_loading_spotify_tracks: bool = False
    spotify_error: str = ""

    spotify_playlist_id: str = SPOTIFY_PLAYLIST_ID_FROM_ENV

    @rx.var
    def spotify_playlist_full_url(self) -> str:
        if self.spotify_playlist_id and self.spotify_playlist_id != "YOUR_PLAYLIST_ID_HERE":
            return f"https://open.spotify.com/playlist/{self.spotify_playlist_id}"
        return "https://open.spotify.com"

    # ... (otras funciones como toggle_mobile_menu, etc. sin cambios) ...
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    def close_mobile_menu(self):
        self.is_mobile_menu_open = False

    def submit_contact_form(self):
        pass  # Implementar lógica si es necesario

    def reset_form_status(self):
        pass  # Implementar lógica si es necesario

    async def _get_spotify_token(self) -> str:
        """Obtiene un token de acceso de Spotify. Lanza SpotifyError si falla."""
        print("Intentando obtener token de Spotify...")
        if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
            raise SpotifyError("Spotify Client ID o Secret no configurados en el entorno.")

        auth_url = "https://accounts.spotify.com/api/token"
        auth_header = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
        auth_data = {"grant_type": "client_credentials"}

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                print("Enviando petición de token a Spotify...")
                response = await client.post(auth_url, headers={"Authorization": f"Basic {auth_header}"},
                                             data=auth_data)
                print(f"Respuesta de token recibida. Status: {response.status_code}")
                response.raise_for_status()
                token_data = response.json()
                token = token_data.get("access_token")
                if not token:
                    raise SpotifyError("La respuesta de Spotify no contenía un token de acceso.")
                print("Token de Spotify obtenido con éxito.")
                return token
        except httpx.HTTPStatusError as e:
            error_body = e.response.json().get("error_description", "Error de autenticación desconocido.")
            raise SpotifyError(
                f"Error de autenticación ({e.response.status_code}): {error_body}. Revisa tus credenciales.") from e
        except (httpx.RequestError) as e:  # Captura errores de conexión, timeouts, etc.
            raise SpotifyError(f"No se pudo conectar con Spotify para obtener el token: {str(e)}") from e

    async def fetch_spotify_tracks(self):
        """Obtiene las pistas de Spotify, manejando el flujo de error de forma centralizada."""
        print("\n--- Iniciando fetch_spotify_tracks ---")
        self.is_loading_spotify_tracks = True
        self.spotify_error = ""
        self.spotify_tracks = []

        try:
            if not self.spotify_playlist_id or self.spotify_playlist_id == "YOUR_PLAYLIST_ID_HERE":
                raise SpotifyError("Spotify Playlist ID no está configurado en las variables de entorno.")

            token = await self._get_spotify_token()

            api_url = f"https://api.spotify.com/v1/playlists/{self.spotify_playlist_id}/tracks?limit=4&fields=items(track(name,artists(name),album(images),duration_ms,external_urls(spotify)))"
            print(f"Enviando petición de tracks a: {api_url}")

            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(api_url, headers={"Authorization": f"Bearer {token}"})
                print(f"Respuesta de tracks recibida. Status: {response.status_code}")
                response.raise_for_status()
                playlist_data = response.json()

            processed_tracks = []
            for item in playlist_data.get("items", []):
                track_data = item.get("track")
                if not track_data: continue  # Saltar si el objeto track es nulo (puede pasar si hay items no musicales)

                # Asegurarse de que los campos esenciales existen antes de procesar
                if not all(k in track_data for k in ["name", "artists", "album", "duration_ms", "external_urls"]):
                    print(
                        f"AVISO: Track incompleto o con formato inesperado, saltando: {track_data.get('name', 'Nombre desconocido')}")
                    continue

                duration_ms = track_data.get("duration_ms", 0)
                minutes, seconds = divmod(duration_ms // 1000, 60)
                formatted_duration = f"{minutes:02d}:{seconds:02d}"

                album_images = track_data.get("album", {}).get("images", [])
                image_url = album_images[0].get(
                    "url") if album_images else "/placeholder.svg?height=300&width=300"  # Usar la primera imagen disponible
                if len(album_images) > 1:  # Preferir la segunda imagen si existe (suele ser de 300px)
                    image_url = album_images[1].get("url", image_url)

                processed_tracks.append({
                    "title": track_data.get("name", "Sin título"),
                    "artists": ", ".join(
                        [artist.get("name", "Artista desconocido") for artist in track_data.get("artists", [])]),
                    "duration": formatted_duration,
                    "image": image_url,
                    "url": track_data.get("external_urls", {}).get("spotify", "#")
                })

            self.spotify_tracks = processed_tracks
            if not self.spotify_tracks:
                print(
                    "AVISO: La petición a Spotify fue exitosa pero no se encontraron tracks procesables en la playlist.")
                self.spotify_error = "No se encontraron canciones en la playlist especificada o no son accesibles."

        except (SpotifyError, httpx.HTTPStatusError, httpx.RequestError) as e:
            error_message = str(e)
            if isinstance(e, httpx.HTTPStatusError):
                try:
                    error_body = e.response.json().get("error", {})
                    api_message = error_body.get("message", "Error desconocido de la API.")
                    error_message = f"Error de API ({e.response.status_code}): {api_message}"
                except Exception:  # Si el cuerpo del error no es JSON
                    error_message = f"Error de API ({e.response.status_code}): {e.response.text}"

            print(f"ERROR en fetch_spotify_tracks: {error_message}")
            self.spotify_error = error_message
        except Exception as e:  # Captura genérica para errores inesperados en el procesamiento
            print(f"ERROR INESPERADO en fetch_spotify_tracks: {str(e)}")
            self.spotify_error = "Ocurrió un error inesperado al procesar las canciones."
        finally:
            print("--- Finalizando fetch_spotify_tracks ---")
            self.is_loading_spotify_tracks = False
