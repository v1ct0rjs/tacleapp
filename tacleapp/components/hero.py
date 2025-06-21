import reflex as rx

def hero() -> rx.Component:
    social_buttons_data = [
        {
            "name": "Beatport",
            "icon": "TBG-PrimaryIcon-White.svg",  # Archivo SVG dentro de assets/
            "href": "https://www.beatport.com/es/artist/10tacle/1121502"
        },
        {
            "name": "Spotify",
            "icon": "spotify-white-icon.svg",
            "href": "https://open.spotify.com/intl-es/artist/4ycl0vQK5aynXLJeRFpanC?si=gWmoNpdsR4aM7gLOVCgF9Q"
        },
        {
            "name": "SoundCloud",
            "icon": "soundcloud-white-icon.svg",
            "href": "https://soundcloud.com/10tacle"
        },
        {
            "name": "Twitch",
            "icon": "twitch-white-icon.svg",
            "href": "https://www.twitch.tv/v1ct0rdev"
        },
    ]

    button_components = []
    for btn in social_buttons_data:
        name = btn["name"]
        href = btn["href"]
        icon_src = btn["icon"]

        # Detecta si es un SVG personalizado o un icono del paquete
        if icon_src.lower().endswith(".svg"):
            # Esta línea obtiene la URL correcta del asset
            svg_url = rx.asset(icon_src)
            icon_component = rx.image(
                src=svg_url,
                height="18px",
                width="auto",
                class_name="mr-2",
                alt=f"{name} icon"
            )
        else:
            icon_component = rx.icon(
                tag=icon_src,
                size=18,
                class_name="mr-2"
            )

        btn_comp = rx.button(
            rx.hstack(
                icon_component,
                rx.text(name),
                spacing="2",
                align="center"
            ),
            variant="outline",
            size="2",
            class_name=(
                "border-gray-600 text-gray-300 "
                "hover:bg-red-500 hover:text-white hover:border-red-500 "
                "font-semibold tracking-wider transition-colors duration-300 "
                "px-6 py-5"
            )
        )

        button_components.append(
            rx.link(btn_comp, href=href, is_external=True)
        )

    return rx.box(
        rx.box(class_name="absolute inset-0 bg-black"),
        rx.box(class_name="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-red-900/25 via-transparent to-transparent opacity-50"),
        rx.container(
            rx.flex(
                rx.image(src="/logo_header.png", alt="10TACLE Logo", class_name="h-auto w-full max-w-md sm:max-w-lg md:max-w-xl mx-auto mb-6"),
                rx.text("Electronic Music Producer & DJ", size="5", class_name="font-orbitron text-gray-400 tracking-widest uppercase mb-8 text-center", as_="div"),
                rx.text(
                    "The purest TECHNO throbs,\n"
                    "strong and sensitive is incorruptible,\n"
                    "brave and unique.\n"
                    "The purest TECHNO reject the obscene and detect perversion.\n"
                    "The purest TECHNO don't fake love nor feign freedom.\n"
                    "TECHNO is you and me.",
                    size="3",
                    class_name="text-gray-300 mb-12 max-w-2xl text-center leading-relaxed",
                    style={"white_space": "pre-wrap"},
                    as_="div"
                ),
                rx.flex(
                    *button_components,
                    spacing="4",
                    justify="center",
                    wrap="wrap",
                    class_name="mt-8"
                ),
                direction="column",
                align="center",
                class_name="text-center"
            ),
            class_name="relative z-10 max-w-4xl mx-auto px-4"
        ),
        id="home",
        class_name="relative min-h-screen flex items-center justify-center overflow-hidden pt-20"
    )
