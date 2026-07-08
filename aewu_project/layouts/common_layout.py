from typing import Literal

import reflex as rx

from ..components import navigation_bar
from ..components import footer


def common_layout(
    *children,
    align:  Literal['start', 'center', 'end'],
    content_size: Literal['1', '2', '3', '4'] = "4",
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
                    size=content_size,
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