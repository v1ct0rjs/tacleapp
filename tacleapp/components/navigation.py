import reflex as rx
from ..state import State


def navigation() -> rx.Component:
    """Navigation component with mobile menu."""
    # nav_links = [
    #     {"name": "Home", "href": "#home"},
    #     {"name": "About", "href": "#about"},
    #     {"name": "Music", "href": "#music"},
    #     {"name": "Events", "href": "#events"},
    #     {"name": "Contact", "href": "#contact"},
    # ]
    nav_links = [
        {"name": "Home", "href": "#home"},
        {"name": "Music", "href": "#music"},
        {"name": "Contact", "href": "#contact"},
    ]

    return rx.box(
        # Desktop Navigation
        rx.box(
            rx.container(
                rx.flex(
                    # Logo
                    rx.link(
                        rx.image(
                            src="/logo_header.png",
                            alt="10TACLE Logo",
                            class_name="h-6 sm:h-8 w-auto"
                        ),
                        href="#home"
                    ),

                    # Desktop Menu
                    rx.flex(
                        *[
                            rx.link(
                                link["name"],
                                href=link["href"],
                                class_name="text-gray-300 hover:text-white transition-colors duration-300 font-medium tracking-wider"
                            )
                            for link in nav_links
                        ],
                        spacing="6",
                        class_name="hidden md:flex items-center"
                    ),

                    # Mobile Menu Button
                    rx.button(
                        rx.cond(
                            State.is_mobile_menu_open,
                            rx.icon("x", size=24),
                            rx.icon("menu", size=24)
                        ),
                        on_click=State.toggle_mobile_menu,
                        class_name="md:hidden text-white hover:text-red-500 transition-colors bg-transparent border-none p-2"
                    ),

                    justify="between",
                    align="center",
                    class_name="h-20"
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
            ),
            class_name="fixed top-0 w-full z-50 bg-black/80 backdrop-blur-md border-b border-gray-800"
        ),

        # Mobile Menu
        rx.cond(
            State.is_mobile_menu_open,
            rx.box(
                rx.flex(
                    *[
                        rx.link(
                            link["name"],
                            href=link["href"],
                            on_click=State.close_mobile_menu,
                            class_name="block px-4 py-3 text-lg text-center text-gray-200 hover:bg-red-500 hover:text-white transition-colors duration-300"
                        )
                        for link in nav_links
                    ],
                    direction="column",
                    spacing="1"
                ),
                class_name="fixed top-20 left-0 right-0 z-40 md:hidden bg-black/95 backdrop-blur-md border-b border-gray-800"
            )
        )
    )
