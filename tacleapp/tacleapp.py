import reflex as rx
from .state import State
from .components import navigation, hero, about, music, events, contact

GTAG = "G-MBP9JLGSZ5"

def index() -> rx.Component:
  """Main page component."""
  return rx.box(
      navigation(),
      hero(),
      #about(),
      music(),
      #events(),
      contact(),
      class_name="min-h-screen bg-black text-white"
  )

# Create the app
app = rx.App(
    _state=State,
    stylesheets=["/styles.css"],
    style={
        "font_family": "'Poppins', sans-serif",
        "background_color": "#000000",
        "color": "#ffffff",
    },
head_components=[
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={GTAG}"),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{GTAG}');
            """),
    ],
)

# Add the main page
app.add_page(
  index,
  title="10tacle - Electronic Music Producer & DJ",
  description="Official website of 10tacle - Electronic music producer, DJ and radio host"
)
