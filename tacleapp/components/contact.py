import reflex as rx
from ..state import State
from .utils import section_header


def contact() -> rx.Component:
    """Contact section component."""

    social_links = [
        {"icon": "instagram", "href": "#", "label": "Instagram"},
        {"icon": "twitter", "href": "#", "label": "Twitter"},
        {"icon": "facebook", "href": "#", "label": "Facebook"},
        {"icon": "youtube", "href": "#", "label": "YouTube"},
    ]

    return rx.box(
        rx.container(
            section_header("Get In ", "Touch"),
            rx.text(
                "Ready to book a performance or collaborate? Let's create something amazing together.",
                class_name="text-gray-400 max-w-2xl text-center -mt-12 mb-16 mx-auto"
            ),

            # Content Grid
            rx.grid(
                # Contact Form
                rx.box(
                    rx.heading("Send a Message", size="6", weight="bold", class_name="font-orbitron text-white mb-6"),
                    rx.form(
                        rx.flex(
                            rx.grid(
                                rx.input(
                                    placeholder="Your Name", name="name",
                                    class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-500 focus:border-red-500 focus:ring-red-500"
                                ),
                                rx.input(
                                    type="email", placeholder="Your Email", name="email",
                                    class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-500 focus:border-red-500 focus:ring-red-500"
                                ),
                                columns={"initial": "1", "sm": "2"},
                                spacing="4"
                            ),
                            rx.input(
                                placeholder="Subject", name="subject",
                                class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-500 focus:border-red-500 focus:ring-red-500"
                            ),
                            rx.text_area(
                                placeholder="Your Message", name="message",
                                rows="5",
                                class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-500 focus:border-red-500 focus:ring-red-500 resize-none"
                            ),
                            rx.button(
                                "Send Message",
                                type="submit",
                                size="3",
                                class_name="w-full bg-red-500 hover:bg-red-600 text-white font-bold border-0 tracking-wider"
                            ),
                            direction="column",
                            spacing="4"
                        ),
                        on_submit=State.submit_contact_form,
                        reset_on_submit=True
                    ),
                    class_name="bg-gray-900/50 rounded-lg p-8 border border-gray-800"
                ),

                # Contact Info
                rx.flex(
                    rx.box(
                        rx.heading("Contact Info", size="5", weight="bold", class_name="font-orbitron text-white mb-4"),
                        rx.flex(
                            rx.flex(rx.icon("mail", size=18, class_name="text-red-500 mr-3"), rx.text("booking@dj10tacle.com"), align="center"),
                            rx.flex(rx.icon("phone", size=18, class_name="text-red-500 mr-3"), rx.text("+1 (555) 123-4567"), align="center"),
                            rx.flex(rx.icon("map-pin", size=18, class_name="text-red-500 mr-3"), rx.text("Los Angeles, CA"), align="center"),
                            direction="column",
                            spacing="3"
                        )
                    ),
                    rx.box(
                        rx.heading("Follow Me", size="5", weight="bold", class_name="font-orbitron text-white mb-4"),
                        rx.flex(
                            *[
                                rx.link(
                                    rx.icon(social["icon"], size=20),
                                    href=social["href"],
                                    is_external=True,
                                    class_name="w-10 h-10 bg-gray-800 rounded-lg flex items-center justify-center text-gray-400 hover:text-white hover:bg-red-500 transition-all duration-300"
                                )
                                for social in social_links
                            ],
                            spacing="3"
                        )
                    ),
                    direction="column",
                    spacing="6",
                    class_name="p-8"
                ),

                columns={"initial": "1", "lg": "2"},
                spacing="6"
            ),

            # Footer
            rx.box(
                rx.text("© 2024 10TACLE. All rights reserved.", size="2", class_name="text-gray-500 text-center"),
                class_name="mt-20 pt-8 border-t border-gray-800"
            ),

            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),

        id="contact",
        class_name="py-20 bg-black"
    )
