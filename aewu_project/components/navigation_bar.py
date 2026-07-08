import reflex as rx


def navigation_bar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.heading("AEWU Project"),
            rx.hstack(
                rx.link(
                    rx.button(
                        rx.icon("home", size=16),
                        "Index",
                        variant="surface"
                    ),
                    href="/"
                ),
                rx.link(
                    rx.button(
                        rx.icon("folders", size=16),
                        "Projects",
                        variant="surface"
                    ),
                    href="/projects"
                )
            ),
            spacing="6"
        ),
        rx.color_mode.button(),
        justify="between"
    )