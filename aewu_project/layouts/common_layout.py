import reflex as rx
from ..components.navigation_bar import navigation_bar
from ..components.footer import footer


def common_layout(*children, **props) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.container(
                navigation_bar(),
                size="4",
                width="100%",
                flex="0"
            ),
            rx.center(
                rx.container(
                    *children,
                    size="4",
                    **props
                ),
                width="100%",
                flex="1"
            ),
            rx.container(
                footer(),
                size="4",
                width="100%",
                flex="0"
            ),
            height="100%"
        ),
        height="100vh"
    )