# hero.py
import reflex as rx

def hero_text() -> rx.Component:
    lines = [
        "The purest TECHNO throbs, strong and sensitive is incorruptible, brave and unique.",
        "The purest TECHNO reject the obscene and detect perversion.",
        "The purest TECHNO don't fake love nor feign freedom.",
        "TECHNO is you and me."
    ]
    spans = []
    for i, line in enumerate(lines):
        spans.append(
            rx.text(
                line,
                class_name="stanza",
                font_size={"base": "0.75rem", "sm": "0.875rem", "md": "1rem"},
                style={"animation_delay": f"{i * 1.5}s"}
            )
        )
    return rx.box(
        *spans,
        class_name="text-gray-300 mb-8 sm:mb-12 text-center leading-relaxed",
        max_width={"base": "95%", "sm": "80%", "md": "640px"},
        margin_x="auto"
    )

def hero() -> rx.Component:
    social_buttons_data = [
        {"name": "Beatport",     "icon": "TBG-PrimaryIcon-White.svg",     "href": "https://www.beatport.com/es/artist/10tacle/1121502"},
        {"name": "Spotify",      "icon": "spotify-white-icon.svg",         "href": "https://open.spotify.com/intl-es/artist/4ycl0vQK5aynXLJeRFpanC"},
        {"name": "SoundCloud",   "icon": "soundcloud-white-icon.svg",      "href": "https://soundcloud.com/10tacle"},
        {"name": "Twitch",       "icon": "twitch-white-icon.svg",          "href": "https://www.twitch.tv/v1ct0rdev"},
    ]

    button_components = []
    for btn in social_buttons_data:
        svg_url = rx.asset(btn["icon"])
        # Explicitly set width and height for the icons within buttons
        icon = rx.image(src=svg_url, width="18px", height="18px", class_name="mr-2", alt=f"{btn['name']} icon")
        btn_comp = rx.button(
            rx.hstack(icon, rx.text(btn["name"]), spacing="2", align="center"),
            variant="outline",
            class_name=(
                "border-gray-600 text-gray-300 "
                "hover:bg-red-500 hover:text-white hover:border-red-500 "
                "font-semibold tracking-wider transition-colors duration-300 "
                # Adjusted padding and text size for better responsiveness
                "px-4 py-2 text-sm sm:px-5 sm:py-2.5"
            )
        )
        button_components.append(rx.link(btn_comp, href=btn["href"], is_external=True))

    return rx.box(
        rx.box(class_name="absolute inset-0 bg-black"),
        rx.box(class_name="absolute inset-0 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-red-900/25 via-transparent to-transparent opacity-50"),
        rx.container(
            rx.flex(
                rx.image(
                    src="/logo_header.png",
                    alt="10TACLE Logo",
                    # Reverted to simpler max_width, ensure w-full allows it to scale down
                    class_name="h-auto w-full max-w-xs sm:max-w-sm md:max-w-md lg:max-w-lg mx-auto mb-6",
                ),
                rx.text(
                    "Electronic Music Producer & DJ",
                    font_size={"base": "0.8rem", "sm": "1rem", "md": "1.25rem"},
                    class_name="font-orbitron text-gray-400 tracking-widest uppercase mb-6 sm:mb-8 text-center",
                    as_="div"
                ),
                hero_text(),
                rx.flex(
                    *button_components,
                    spacing={"base": "3", "sm": "4"}, # Adjusted spacing
                    justify="center",
                    wrap="wrap",
                    class_name="mt-4 sm:mt-6"
                ),
                direction="column",
                align="center",
                class_name="text-center"
            ),
            class_name="relative z-10 max-w-5xl mx-auto px-3 sm:px-4"
        ),
        id="home",
        class_name="relative min-h-screen flex items-center justify-center overflow-hidden pt-24 pb-12 md:pt-20"
    )
