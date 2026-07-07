from typing import Literal

import reflex as rx

from ..components import navigation_bar
from ..components import footer


def common_layout(
    *children,
    align:  Literal['start', 'center', 'end'],
    **props
) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.container(
                navigation_bar(),
                size="4",
                width="100%",
                flex="0"
            ),
            rx.flex(
                rx.container(
                    *children,
                    size="4",
                    **props
                ),
                width="100%",
                flex="1",
                align=align
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