import reflex as rx


def hero() -> rx.Component:
    """Hero section component."""
    return rx.box(
        # Background with gradient
        rx.box(
            class_name="absolute inset-0 bg-gradient-to-br from-black via-gray-900 to-black"
        ),
        rx.box(
            class_name="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-red-900/20 via-transparent to-transparent"
        ),

        # Animated Music Bars
        rx.flex(
            *[
                rx.box(
                    class_name=f"bg-red-500 w-1 animate-pulse",
                    style={
                        "height": f"{20 + (i % 5) * 20}px",
                        "animation-delay": f"{i * 0.1}s"
                    }
                )
                for i in range(50)
            ],
            class_name="absolute bottom-0 left-0 right-0 justify-center items-end space-x-1 opacity-30",
            spacing="1"
        ),

        # Content
        rx.container(
            rx.flex(
                # Music Icon
                rx.box(
                    rx.icon("music", size=64, class_name="text-red-500 mx-auto mb-4"),
                    class_name="animate-pulse"
                ),

                # Main Title
                rx.heading(
                    "DJ 10TACLE",
                    size="9",
                    weight="bold",
                    class_name="bg-gradient-to-r from-white via-red-500 to-white bg-clip-text text-transparent mb-6"
                ),

                # Subtitle
                rx.text(
                    "Electronic Music Producer & DJ",
                    size="6",
                    class_name="text-gray-300 mb-8"
                ),

                # Description
                rx.text(
                    "Transforming beats into experiences. From underground clubs to main stages, bringing you the finest electronic music that moves your soul.",
                    size="4",
                    class_name="text-gray-400 mb-12 max-w-3xl text-center"
                ),

                # Buttons
                rx.flex(
                    rx.button(
                        rx.icon("play", size=20, class_name="mr-2"),
                        "Listen Now",
                        size="4",
                        class_name="bg-red-500 hover:bg-red-600 text-white border-0 px-8 py-3 shadow-lg shadow-red-500/25"
                    ),
                    rx.button(
                        "View Events",
                        size="4",
                        variant="outline",
                        class_name="border-white text-white hover:bg-white hover:text-black px-8 py-3 bg-transparent"
                    ),
                    spacing="4",
                    class_name="flex-col sm:flex-row"
                ),

                direction="column",
                align="center",
                class_name="text-center"
            ),
            class_name="relative z-10 max-w-4xl mx-auto px-4"
        ),

        id="home",
        class_name="relative min-h-screen flex items-center justify-center overflow-hidden pt-16"
    )
