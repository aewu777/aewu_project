import reflex as rx

from ..config import PROJECT_LINKS


def footer() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text("2026"),
            rx.icon("copyright", size=16),
            rx.text("by aewu with love."),
            align="center"
        ),
        rx.hstack(
            rx.link("GitHub", href=PROJECT_LINKS['github'])
        ),
        justify="between"
    )