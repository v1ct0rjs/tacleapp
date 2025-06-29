import reflex as rx
from .utils import section_header
from ..state import State


def music() -> rx.Component:
    """Music section con Tracks de Spotify y Sessions de SoundCloud."""

    spotify_playlist = [
        """<iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/5uGYoNGFfm9jB1Mm9PHHaj?utm_source=generator" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>"""
    ]

    soundcloud_embed_codes = [
        """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1512589402&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
        """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2090535147&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
        """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2007493087&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
        """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1972991863&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
        """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/1916937122&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
        """<iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/2072434876&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
    ]
    podcast_embed_codes = [
        """<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1521291607&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
        """<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1470611422&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
        """<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1470612097&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe>""",
    ]

    return rx.box(
        rx.container(
            section_header("My ", "Music"),
            # --- Tracks (Spotify) ---
            rx.box(
                rx.heading("Latest Tracks", size="7", weight="bold",
                           class_name="font-orbitron text-white mb-3 text-center sm:text-left"),
                rx.text(
                    "Last songs on Spotify.",
                    class_name="text-gray-400 max-w-2xl text-center sm:text-left mb-10"
                ),
                rx.cond(
                    len(spotify_playlist) > 0,
                    rx.vstack(
                        *[
                            rx.box(
                                rx.html(embed_code),
                                class_name="w-full max-w-3xl mx-auto my-4 rounded-lg border border-gray-800",
                                min_height="166px"
                            )
                            for embed_code in spotify_playlist
                        ],
                        spacing="6",
                        align="center",
                        class_name="w-full"
                    ),
                    rx.center(
                        rx.text("No hay tracks para mostrar en este momento.",
                                class_name="text-gray-500"),
                        class_name="h-32"
                    )
                ),

                rx.flex(
                    rx.link(
                        rx.button(
                            "Spotify",
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
                rx.heading("Sessions", size="7", weight="bold",
                           class_name="font-orbitron text-white mb-3 text-center sm:text-left"),
                rx.text(
                    "Last tracks and sets in SoundCloud.",
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
                id="soundcloud-sessions",
                class_name="pt-10"
            ),
            # --- Podcast (SoundCloud) ---
            rx.box(
                rx.heading("Podcast", size="7", weight="bold",
                           class_name="font-orbitron text-white mb-3 text-center sm:text-left"),
                rx.text(
                    "Podcast episodes on SoundCloud.",
                    class_name="text-gray-400 max-w-2xl text-center sm:text-left mb-10"
                ),
                rx.cond(
                    len(podcast_embed_codes) > 0,
                    rx.vstack(
                        *[
                            rx.box(
                                rx.html(embed_code),
                                class_name="w-full max-w-3xl mx-auto my-4 rounded-lg border border-gray-800",
                                min_height="166px"
                            )
                            for embed_code in podcast_embed_codes
                        ],
                        spacing="6",
                        align="center",
                        class_name="w-full"
                    ),
                    rx.center(
                        rx.text("No hay podcasts de SoundCloud para mostrar en este momento.",
                                class_name="text-gray-500"),
                        class_name="h-32"
                    )
                ),
                rx.flex(
                    rx.link(
                        rx.button(
                            "SoundCloud",
                            rx.icon("arrow-right", size=16, class_name="ml-2"),
                            size="3", variant="outline",
                            class_name="border-gray-500 text-gray-300 hover:bg-white hover:text-black font-bold mt-12 tracking-wider",
                        ),
                        href="https://soundcloud.com/10tacle",
                        is_external=True,
                    ),
                    justify="center",
                    class_name="w-full",
                ),
                id="soundcloud-podcasts",
                class_name="pt-10",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),
        id="music",
        class_name="py-20 bg-black",
    )