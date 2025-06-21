import reflex as rx
from .state import State
from .components import navigation, hero, about, music, events, contact

def index() -> rx.Component:
  """Main page component."""
  return rx.box(
      navigation(),
      hero(),
      about(),
      music(),
      events(),
      contact(),
      class_name="min-h-screen bg-black text-white"
  )

# Create the app
app = rx.App(
  _state=State,  # <--- CORRECCIÓN AQUÍ
  style={
      "font_family": "'Poppins', sans-serif",
      "background_color": "#000000",
      "color": "#ffffff",
  }
)

# Add the main page
app.add_page(
  index,
  title="DJ 10tacle - Electronic Music Producer & DJ",
  description="Official website of DJ 10tacle - Electronic music producer, DJ and performer"
)
