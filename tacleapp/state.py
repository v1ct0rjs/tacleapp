import reflex as rx
import httpx
import os
import base64
from dotenv import load_dotenv
import asyncio

print(">>> [STATE.PY] Archivo state.py está siendo leído por Python <<<")

load_dotenv()
print(">>> [STATE.PY] python-dotenv load_dotenv() ejecutado <<<")

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_PLAYLIST_ID_FROM_ENV = os.getenv("SPOTIFY_PLAYLIST_ID", "YOUR_PLAYLIST_ID_HERE")

print(f">>> [STATE.PY] SPOTIFY_CLIENT_ID: {'Configurado' if SPOTIFY_CLIENT_ID else 'NO Configurado'}")
print(f">>> [STATE.PY] SPOTIFY_CLIENT_SECRET: {'Configurado' if SPOTIFY_CLIENT_SECRET else 'NO Configurado'}")
print(f">>> [STATE.PY] SPOTIFY_PLAYLIST_ID_FROM_ENV: {SPOTIFY_PLAYLIST_ID_FROM_ENV}")


class SpotifyError(Exception):
    pass


class State(rx.State):
    print(">>> [STATE.PY] Clase State está siendo definida <<<")

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

    debug_message: str = "Mensaje de depuración inicial"
    # ESTA LÍNEA DEBE ESTAR PRESENTE
    click_test_message: str = "Aún no se ha hecho clic en el botón de prueba."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(">>> [STATE.PY] Instancia de State creada (constructor __init__) <<<")

    # --- ESTE MÉTODO DEBE ESTAR PRESENTE ---
    def simple_click_test(self):
        print(">>> [STATE.PY] simple_click_test() INVOCADO <<<")
        self.click_test_message = "¡El botón de prueba simple FUNCIONÓ!"
        print(f">>> [STATE.PY] click_test_message ahora es: {self.click_test_message}")

    async def load_initial_spotify_tracks(self):
        print(">>> [STATE.PY] load_initial_spotify_tracks (VERSIÓN ASÍNCRONA) INVOCADO <<<")
        if self.is_loading_spotify_tracks:
            print(">>> [STATE.PY] Ya se está cargando, no se inicia nueva tarea.")
            return

        self.is_loading_spotify_tracks = True
        self.spotify_error = ""
        self.spotify_tracks = []
        self.debug_message = "Iniciando carga asíncrona de tracks..."
        print(">>> [STATE.PY] Llamando a fetch_spotify_tracks...")

        await self.fetch_spotify_tracks()
        self.debug_message = "Carga asíncrona de tracks (potencialmente) completada."

    @rx.var
    def spotify_playlist_full_url(self) -> str:
        if self.spotify_playlist_id and self.spotify_playlist_id != "YOUR_PLAYLIST_ID_HERE":
            return f"https://open.spotify.com/playlist/{self.spotify_playlist_id}"
        return "https://open.spotify.com"

    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open

    def close_mobile_menu(self):
        self.is_mobile_menu_open = False

    def handle_contact_submit(self, form_data: dict):
        print(f">>> [STATE.PY] Contact form submitted con datos: {form_data}")
        self.contact_name = form_data.get("name", "")
        self.contact_email = form_data.get("email", "")
        self.contact_subject = form_data.get("subject", "")
        self.contact_message = form_data.get("message", "")
        print(">>> [STATE.PY] Lógica de envío de email/DB (simulada).")
        self.form_submitted = True

    def set_form_submitted(self, status: bool):
        print(f">>> [STATE.PY] set_form_submitted llamado con: {status}")
        self.form_submitted = status

    async def _get_spotify_token(self) -> str:
        print(">>> [STATE.PY] _get_spotify_token() INVOCADO <<<")
        if not SPOTIFY_CLIENT_ID or not SPOTIFY_CLIENT_SECRET:
            print(">>> [STATE.PY] ERROR en _get_spotify_token: Client ID o Secret NO configurados.")
            raise SpotifyError("Spotify Client ID o Secret no configurados en el entorno.")

        auth_url = "https://accounts.spotify.com/api/token"
        auth_header = base64.b64encode(f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}".encode()).decode()
        auth_data = {"grant_type": "client_credentials"}

        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                print(">>> [STATE.PY] _get_spotify_token: Enviando petición de token a Spotify...")
                response = await client.post(auth_url, headers={"Authorization": f"Basic {auth_header}"},
                                             data=auth_data)
                print(f">>> [STATE.PY] _get_spotify_token: Respuesta de token recibida. Status: {response.status_code}")
                response.raise_for_status()
                token_data = response.json()
                token = token_data.get("access_token")
                if not token:
                    print(">>> [STATE.PY] ERROR en _get_spotify_token: La respuesta no contenía token.")
                    raise SpotifyError("La respuesta de Spotify no contenía un token de acceso.")
                print(">>> [STATE.PY] _get_spotify_token: Token obtenido con éxito.")
                return token
        except httpx.HTTPStatusError as e:
            error_body_text = "No disponible"
            try:
                error_body_text = e.response.json().get("error_description", "Error de autenticación desconocido.")
            except:
                error_body_text = e.response.text if e.response else "Respuesta de error no disponible"
            print(f">>> [STATE.PY] ERROR en _get_spotify_token (HTTPStatusError): {error_body_text}")
            raise SpotifyError(
                f"Error de autenticación ({e.response.status_code}): {error_body_text}. Revisa tus credenciales.") from e
        except (httpx.RequestError) as e:
            print(f">>> [STATE.PY] ERROR en _get_spotify_token (RequestError): {str(e)}")
            raise SpotifyError(f"No se pudo conectar con Spotify para obtener el token: {str(e)}") from e

    async def fetch_spotify_tracks(self):
        print("\n>>> [STATE.PY] --- Iniciando fetch_spotify_tracks --- <<<")

        try:
            if not self.spotify_playlist_id or self.spotify_playlist_id == "YOUR_PLAYLIST_ID_HERE":
                print(
                    f">>> [STATE.PY] ERROR en fetch_spotify_tracks: Playlist ID no configurado: {self.spotify_playlist_id}")
                raise SpotifyError("Spotify Playlist ID no está configurado en las variables de entorno.")

            token = await self._get_spotify_token()

            api_url = f"https://api.spotify.com/v1/playlists/{self.spotify_playlist_id}/tracks?limit=4"
            print(f">>> [STATE.PY] fetch_spotify_tracks: Enviando petición de tracks a: {api_url}")

            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(api_url, headers={"Authorization": f"Bearer {token}"})
                print(
                    f">>> [STATE.PY] fetch_spotify_tracks: Respuesta de tracks recibida. Status: {response.status_code}")
                response.raise_for_status()
                playlist_data = response.json()

            print(">>> [STATE.PY] --- RESPUESTA COMPLETA DE SPOTIFY (fetch_spotify_tracks) ---")
            import json
            print(json.dumps(playlist_data, indent=2))
            print("------------------------------------")

            processed_tracks = []
            for item in playlist_data.get("items", []):
                track_data = item.get("track")
                if not track_data: continue

                if not all(k in track_data for k in ["name", "artists", "album", "duration_ms", "external_urls"]):
                    print(
                        f"AVISO: Track incompleto o con formato inesperado, saltando: {track_data.get('name', 'Nombre desconocido')}")
                    continue

                duration_ms = track_data.get("duration_ms", 0)
                minutes, seconds = divmod(duration_ms // 1000, 60)
                formatted_duration = f"{minutes:02d}:{seconds:02d}"

                album_images = track_data.get("album", {}).get("images", [])
                image_url = album_images[0].get("url") if album_images else "/placeholder.svg?height=300&width=300"
                if len(album_images) > 1:
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
                print(">>> [STATE.PY] AVISO: Petición exitosa pero no se encontraron tracks procesables.")
                self.spotify_error = "No se encontraron canciones en la playlist especificada o no son accesibles."
            else:
                self.spotify_error = ""

        except (SpotifyError, httpx.HTTPStatusError, httpx.RequestError) as e:
            error_message = str(e)
            if isinstance(e, httpx.HTTPStatusError):
                try:
                    error_body = e.response.json().get("error", {})
                    api_message = error_body.get("message", "Error desconocido de la API.")
                    error_message = f"Error de API ({e.response.status_code}): {api_message}"
                except Exception:
                    error_body_text = e.response.text if e.response else "Respuesta de error no disponible"
                    error_message = f"Error de API ({e.response.status_code}): {error_body_text}"

            print(f">>> [STATE.PY] ERROR en fetch_spotify_tracks (Excepción capturada): {error_message}")
            self.spotify_error = error_message
        except Exception as e:
            print(f">>> [STATE.PY] ERROR INESPERADO en fetch_spotify_tracks: {str(e)}")
            self.spotify_error = "Ocurrió un error inesperado al procesar las canciones."
        finally:
            print(">>> [STATE.PY] --- Finalizando fetch_spotify_tracks ---")
            self.is_loading_spotify_tracks = False


print(">>> [STATE.PY] Archivo state.py leído completamente por Python <<<")
