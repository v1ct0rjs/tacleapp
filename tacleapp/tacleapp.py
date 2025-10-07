import reflex as rx
from .state import State
from .components import navigation, hero, music, events, contact

GTAG = "G-MBP9JLGSZ5"

def index() -> rx.Component:
    """Main page component with futuristic background effects."""
    return rx.box(
        #navigation(),
        rx.box(hero(), as_="section", class_name="section-tight"),
        rx.box(music(), as_="section", class_name="section-tight"),
        rx.box(contact(), as_="section", class_name="section-tight"),
        class_name="futuristic-bg",
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
      initial-value: rgba(255, 255, 255, 0.08);
    }

    :root {
      --grid-size: 128px;
      --grid-cycle: 25s; /* intervalo entre transiciones (antes 6s) */
      --grid-c1: rgba(255, 0, 0, 0.12);
      --grid-c2: rgba(255, 255, 255, 0.08);
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

    .futuristic-bg::before,
    .futuristic-bg::after {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
    }

    .futuristic-bg::before {
        background: linear-gradient(
            transparent 98%,
            rgba(255, 0, 0, 0.35) 99%,
            transparent 100%
        );
        background-size: 100% 100px;
        animation: scan-line 1.2s steps(48, end) infinite;
        opacity: .9;
        mix-blend-mode: screen;
    }

    .futuristic-bg::after {
        background:
            repeating-linear-gradient(
                0deg,
                rgba(255,255,255,0.03) 0px,
                rgba(255,255,255,0.03) 2px,
                transparent 2px,
                transparent 4px
            ),
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
                rgba(255,255,255,0.04) 12px,
                rgba(255,255,255,0.04) 13px
            );
        animation:
            glitch-shift 1.1s steps(18, end) infinite,
            strobe-electric 1.6s steps(30, end) infinite;
        opacity: .55;
        mix-blend-mode: lighten;
    }

    .futuristic-bg > * {
        position: relative;
        z-index: 1;
    }

    /* --- Animaciones --- */
    @keyframes scan-line {
        0%   { transform: translateY(0); }
        100% { transform: translateY(100px); }
    }

    @keyframes glitch-shift {
        0%   { transform: translate(0, 0); }
        8%   { transform: translate(-2px, 1px); }
        16%  { transform: translate(3px, -1px); }
        24%  { transform: translate(-1px, 0); }
        32%  { transform: translate(2px, 0.5px); }
        40%  { transform: translate(0, 0); }
        55%  { transform: translate(1px, -0.5px); }
        70%  { transform: translate(-1px, 0.5px); }
        85%  { transform: translate(2px, -1px); }
        100% { transform: translate(0, 0); }
    }

    @keyframes strobe-electric {
        0%, 100% { filter: none; opacity: .45; }
        8%, 23%, 37%, 51%, 66%, 81%, 93% {
            filter: none; opacity: .45;
        }
        9%, 24%, 38%, 52%, 67%, 82%, 94% {
            filter: brightness(1.65) contrast(1.35) saturate(1.05);
            opacity: .9;
        }
    }

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
            --grid-c2: rgba(255, 255, 255, 0.08);
        }
        35% {
            --grid-c1: rgba(255, 20, 20, 0.14);
            --grid-c2: rgba(255, 0, 0, 0.10);
        }
        55% {
            --grid-c1: rgba(255, 24, 24, 0.18);
            --grid-c2: rgba(255, 0, 0, 0.14);
        }
        70% {
            --grid-c1: rgba(255, 28, 28, 0.22);
            --grid-c2: rgba(255, 0, 0, 0.18);
        }
        78% {
            --grid-c1: rgba(255, 30, 30, 0.28);
            --grid-c2: rgba(255, 0, 0, 0.22);
        }
        82% {
            --grid-c1: rgba(255, 34, 34, 0.38);
            --grid-c2: rgba(255, 0, 0, 0.28);
        }
        86% {
            --grid-c1: rgba(255, 40, 40, 0.88); /* pico rápido */
            --grid-c2: rgba(255, 0, 0, 0.46);
        }
        88% {
            --grid-c1: rgba(255, 36, 36, 0.52); /* salida rápida */
            --grid-c2: rgba(255, 0, 0, 0.30);
        }
        92% {
            --grid-c1: rgba(255, 30, 30, 0.28);
            --grid-c2: rgba(255, 0, 0, 0.20);
        }
        96%,
        100% {
            --grid-c1: rgba(255, 0, 0, 0.12);
            --grid-c2: rgba(255, 255, 255, 0.08);
        }
    }

    #music, #contact, #events { background: transparent !important; }
    .section, .section-bg, .panel-full { background: transparent !important; }

    html { scroll-behavior: smooth; }
    #home, #music, #contact, #events { scroll-margin-top: 5rem; }
    @media (max-width: 767px) {
        #home, #music, #contact, #events { scroll-margin-top: 4rem; }
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
            """
        ),
        rx.html(
            '<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">'
        ),
        rx.html('<link rel="stylesheet" href="/styles.css">'),
        # Importante: inline CSS al final para que no lo pise /styles.css
        rx.html(f"<style>{get_custom_css()}</style>"),
    ],
)

# Add the main page
app.add_page(
    index,
    title="10tacle - Electronic Music Producer & DJ",
    description="Official website of 10tacle - Electronic music producer, DJ and radio host",
)
