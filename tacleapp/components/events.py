import reflex as rx
from .utils import section_header


def events() -> rx.Component:
    """Events section component."""

    upcoming_events = [
        {
            "date": "FEB 15",
            "title": "Underground Sessions",
            "venue": "Club Nexus",
            "location": "Berlin, Germany",
        },
        {
            "date": "FEB 28",
            "title": "Electronic Nights Festival",
            "venue": "Main Stage",
            "location": "Amsterdam, Netherlands",
        },
        {
            "date": "MAR 12",
            "title": "Techno Revolution",
            "venue": "Warehouse 23",
            "location": "London, UK",
        }
    ]

    return rx.box(
        rx.container(
            section_header("Upcoming ", "Events"),
            rx.text(
                "Don't miss out on the next electrifying performance.",
                class_name="text-gray-400 max-w-2xl text-center -mt-12 mb-16 mx-auto"
            ),

            # Upcoming Events List
            rx.flex(
                *[
                    rx.flex(
                        # Date
                        rx.box(
                            rx.text(event["date"], class_name="font-orbitron text-red-500 text-xl font-bold text-center"),
                            class_name="w-24 flex-shrink-0"
                        ),
                        # Divider
                        rx.box(class_name="w-px bg-gray-700 mx-6 hidden sm:block"),
                        # Event Info
                        rx.box(
                            rx.heading(event["title"], size="5", weight="bold", class_name="font-orbitron text-white mb-1"),
                            rx.text(f"{event['venue']} • {event['location']}", class_name="text-gray-400"),
                            class_name="flex-1"
                        ),
                        # Action Button
                        rx.button(
                            "Get Tickets",
                            size="2",
                            class_name="bg-red-500 hover:bg-red-600 text-white font-bold border-0 tracking-wider ml-4"
                        ),
                        align="center",
                        justify="between",
                        class_name="bg-gray-900/50 rounded-lg p-6 border border-gray-800 hover:border-red-500/50 transition-all duration-300 w-full flex-col sm:flex-row"
                    )
                    for event in upcoming_events
                ],
                direction="column",
                spacing="4"
            ),

            class_name="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8"
        ),

        id="events",
        class_name="py-20 bg-gradient-to-b from-gray-900 to-black"
    )
