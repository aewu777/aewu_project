import reflex as rx


def navigation_bar() -> rx.Component:
    return rx.hstack(
        rx.heading("AEWU Project"),
        rx.color_mode.button(),
        justify="between"
    )