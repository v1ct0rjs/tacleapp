import reflex as rx
from .components.stage3d import stage3d # Asegúrate de que esta importación esté descomentada

def index() -> rx.Component:
    return rx.vstack(
        rx.heading("DJ 10tacle", size="7", weight="bold"),
        stage3d(height="60vh", width="100%"), # Usamos stage3d de nuevo
        rx.text("Nuevos lanzamientos · Próximos eventos", margin_top="2em"),
        gap="2em", align="center", padding="2em",
    )

app = rx.App()
app.add_page(index, title="DJ 10tacle")






