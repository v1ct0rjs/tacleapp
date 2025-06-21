import reflex as rx
from .utils import section_header


def music() -> rx.Component:
    """Music section component."""

    tracks = [
        {
            "title": "Midnight Pulse",
            "genre": "Progressive House",
            "duration": "6:42",
            "image": "/placeholder.svg?height=300&width=300"
        },
        {
            "title": "Digital Dreams",
            "genre": "Techno",
            "duration": "7:15",
            "image": "/placeholder.svg?height=300&width=300"
        },
        {
            "title": "Neon Nights",
            "genre": "Deep House",
            "duration": "5:28",
            "image": "/placeholder.svg?height=300&width=300"
        },
        {
            "title": "Synthetic Soul",
            "genre": "Experimental",
            "duration": "8:03",
            "image": "/placeholder.svg?height=300&width=300"
        },
    ]

    return rx.box(
        rx.container(
            section_header("Latest ", "Releases"),
            rx.text(
                "Explore the latest tracks and discover the sound that defines 10TACLE.",
                class_name="text-gray-400 max-w-2xl text-center -mt-12 mb-16 mx-auto"
            ),

            # Tracks Grid
            rx.grid(
                *[
                    rx.box(
                        rx.box(
                            rx.image(
                                src=track["image"],
                                alt=track["title"],
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

                        # Track Info
                        rx.box(
                            rx.heading(track["title"], size="5", weight="bold", class_name="font-orbitron text-white mb-2"),
                            rx.text(track["genre"], size="2", class_name="text-red-500 font-semibold uppercase tracking-wider mb-3"),
                            rx.flex(
                                rx.icon("clock", size=16, class_name="text-gray-400 mr-2"),
                                rx.text(track["duration"], size="2", class_name="text-gray-400"),
                                align="center"
                            ),
                            class_name="p-6"
                        ),

                        class_name="group bg-gray-900/50 rounded-lg overflow-hidden border border-gray-800 hover:border-red-500/50 transition-all duration-300"
                    )
                    for track in tracks
                ],
                columns={"initial": "1", "sm": "2", "lg": "4"},
                spacing="6"
            ),

            # View All Button
            rx.flex(
                rx.button(
                    "View on Spotify",
                    rx.icon("arrow-right", size=16, class_name="ml-2"),
                    size="3",
                    variant="outline",
                    class_name="border-gray-500 text-gray-300 hover:bg-white hover:text-black font-bold mt-12 tracking-wider"
                ),
                justify="center"
            ),

            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),

        id="music",
        class_name="py-20 bg-black"
    )
