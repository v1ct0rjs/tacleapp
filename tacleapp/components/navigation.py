import reflex as rx
from ..state import State


def navigation() -> rx.Component:
    """Navigation component with mobile menu."""
    return rx.box(
        # Desktop Navigation
        rx.box(
            rx.container(
                rx.flex(
                    # Logo
                    rx.heading(
                        "DJ 10TACLE",
                        size="7",
                        weight="bold",
                        class_name="bg-gradient-to-r from-white via-red-500 to-white bg-clip-text text-transparent"
                    ),

                    # Desktop Menu
                    rx.flex(
                        rx.link("Home", href="#home",
                                class_name="text-white hover:text-red-500 transition-colors duration-300 font-medium"),
                        rx.link("About", href="#about",
                                class_name="text-white hover:text-red-500 transition-colors duration-300 font-medium"),
                        rx.link("Music", href="#music",
                                class_name="text-white hover:text-red-500 transition-colors duration-300 font-medium"),
                        rx.link("Events", href="#events",
                                class_name="text-white hover:text-red-500 transition-colors duration-300 font-medium"),
                        rx.link("Contact", href="#contact",
                                class_name="text-white hover:text-red-500 transition-colors duration-300 font-medium"),
                        spacing="8",
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
                        class_name="md:hidden text-white hover:text-red-500 transition-colors bg-transparent border-none"
                    ),

                    justify="between",
                    align="center",
                    class_name="h-16"
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"
            ),
            class_name="fixed top-0 w-full z-50 bg-black/90 backdrop-blur-sm border-b border-red-500/20"
        ),

        # Mobile Menu
        rx.cond(
            State.is_mobile_menu_open,
            rx.box(
                rx.flex(
                    rx.link("Home", href="#home", on_click=State.close_mobile_menu,
                            class_name="block px-3 py-2 text-white hover:text-red-500 transition-colors duration-300"),
                    rx.link("About", href="#about", on_click=State.close_mobile_menu,
                            class_name="block px-3 py-2 text-white hover:text-red-500 transition-colors duration-300"),
                    rx.link("Music", href="#music", on_click=State.close_mobile_menu,
                            class_name="block px-3 py-2 text-white hover:text-red-500 transition-colors duration-300"),
                    rx.link("Events", href="#events", on_click=State.close_mobile_menu,
                            class_name="block px-3 py-2 text-white hover:text-red-500 transition-colors duration-300"),
                    rx.link("Contact", href="#contact", on_click=State.close_mobile_menu,
                            class_name="block px-3 py-2 text-white hover:text-red-500 transition-colors duration-300"),
                    direction="column",
                    spacing="1"
                ),
                class_name="fixed top-16 left-0 right-0 z-40 md:hidden bg-black/95 backdrop-blur-sm border-b border-red-500/20 px-2 pt-2 pb-3"
            )
        )
    )
