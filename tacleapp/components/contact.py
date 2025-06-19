import reflex as rx
from ..state import State


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
            # Section Header
            rx.flex(
                rx.heading(
                    "Get In ",
                    rx.text("Touch", class_name="text-red-500"),
                    size="8",
                    weight="bold",
                    class_name="mb-6"
                ),
                rx.box(class_name="w-24 h-1 bg-red-500 mx-auto mb-8"),
                rx.text(
                    "Ready to book a performance or collaborate? Let's create something amazing together.",
                    size="4",
                    class_name="text-gray-400 max-w-2xl text-center"
                ),
                direction="column",
                align="center",
                class_name="text-center mb-16"
            ),

            # Content Grid
            rx.grid(
                # Contact Form
                rx.box(
                    rx.heading("Send a Message", size="6", weight="bold", class_name="text-white mb-6"),

                    rx.form(
                        rx.flex(
                            # Name and Email Row
                            rx.grid(
                                rx.input(
                                    placeholder="Your Name",
                                    value=State.contact_name,
                                    on_change=State.set_contact_name,
                                    class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500"
                                ),
                                rx.input(
                                    type="email",
                                    placeholder="Your Email",
                                    value=State.contact_email,
                                    on_change=State.set_contact_email,
                                    class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500"
                                ),
                                # CORRECCIÓN AQUÍ:
                                columns={"initial": "1", "sm": "2"},
                                spacing="4"  # Asegúrate que "4" esté en la escala 0-9
                            ),

                            # Subject
                            rx.input(
                                placeholder="Subject",
                                value=State.contact_subject,
                                on_change=State.set_contact_subject,
                                class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500"
                            ),

                            # Message
                            rx.text_area(
                                placeholder="Your Message",
                                value=State.contact_message,
                                on_change=State.set_contact_message,
                                rows="6",
                                class_name="bg-gray-800 border-gray-700 text-white placeholder-gray-400 focus:border-red-500 resize-none"
                            ),

                            # Submit Button
                            rx.button(
                                "Send Message",
                                type="submit",
                                size="4",
                                class_name="w-full bg-red-500 hover:bg-red-600 text-white border-0"
                            ),

                            direction="column",
                            spacing="6"  # Asegúrate que "6" esté en la escala 0-9
                        ),
                        on_submit=State.submit_contact_form,
                        reset_on_submit=False  # Mantener así o cambiar a True si se prefiere
                    ),

                    class_name="bg-gray-900/50 rounded-lg p-8 border border-gray-800"
                ),

                # Contact Info
                rx.flex(
                    # Contact Information
                    rx.box(
                        rx.heading("Contact Information", size="6", weight="bold", class_name="text-white mb-6"),
                        rx.flex(
                            rx.flex(
                                rx.icon("mail", size=20, class_name="text-red-500 mr-4"),
                                rx.text("booking@dj10tacle.com", class_name="text-gray-300"),
                                align="center"
                            ),
                            rx.flex(
                                rx.icon("phone", size=20, class_name="text-red-500 mr-4"),
                                rx.text("+1 (555) 123-4567", class_name="text-gray-300"),
                                align="center"
                            ),
                            rx.flex(
                                rx.icon("map-pin", size=20, class_name="text-red-500 mr-4"),
                                rx.text("Los Angeles, CA", class_name="text-gray-300"),
                                align="center"
                            ),
                            direction="column",
                            spacing="4"  # Asegúrate que "4" esté en la escala 0-9
                        )
                    ),

                    # Social Media
                    rx.box(
                        rx.heading("Follow the Journey", size="5", weight="bold", class_name="text-white mb-4"),
                        rx.flex(
                            *[
                                rx.link(
                                    rx.icon(social["icon"], size=20),
                                    href=social["href"],
                                    class_name="w-12 h-12 bg-gray-800 rounded-lg flex items-center justify-center text-gray-400 hover:text-white hover:bg-red-500 transition-all duration-300"
                                )
                                for social in social_links
                            ],
                            spacing="4"  # Asegúrate que "4" esté en la escala 0-9
                        )
                    ),

                    # Booking Info
                    rx.box(
                        rx.heading("Booking Inquiries", size="4", weight="bold", class_name="text-white mb-3"),
                        rx.text(
                            "For booking requests, please include event details, date, location, and budget range.",
                            size="2",
                            class_name="text-gray-400 mb-4"
                        ),
                        rx.text("Response time: 24-48 hours", size="2", class_name="text-gray-400"),
                        class_name="bg-gray-900/50 rounded-lg p-6 border border-gray-800"
                    ),

                    direction="column",
                    spacing="8"  # Asegúrate que "8" esté en la escala 0-9
                ),

                # CORRECCIONES AQUÍ para el grid principal:
                columns={"initial": "1", "md": "2"},  # Ajustado, antes era ["1", "1", "2"]
                spacing="9"  # Ajustado, antes era "12"
            ),

            # Footer
            rx.box(
                rx.text("© 2024 DJ 10TACLE. All rights reserved.", class_name="text-gray-400 text-center"),
                class_name="mt-20 pt-8 border-t border-gray-800"
            ),

            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
        ),

        id="contact",
        class_name="py-20 bg-black"
    )
