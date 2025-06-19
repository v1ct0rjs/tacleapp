import reflex as rx


def events() -> rx.Component:
    """Events section component."""

    upcoming_events = [
        {
            "date": "2024-02-15",
            "title": "Underground Sessions",
            "venue": "Club Nexus",
            "location": "Berlin, Germany",
            "time": "23:00"
        },
        {
            "date": "2024-02-28",
            "title": "Electronic Nights Festival",
            "venue": "Main Stage",
            "location": "Amsterdam, Netherlands",
            "time": "21:30"
        },
        {
            "date": "2024-03-12",
            "title": "Techno Revolution",
            "venue": "Warehouse 23",
            "location": "London, UK",
            "time": "22:00"
        }
    ]

    past_events = [
        {
            "date": "2024-01-20",
            "title": "New Year Beats",
            "venue": "Sky Lounge",
            "location": "Miami, USA",
            "time": "20:00"
        }
    ]

    return rx.box(
        rx.container(
            # Section Header
            rx.flex(
                rx.heading(
                    "Upcoming ",
                    rx.text("Events", class_name="text-red-500"),
                    size="8",
                    weight="bold",
                    class_name="mb-6"
                ),
                rx.box(class_name="w-24 h-1 bg-red-500 mx-auto mb-8"),
                rx.text(
                    "Don't miss out on the next electrifying performance",
                    size="4",
                    class_name="text-gray-400 max-w-2xl text-center"
                ),
                direction="column",
                align="center",
                class_name="text-center mb-16"
            ),

            # Upcoming Events
            rx.box(
                rx.heading("Coming Up", size="6", weight="bold", class_name="text-white mb-8"),
                rx.flex(
                    *[
                        rx.box(
                            rx.flex(
                                # Event Info
                                rx.box(
                                    rx.flex(  # Flex para fecha y hora
                                        rx.flex(
                                            rx.icon("calendar", size=20, class_name="text-red-500 mr-2"),
                                            rx.text(event["date"], class_name="text-red-500 font-medium"),
                                            align="center",
                                            class_name="mb-2"
                                        ),
                                        rx.flex(
                                            rx.icon("clock", size=20, class_name="text-gray-400 mr-2"),
                                            rx.text(event["time"], class_name="text-gray-400"),
                                            align="center"
                                        ),
                                        # CORRECCIÓN AQUÍ:
                                        direction={"initial": "column", "sm": "row"},
                                        spacing="4",  # Asegúrate que "4" esté en la escala 0-9
                                        class_name="mb-4"
                                    ),

                                    rx.heading(event["title"], size="6", weight="bold", class_name="text-white mb-2"),

                                    rx.flex(
                                        rx.icon("map-pin", size=16, class_name="text-gray-400 mr-2"),
                                        rx.text(f"{event['venue']} • {event['location']}", class_name="text-gray-300"),
                                        align="center"
                                    ),

                                    class_name="flex-1"
                                ),

                                # Action Buttons
                                rx.flex(
                                    rx.button(
                                        rx.icon("ticket", size=16, class_name="mr-2"),
                                        "Get Tickets",
                                        size="3",
                                        class_name="bg-red-500 hover:bg-red-600 text-white border-0"
                                    ),
                                    rx.button(
                                        "More Info",
                                        size="3",
                                        variant="outline",
                                        class_name="border-gray-600 text-gray-300 hover:bg-gray-700 bg-transparent"
                                    ),
                                    spacing="3"  # Asegúrate que "3" esté en la escala 0-9
                                ),

                                # CORRECCIÓN AQUÍ para el flex principal de la tarjeta de evento:
                                direction={"initial": "column", "md": "row"},
                                justify="between",
                                align={"initial": "start", "md": "center"},  # También se puede hacer responsivo
                                spacing="4"  # Asegúrate que "4" esté en la escala 0-9
                            ),
                            class_name="bg-gray-800/50 rounded-lg p-6 border border-gray-700 hover:border-red-500/50 transition-all duration-300"
                        )
                        for event in upcoming_events
                    ],
                    direction="column",
                    spacing="6"  # Asegúrate que "6" esté en la escala 0-9
                ),
                class_name="mb-16"
            ),

            # Past Events
            rx.box(
                rx.heading("Recent Performances", size="6", weight="bold", class_name="text-white mb-8"),
                rx.grid(
                    *[
                        rx.box(
                            rx.flex(
                                rx.icon("calendar", size=16, class_name="text-gray-500 mr-2"),
                                rx.text(event["date"], size="2", class_name="text-gray-500"),
                                align="center",
                                class_name="mb-3"
                            ),
                            rx.heading(event["title"], size="5", weight="bold", class_name="text-gray-300 mb-2"),
                            rx.flex(
                                rx.icon("map-pin", size=16, class_name="text-gray-400 mr-2"),
                                rx.text(f"{event['venue']} • {event['location']}", size="2",
                                        class_name="text-gray-400"),
                                align="center"
                            ),
                            class_name="bg-gray-900/30 rounded-lg p-6 border border-gray-800 opacity-75"
                        )
                        for event in past_events
                    ],
                    columns={"initial": "1", "md": "2"},  # Corregido por consistencia, antes era ["1", "2"]
                    spacing="6"  # Asegúrate que "6" esté en la escala 0-9
                )
            ),

            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),

        id="events",
        class_name="py-20 bg-gradient-to-b from-gray-900 to-black"
    )
