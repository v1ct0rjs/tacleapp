import reflex as rx

def navigation() -> rx.Component:
    links = [("Home", "#home"), ("Music", "#music"), ("Contact", "#contact")]

    return rx.box(
        rx.box(  # rail fijo y transparente
            rx.vstack(
                *[
                    rx.link(
                        label,
                        href=href,
                        class_name="left-ghost-link"
                    )
                    for (label, href) in links
                ],
                class_name="left-ghost-col"
            ),
            class_name="left-ghost-nav"
        ),
        as_="nav",
        role="navigation"
    )

