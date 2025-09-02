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
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    body, html {
        margin: 0 !important;
        padding: 0 !important;
        overflow-x: hidden;
        background-color: #000000;
    }

    .futuristic-bg {
        position: relative;
        background: 
            linear-gradient(rgba(255,255,255,0.15) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.15) 1px, transparent 1px),
            radial-gradient(circle, rgba(255,255,255,0.08) 1px, transparent 1px);
        background-size: 40px 40px, 40px 40px, 20px 20px;
        animation: matrix-drift 20s linear infinite;
        min-height: 100vh;
    }

    .futuristic-bg::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 100%;
        background: linear-gradient(transparent 98%, rgba(255,255,255,0.3) 99%, transparent 100%);
        background-size: 100% 100px;
        animation: scan-line 6s linear infinite;
        pointer-events: none;
        z-index: 1;
    }

    .futuristic-bg::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(255,255,255,0.15) 1px, transparent 2px),
            radial-gradient(circle at 80% 20%, rgba(255,255,255,0.15) 1px, transparent 2px),
            radial-gradient(circle at 40% 40%, rgba(255,255,255,0.12) 1px, transparent 2px);
        background-size: 60px 60px, 80px 80px, 100px 100px;
        animation: particles-float 15s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }

    /* Ensure content appears above background effects */
    .futuristic-bg > * {
        position: relative;
        z-index: 2;
    }

    @keyframes matrix-drift {
        0% { transform: translateY(0) translateX(0); }
        100% { transform: translateY(40px) translateX(20px); }
    }

    @keyframes scan-line {
        0% { transform: translateY(-100px); opacity: 0; }
        10% { opacity: 0.8; }
        90% { opacity: 0.8; }
        100% { transform: translateY(100vh); opacity: 0; }
    }

    @keyframes particles-float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        33% { transform: translateY(-20px) rotate(120deg); }
        66% { transform: translateY(10px) rotate(240deg); }
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
