import reflex as rx

def section_header(title: str, highlight: str) -> rx.Component:
    """Reusable section header."""
    return rx.flex(
        rx.heading(
            title,
            rx.text(highlight, as_="span", class_name="text-red-500"),
            size="8",
            weight="bold",
            class_name="font-orbitron tracking-widest uppercase"
        ),
        rx.box(class_name="w-24 h-0.5 bg-red-500 mt-4 mb-8"),
        direction="column",
        align="center",
        class_name="text-center mb-16"
    )
