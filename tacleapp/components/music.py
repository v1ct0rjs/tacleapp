import reflex as rx
from .utils import section_header
from ..state import State  # Importar el State

def spotify_track_card(track: dict) -> rx.Component:
    """Componente para una tarjeta de música de Spotify."""
    return rx.box(
        rx.link(
            rx.box(
                rx.image(
                    src=track.get("image", "/placeholder.svg?height=300&width=300"),
                    alt=track.get("title", "Track image"),
                    class_name="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300"
                ),
                rx.box(
                    rx.button(
                        rx.icon("play", size=24, fill="white"),
                        size="3",
                        radius="full",
                        class_name="bg-red-500 hover:bg-red-600 text-white border-0 shadow-lg"
                    ),
                    class_name="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center"
                ),
                class_name="relative overflow-hidden rounded-t-lg"
            ),
            href=track.get("url", "#"),
            is_external=True,
        ),
        # Track Info
        rx.box(
            rx.heading(track.get("title", "Track Desconocido"), size="4", weight="bold",
                       class_name="font-orbitron text-white mb-1 truncate"),
            rx.text(track.get("artists", "Artista Desconocido"), size="2", class_name="text-gray-400 mb-2 truncate"),
            rx.flex(
                rx.icon("clock", size=16, class_name="text-gray-400 mr-2"),
                rx.text(track.get("duration", "00:00"), size="2", class_name="text-gray-400"),
                align="center"
            ),
            class_name="p-4"
        ),
        class_name="group bg-gray-900/50 rounded-lg overflow-hidden border border-gray-800 hover:border-red-500/50 transition-all duration-300"
    )

def music() -> rx.Component:
    """Music section con Tracks de Spotify y Sessions de SoundCloud."""

    # Actualiza esta lista con tus iframes de SoundCloud
    # El iframe original del usuario (2072434876) no funciona porque el track_id es inválido o no público.
    # Se reemplaza con un ejemplo funcional. El usuario deberá usar sus propios iframes válidos.
    soundcloud_embed_codes = [
        """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/656341994&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>""",
        # Ejemplo del iframe original del usuario (comentado porque no funciona):
        # """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2072434876&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>""",
    ]

    return rx.box(
        rx.container(
            section_header("My ", "Music"),
            # --- Tracks (Spotify) ---
            rx.box(
                rx.heading("Latest Tracks", size="7", weight="bold",
                           class_name="font-orbitron text-white mb-3 text-center sm:text-left"),
                rx.text(
                    "Mis últimos lanzamientos y producciones disponibles en Spotify.",
                    class_name="text-gray-400 max-w-2xl text-center sm:text-left mb-10"
                ),
                rx.cond(
                    State.is_loading_spotify_tracks,
                    rx.center(rx.spinner(size="3", color="red"), class_name="h-64"),
                    rx.cond(
                        State.spotify_error,
                        rx.center(
                            rx.vstack(
                                rx.icon("triangle-alert", size=48, class_name="text-yellow-500"),
                                rx.text("Error al cargar tracks de Spotify:", class_name="text-lg font-semibold"),
                                rx.text(State.spotify_error, class_name="text-gray-400 text-center"),
                                rx.button("Intentar de nuevo", on_click=State.fetch_spotify_tracks,
                                          class_name="mt-4 bg-red-500 hover:bg-red-600"),
                                align="center", spacing="3"
                            ),
                            class_name="h-64 p-8 bg-gray-900/50 rounded-lg border border-gray-800"
                        ),
                        rx.cond(
                            State.spotify_tracks,
                            rx.grid(
                                rx.foreach(State.spotify_tracks, spotify_track_card),
                                columns={"initial": "1", "sm": "2", "lg": "4"},
                                spacing="6"
                            ),
                            rx.center(
                                rx.text("No hay tracks de Spotify para mostrar en este momento.",
                                        class_name="text-gray-500"),
                                class_name="h-64"
                            )
                        )
                    )
                ),
                rx.flex(
                    rx.link(
                        rx.button(
                            "Más en Spotify",
                            rx.icon("arrow-right", size=16, class_name="ml-2"),
                            size="3", variant="outline",
                            class_name="border-gray-500 text-gray-300 hover:bg-white hover:text-black font-bold mt-12 tracking-wider"
                        ),
                        href=State.spotify_playlist_full_url,
                        is_external=True,
                    ),
                    justify="center",
                    class_name="w-full"
                ),
                id="spotify-tracks",
                class_name="mb-20 pt-10"
            ),
            # --- Sessions (SoundCloud) ---
            rx.box(
                rx.heading("DJ Sessions", size="7", weight="bold",
                           class_name="font-orbitron text-white mb-3 text-center sm:text-left"),
                rx.text(
                    "Escucha mis últimas sesiones y mixes en SoundCloud.",
                    class_name="text-gray-400 max-w-2xl text-center sm:text-left mb-10"
                ),
                rx.cond(
                    len(soundcloud_embed_codes) > 0,
                    rx.vstack(
                        *[
                            rx.box(
                                rx.html(embed_code),
                                class_name="w-full max-w-3xl mx-auto my-4 rounded-lg border border-gray-800",
                                min_height="166px"
                            )
                            for embed_code in soundcloud_embed_codes
                        ],
                        spacing="6",
                        align="center",
                        class_name="w-full"
                    ),
                    rx.center(
                        rx.text("No hay sesiones de SoundCloud para mostrar en este momento.",
                                class_name="text-gray-500"),
                        class_name="h-32"
                    )
                ),
                rx.flex(
                    rx.link(
                        rx.button(
                            "Más en SoundCloud",
                            rx.icon("arrow-right", size=16, class_name="ml-2"),
                            size="3", variant="outline",
                            class_name="border-gray-500 text-gray-300 hover:bg-white hover:text-black font-bold mt-12 tracking-wider"
                        ),
                        href="https://soundcloud.com/tu-nombre-de-usuario", # Reemplaza con tu URL de perfil de SoundCloud
                        is_external=True,
                    ),
                    justify="center",
                    class_name="w-full"
                ),
                id="soundcloud-sessions",
                class_name="pt-10"
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),
        id="music",
        class_name="py-20 bg-black",
        on_mount=State.fetch_spotify_tracks
    )
