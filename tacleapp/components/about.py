import reflex as rx
from .utils import section_header


def about() -> rx.Component:
    """About section component."""

    stats = [
        {"icon": "headphones", "label": "Years Experience", "value": "8+"},
        {"icon": "disc", "label": "Tracks Released", "value": "150+"},
        {"icon": "users", "label": "Live Performances", "value": "200+"},
        {"icon": "award", "label": "Awards Won", "value": "12"},
    ]

    return rx.box(
        rx.container(
            section_header("About ", "10TACLE"),

            # Content Grid
            rx.grid(
                # Text Content
                rx.box(
                    rx.heading("The Journey", size="6", weight="bold", class_name="font-orbitron text-white mb-6"),
                    rx.text(
                        "Born from a passion for electronic music, DJ 10TACLE has been pushing boundaries and creating unforgettable experiences for over 8 years. Starting from underground venues to headlining major festivals, the journey has been nothing short of extraordinary.",
                        class_name="text-gray-300 mb-6 leading-relaxed"
                    ),
                    rx.text(
                        "Specializing in progressive house, techno, and experimental electronic sounds, 10TACLE creates a unique sonic landscape that connects with audiences on a deeper level.",
                        class_name="text-gray-300 leading-relaxed"
                    ),
                ),

                # Stats Grid
                rx.grid(
                    *[
                        rx.box(
                            rx.icon(stat["icon"], size=32, class_name="text-red-500 mb-4"),
                            rx.text(stat["value"], size="7", weight="bold", class_name="font-orbitron text-white mb-2"),
                            rx.text(stat["label"], size="2", class_name="text-gray-400 uppercase tracking-wider"),
                            class_name="bg-gray-900/50 p-6 rounded-lg border border-gray-800 text-center"
                        )
                        for stat in stats
                    ],
                    columns="2",
                    spacing="6"
                ),

                columns={"initial": "1", "md": "2"},
                spacing="9",
                align="center"
            ),

            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),

        id="about",
        class_name="py-20 bg-gradient-to-b from-black to-gray-900"
    )
