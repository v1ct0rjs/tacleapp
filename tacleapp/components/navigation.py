import reflex as rx
from ..state import State


def navigation() -> rx.Component:
    nav_links = [
        {"name": "Home", "href": "#home"},
        {"name": "Music", "href": "#music"},
        {"name": "Contact", "href": "#contact"},
    ]

    return rx.box(
        # Debug text to show the state of is_mobile_menu_open
        # rx.text(
        #     State.is_mobile_menu_open.to_string(),
        #     class_name="fixed top-24 left-4 text-xs text-white z-[9999] bg-purple-600 p-1 rounded"
        # ),
        rx.box(
            rx.container(
                rx.flex(
                    rx.link(
                        rx.image(
                            src="/logo_header.png",
                            alt="10TACLE Logo",
                            class_name="h-6 sm:h-8 w-auto"
                        ),
                        href="#home",
                        on_click=State.close_mobile_menu
                    ),
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
                    rx.button(
                        rx.cond(
                            State.is_mobile_menu_open,
                            rx.icon("x", size=24, key="close-icon"), # Added key for stability
                            rx.icon("menu", size=24, key="menu-icon")  # Added key for stability
                        ),
                        on_click=State.toggle_mobile_menu,
                        class_name="md:hidden text-white hover:text-red-500 focus:outline-none bg-transparent border-0 p-2 transition-colors"
                    ),
                    justify="between",
                    align="center",
                    class_name="h-20" # Navbar height
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
            ),
            class_name="fixed top-0 w-full z-50 bg-black/80 backdrop-blur-md border-b border-gray-800"
        ),
        # Mobile Menu
        # Using rx.fragment to avoid issues with rx.cond directly returning None if not careful
        rx.fragment(
            rx.cond(
                State.is_mobile_menu_open,
                rx.box(
                    rx.flex(
                        *[
                            rx.link(
                                link["name"],
                                href=link["href"],
                                on_click=State.close_mobile_menu,
                                class_name="block w-full px-4 py-4 text-lg text-center text-gray-200 hover:bg-red-500 hover:text-white transition-colors duration-300"
                            )
                            for link in nav_links
                        ],
                        direction="column",
                        width="100%",
                        align="stretch"
                    ),
                    class_name=(
                        "fixed top-20 left-0 right-0 z-40 md:hidden " # top-20 matches navbar height
                        "bg-black/95 backdrop-blur-lg border-b border-gray-700 shadow-xl "
                        "transform transition-transform duration-300 ease-in-out" # Base for transition
                    ),
                    # Apply transform based on state for slide-in/out effect (optional)
                    # style={"transform": rx.cond(State.is_mobile_menu_open, "translateY(0%)", "translateY(-100%)")}
                    padding_y="2"
                )
            )
        )
    )
