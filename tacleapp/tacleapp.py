import reflex as rx
from .state import State
from .components import navigation, hero, music, events, contact

GTAG = "G-MBP9JLGSZ5"

def index() -> rx.Component:
    """Main page component with simplified futuristic background effects."""
    return rx.box(
        # Main content with background effects
        #navigation(),
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
        /* Fondo base (grid) atado al viewport para que abarque toda la página */
        background:
            linear-gradient(rgba(255,255,255,0.12) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.12) 1px, transparent 1px);
        background-size: 40px 40px, 40px 40px;
        background-attachment: fixed, fixed;
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

    /* --- Scan lines ROJAS --- */
    .futuristic-bg::before {
        /* banda fina roja que "escanea" verticalmente */
        background: linear-gradient(
            transparent 98%,
            rgba(255, 0, 0, 0.35) 99%,
            transparent 100%
        );
        background-size: 100% 100px;
        animation: scan-line 6s linear infinite;
        opacity: .9;
        mix-blend-mode: screen; /* hace que la línea roja brille sobre el fondo oscuro */
    }

    /* --- Glitch overlay (sin puntos girando) --- */
    .futuristic-bg::after {
        /* ruido fino + columnas muy sutiles + bandas horizontales que se desplazan a saltos */
        background:
            /* ruido fino horizontal */
            repeating-linear-gradient(
                0deg,
                rgba(255,255,255,0.03) 0px,
                rgba(255,255,255,0.03) 2px,
                transparent 2px,
                transparent 4px
            ),
            /* columnas verticales muy suaves con un toque rojo */
            repeating-linear-gradient(
                90deg,
                transparent 0px,
                transparent 180px,
                rgba(255,0,0,0.05) 180px,
                rgba(255,0,0,0.05) 181px
            ),
            /* bandas horizontales intermitentes (glitch) */
            repeating-linear-gradient(
                0deg,
                transparent 0px,
                transparent 12px,
                rgba(255,255,255,0.04) 12px,
                rgba(255,255,255,0.04) 13px
            );
        animation:
            glitch-shift 2.2s steps(12) infinite,
            glitch-flash 6s steps(20) infinite;
        opacity: .55;
        mix-blend-mode: lighten;
    }

    /* El contenido siempre por encima de los overlays */
    .futuristic-bg > * {
        position: relative;
        z-index: 1;
    }

    /* Animación: scan line baja en bucle */
    @keyframes scan-line {
        0%   { transform: translateY(0); }
        100% { transform: translateY(100px); }
    }

    /* Animación: pequeños "saltos" tipo glitch */
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

    /* Pequeños destellos/contraste para reforzar el efecto glitch */
    @keyframes glitch-flash {
        0%, 45%, 55%, 100% { filter: none; }
        46% { filter: brightness(1.05) contrast(1.15) saturate(1.05); }
        54% { filter: brightness(1.1) contrast(1.2) saturate(1.1); }
    }
    /* Forzar transparencia de los contenedores de sección más comunes */
    #music, #contact, #events {
        background: transparent !important;
    }

    /* Si usas wrappers con clases personalizadas, añádelas aquí */
    .section, .section-bg, .panel-full {
        background: transparent !important;
    }
    /* Scroll suave al pinchar en #ancla */
    html { scroll-behavior: smooth; }

    /* La cabecera mide h-16 md:h-20 => 4rem/5rem */
    #home, #music, #contact, #events {
        scroll-margin-top: 5rem;      /* 80px para desktop */
    }
    @media (max-width: 767px) {
        #home, #music, #contact, #events {
            scroll-margin-top: 4rem;  /* 64px para móvil */
        }
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
        rx.html('<link rel="stylesheet" href="/styles.css">'),
        rx.html(f"<style>{get_custom_css()}</style>"),
    ],
)

# Add the main page
app.add_page(
    index,
    title="10tacle - Electronic Music Producer & DJ",
    description="Official website of 10tacle - Electronic music producer, DJ and radio host"
)
