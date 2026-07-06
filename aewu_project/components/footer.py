import reflex as rx
from ..config import project_links


def footer() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.text("2026"),
            rx.icon("copyright", size=16),
            rx.text("by aewu with love."),
            align="center"
        ),
        rx.hstack(
            rx.link("GitHub", href=project_links["github"])
        ),
        justify="between"
    )