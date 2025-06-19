import reflex as rx


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
            # Section Header
            rx.flex(
                rx.heading(
                    "Latest ",
                    rx.text("Releases", class_name="text-red-500"),
                    size="8",
                    weight="bold",
                    class_name="mb-6"
                ),
                rx.box(class_name="w-24 h-1 bg-red-500 mx-auto mb-8"),
                rx.text(
                    "Explore the latest tracks and discover the sound that defines 10TACLE",
                    size="4",
                    class_name="text-gray-400 max-w-2xl text-center"
                ),
                direction="column",
                align="center",
                class_name="text-center mb-16"
            ),

            # Tracks Grid
            rx.grid(
                *[
                    rx.box(
                        # Track Image
                        rx.box(
                            rx.image(
                                src=track["image"],
                                alt=track["title"],
                                class_name="w-full h-64 object-cover group-hover:scale-105 transition-transform duration-300"
                            ),
                            rx.box(
                                rx.button(
                                    rx.icon("play", size=16),
                                    size="2",
                                    class_name="bg-red-500 hover:bg-red-600 text-white border-0"
                                ),
                                class_name="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center"
                            ),
                            class_name="relative overflow-hidden"
                        ),

                        # Track Info
                        rx.box(
                            rx.heading(track["title"], size="5", weight="bold", class_name="text-white mb-2"),
                            rx.text(track["genre"], size="2", class_name="text-red-500 mb-2"),
                            rx.text(track["duration"], size="2", class_name="text-gray-400 mb-4"),

                            # Action Buttons
                            rx.flex(
                                rx.button(
                                    rx.icon("download", size=16, class_name="mr-1"),
                                    "Download",
                                    size="2",
                                    variant="outline",
                                    class_name="flex-1 border-gray-600 text-gray-300 hover:bg-gray-800 bg-transparent"
                                ),
                                rx.button(
                                    rx.icon("external-link", size=16),
                                    size="2",
                                    variant="outline",
                                    class_name="border-gray-600 text-gray-300 hover:bg-gray-800 bg-transparent"
                                ),
                                spacing="2"
                            ),

                            class_name="p-6"
                        ),

                        class_name="group bg-gray-900/50 rounded-lg overflow-hidden border border-gray-800 hover:border-red-500/50 transition-all duration-300"
                    )
                    for track in tracks
                ],
                # CORRECCIÓN AQUÍ:
                columns={"initial": "1", "sm": "2", "md": "2", "lg": "4"},  # Ajustado para sm y md también
                spacing="8"  # Asegúrate que "8" esté en la escala 0-9. Si no, ajústalo (ej. "6" o "9")
            ),

            # View All Button
            rx.flex(
                rx.button(
                    "View All Releases",
                    size="4",
                    class_name="bg-red-500 hover:bg-red-600 text-white border-0 px-8 mt-12"
                ),
                justify="center"
            ),

            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),

        id="music",
        class_name="py-20 bg-black"
    )
