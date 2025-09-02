import reflex as rx
from .state import State
from .components import navigation, hero, music, events, contact

GTAG = "G-MBP9JLGSZ5"


def index() -> rx.Component:
    """Main page component with simplified futuristic background effects."""
    return rx.box(
        # Main content with background effects
        navigation(),
        hero(),
        music(),
        contact(),
        class_name="futuristic-bg",
        style={
            "background_color": "#000000",
            "color": "#ffffff",
            "margin": "0",
            "padding": "0",
            "width": "100%"
        }
    )


def get_custom_css():
    return """
    /* Reset básico */
    * { margin:0; padding:0; box-sizing:border-box; }

    /* 1 sola zona de scroll y sin desplazamiento horizontal */
    html, body, #__next {
        height: 100%;
        min-height: 100%;
        overflow-x: clip; /* evita doble barra horizontal por sombras/transform */
        background-color: #000;
    }

    /* Contenedor raíz de la página */
    .futuristic-bg {
        position: relative;
        isolation: isolate; /* crea un stacking context propio */
        min-height: 100%;
        /* Fondo base (grid + puntos) atado al viewport para que abarque toda la página */
        background:
            linear-gradient(rgba(255,255,255,0.12) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.12) 1px, transparent 1px),
            radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px);
        background-size: 40px 40px, 40px 40px, 20px 20px;
        /* Esta línea hace que el fondo se mantenga mientras haces scroll */
        background-attachment: fixed, fixed, fixed;
    }

    /* Overlays animados pegados al viewport (no al alto del contenedor) */
    .futuristic-bg::before,
    .futuristic-bg::after {
        content: "";
        position: fixed;   /* clave: fijo al viewport */
        inset: 0;          /* top/right/bottom/left: 0 */
        pointer-events: none;
        z-index: 0;        /* debajo del contenido */
    }

    .futuristic-bg::before {
        background: linear-gradient(transparent 98%, rgba(255,255,255,0.25) 99%, transparent 100%);
        background-size: 100% 100px;
        animation: scan-line 6s linear infinite;
        opacity: .7;
    }

    .futuristic-bg::after {
        background:
            radial-gradient(circle at 20% 80%, rgba(255,255,255,0.12) 1px, transparent 2px),
            radial-gradient(circle at 80% 20%, rgba(255,255,255,0.12) 1px, transparent 2px),
            radial-gradient(circle at 40% 40%, rgba(255,255,255,0.08) 1px, transparent 2px);
        background-size: 60px 60px, 80px 80px, 100px 100px;
        animation: particles-float 15s ease-in-out infinite;
    }

    /* El contenido siempre por encima de los overlays */
    .futuristic-bg > * {
        position: relative;
        z-index: 1;
    }

    @keyframes scan-line {
        0%   { transform: translateY(0); }
        100% { transform: translateY(100px); }
    }
    @keyframes particles-float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        33%      { transform: translateY(-20px) rotate(120deg); }
        66%      { transform: translateY(10px) rotate(240deg); }
    }
    """



# Create the app
app = rx.App(
    _state=State,
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
        rx.html(
            '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">'),
        rx.html(f"<style>{get_custom_css()}</style>"),
    ],
)

# Add the main page
app.add_page(
    index,
    title="10tacle - Electronic Music Producer & DJ",
    description="Official website of 10tacle - Electronic music producer, DJ and radio host"
)
