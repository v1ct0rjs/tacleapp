import reflex as rx
from .components.stage3d import Stage3d

def index() -> rx.Component:
    return rx.vstack(
        rx.heading("DJ 10tacle", size="7", weight="bold"),
        Stage3d(height="60vh", width="100%"),
        rx.text("Nuevos lanzamientos · Próximos eventos", margin_top="2em"),
        gap="2em", align="center", padding="2em",
    )

app = rx.App()
app.add_page(index, title="DJ 10tacle")




