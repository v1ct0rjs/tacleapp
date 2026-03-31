import reflex as rx
from .state import State
from .components import navigation, hero, music, events, contact

GTAG = "G-MBP9JLGSZ5"

def index() -> rx.Component:
    """Main page component with futuristic background effects."""
    return rx.box(
        navigation(),
        rx.box(hero(), as_="section", id="home", class_name="section-tight"),
        rx.box(music(), as_="section", id="music", class_name="section-tight"),
        rx.box(contact(), as_="section", id="contact", class_name="section-tight"),
        class_name="futuristic-bg nav-offset",
        style={
            "background_color": "#000000",
            "color": "#ffffff",
            "margin": "0",
            "padding": "0",
            "width": "100%",
        },
    )


def get_custom_css():
    return """
    /* Propiedades animables para los colores de la rejilla */
    @property --grid-c1 {
      syntax: '<color>';
      inherits: true;
      initial-value: rgba(255, 0, 0, 0.12);
    }
    @property --grid-c2 {
      syntax: '<color>';
      inherits: true;
      initial-value: rgba(255, 0, 0, 0.08);
    }

    :root {
      --grid-size: 128px;
      --grid-cycle: 25s; /* intervalo entre transiciones (antes 6s) */
      --grid-c1: rgba(255, 0, 0, 0.12);
      --grid-c2: rgba(255, 0, 0, 0.08);
    }

    @media (max-width: 767px) {
      :root { --grid-size: 12px; }
    }

    * { margin:0; padding:0; box-sizing:border-box; }

    html, body, #__next {
        height: 100%;
        min-height: 100%;
        overflow-x: clip;
        background-color: #000;
    }

    .futuristic-bg {
        position: relative;
        isolation: isolate;
        min-height: 100%;
        background-image:
            linear-gradient(0deg, transparent calc(var(--grid-size) - 1px), var(--grid-c1) 1px),
            linear-gradient(90deg, transparent calc(var(--grid-size) - 1px), var(--grid-c2) 1px);
        background-size: var(--grid-size) var(--grid-size), var(--grid-size) var(--grid-size);
        background-position: 0 0, 0 0;
        background-attachment: fixed, fixed;

        /* Jitter + transición lenta con pico rápido cada var(--grid-cycle) */
        animation:
          grid-jitter 0.8s steps(6, end) infinite,
          grid-slow-spike-color var(--grid-cycle) linear infinite;
    }

    .futuristic-bg::after {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
    }

    .futuristic-bg::after {
        background:
            repeating-linear-gradient(
                90deg,
                transparent 0px,
                transparent 180px,
                rgba(255,0,0,0.05) 180px,
                rgba(255,0,0,0.05) 181px
            ),
            repeating-linear-gradient(
                0deg,
                transparent 0px,
                transparent 12px,
                rgba(255,0,0,0.03) 12px,
                rgba(255,0,0,0.03) 13px
            );
        animation: none;
        opacity: .22;
        mix-blend-mode: lighten;
    }

    .futuristic-bg > * {
        position: relative;
        z-index: 1;
    }

    /* --- Animaciones --- */

    @keyframes grid-jitter {
        0%   { background-position: 0 0, 0 0; }
        20%  { background-position: -1px 0, 0 -1px; }
        40%  { background-position: 0 0, 0 0; }
        60%  { background-position: 1px 0, 0 1px; }
        80%  { background-position: 0 0, 0 0; }
        100% { background-position: -1px -1px, 1px 1px; }
    }

    /* Transición lenta -> pico rápido ~86% y caída breve; ciclo var(--grid-cycle) */
    @keyframes grid-slow-spike-color {
        0% {
            --grid-c1: rgba(255, 0, 0, 0.12);
            --grid-c2: rgba(255, 0, 0, 0.08);
        }
        35% {
            --grid-c1: rgba(255, 16, 16, 0.14);
            --grid-c2: rgba(255, 0, 0, 0.10);
        }
        55% {
            --grid-c1: rgba(255, 18, 18, 0.16);
            --grid-c2: rgba(255, 0, 0, 0.12);
        }
        70% {
            --grid-c1: rgba(255, 20, 20, 0.18);
            --grid-c2: rgba(255, 0, 0, 0.14);
        }
        78% {
            --grid-c1: rgba(255, 22, 22, 0.20);
            --grid-c2: rgba(255, 0, 0, 0.15);
        }
        82% {
            --grid-c1: rgba(255, 24, 24, 0.22);
            --grid-c2: rgba(255, 0, 0, 0.16);
        }
        86% {
            --grid-c1: rgba(255, 26, 26, 0.24);
            --grid-c2: rgba(255, 0, 0, 0.17);
        }
        88% {
            --grid-c1: rgba(255, 24, 24, 0.22);
            --grid-c2: rgba(255, 0, 0, 0.16);
        }
        92% {
            --grid-c1: rgba(255, 22, 22, 0.20);
            --grid-c2: rgba(255, 0, 0, 0.14);
        }
        96%,
        100% {
            --grid-c1: rgba(255, 0, 0, 0.12);
            --grid-c2: rgba(255, 0, 0, 0.08);
        }
    }

    #music, #contact, #events { background: transparent !important; }
    .section, .section-bg, .panel-full { background: transparent !important; }

    html { scroll-behavior: smooth; }
    #home, #music, #contact, #events, #soundcloud-sessions, #soundcloud-podcasts { scroll-margin-top: 5rem; }
    @media (max-width: 767px) {
        #home, #music, #contact, #events, #soundcloud-sessions, #soundcloud-podcasts { scroll-margin-top: 4rem; }
    }
    """




# Create the app
# Create the app
app = rx.App(
    _state=State,
    style={
        "font_family": "'Poppins', sans-serif",
        "background_color": "#000000",
        "color": "#ffffff",
    },
    stylesheets=[
        "/styles.css",
    ],
    head_components=[
        # Google Analytics
        rx.script(src=f"https://www.googletagmanager.com/gtag/js?id={GTAG}"),
        rx.script(
            f"""
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{GTAG}');
            """
        ),
    ],
)

# Add the main page
app.add_page(
    index,
    title="10tacle - Electronic Music Producer & DJ",
    description="Official website of 10tacle - Electronic music producer, DJ and radio host",
)