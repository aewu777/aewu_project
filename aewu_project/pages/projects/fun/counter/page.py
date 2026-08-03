import reflex as rx

from .....layouts import common_layout

from .state import CounterState

from .data import OPERATIONS


def _operations_section() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Operations",
            size="1",
            weight="bold",
            color_scheme="gray",
            text_transform="uppercase"
        ),
        rx.grid(
            [rx.button(
                label,
                variant="surface",
                on_click=event,
                height="40px",
                width="100%"
            ) for label, event in OPERATIONS],
            columns="3",
            spacing="2",
            width="100%"
        ),
        width="100%",
        spacing='2'
    )

@rx.page("/projects/fun/counter", "AEWU Project | Counter")
def counter_page():
    return common_layout(
        rx.vstack(
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            CounterState.count,
                            size="9",
                            weight="bold"
                        ),
                        justify="center",
                        width="100%"
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text(
                                "Decrement Step",
                                size="2",
                                weight="medium",
                                color_scheme="gray"
                            ),
                            rx.input(
                                type="number",
                                value=CounterState.decrement_step,
                                on_change=CounterState.set_decrement_step,
                                size="2",
                                height="40px",
                                width="100%"
                            ),
                            rx.button(
                                rx.icon("minus", size=16),
                                "Decrement",
                                variant="soft",
                                color_scheme="gray",
                                on_click=CounterState.decrement,
                                height="40px",
                                width="100%"
                            ),
                            width="100%",
                            spacing='2'
                        ),
                        rx.vstack(
                            rx.text(
                                "Increment Step",
                                size="2",
                                weight="medium",
                                color_scheme="gray"
                            ),
                            rx.input(
                                type="number",
                                value=CounterState.increment_step,
                                on_change=CounterState.set_increment_step,
                                size="2",
                                height="40px",
                                width="100%"
                            ),
                            rx.button(
                                rx.icon("plus", size=16),
                                "Increment",
                                color_scheme='violet',
                                on_click=CounterState.increment,
                                height="40px",
                                width="100%"
                            ),
                            width="100%",
                            spacing='2'                            
                        ),
                        width="100%",
                        spacing='2'
                    ),
                    _operations_section(),
                    rx.separator(),
                    rx.button(
                        rx.icon("rotate-ccw", size=16),
                        "Reset",
                        variant="soft",
                        color_scheme="tomato",
                        on_click=CounterState.reset_count,
                        height="40px",
                        width="100%"
                    ),
                    spacing="4",
                ),
                size="2",
                width="100%"
            ),
            align='center'
        ),
        align='center',
        content_size="1"
    )