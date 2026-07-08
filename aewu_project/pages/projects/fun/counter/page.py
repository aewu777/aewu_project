import reflex as rx

from .....layouts import common_layout

from .state import CounterState


@rx.page("/projects/fun/counter", "AEWU Project | Counter")
def counter_page():
    return common_layout(
        rx.vstack(
            rx.heading(CounterState.count, size="9"),
            rx.hstack(
                rx.button(
                    "Decrement",
                    color_scheme="tomato",
                    on_click=CounterState.decrement,
                    flex="1"
                ),
                rx.button(
                    "Increment",
                    color_scheme="grass",
                    on_click=CounterState.increment,
                    flex="1"
                ),
                width="100%"
            ),
            rx.button(
                "Reset",
                on_click=CounterState.reset_count,
                width="100%"
            ),
            align="center"
        ),
        align="center",
        content_size="1"
    )