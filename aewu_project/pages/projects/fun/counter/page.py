import reflex as rx

from .....layouts import common_layout

from .state import CounterState


@rx.page("/projects/fun/counter", "AEWU Project | Counter")
def counter_page():
    return common_layout(
        rx.vstack(
            rx.heading(CounterState.count, size="9"),
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.input(
                            value=CounterState.decrement_step,
                            placeholder="Any integer you want...",
                            on_change=CounterState.set_decrement_step,
                            flex="1"
                        ),
                        rx.input(
                            value=CounterState.increment_step,
                            placeholder="Any integer you want...",
                            on_change=CounterState.set_increment_step,
                            flex="1"
                        ),
                        width="100%"
                    ),
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
                    flex="1"
                ),
                rx.vstack(
                    rx.hstack(
                        rx.button(
                            "Double",
                            color_scheme="bronze",
                            on_click=CounterState.set_count(CounterState.count * 2),
                            flex="1"
                        ),
                        rx.button(
                            "Triple",
                            color_scheme="bronze",
                            on_click=CounterState.set_count(CounterState.count * 3),
                            flex="1"
                        ),
                        width="100%"
                    ),
                    rx.hstack(
                        rx.button(
                            "Halve",
                            color_scheme="bronze",
                            on_click=CounterState.set_count(CounterState.count / 2),
                            flex="1"
                        ),
                        rx.button(
                            "Third",
                            color_scheme="bronze",
                            on_click=CounterState.set_count(CounterState.count / 3),
                            flex="1"
                        ),
                        width="100%"
                    ),
                    rx.hstack(
                        rx.button(
                            "Square",
                            color_scheme="bronze",
                            on_click=CounterState.set_count(CounterState.count ** 2),
                            flex="1"
                        ),
                        rx.button(
                            "Sqrt",
                            color_scheme="bronze",
                            on_click=CounterState.set_count(CounterState.count ** 0.5),
                            flex="1"
                        ),
                        width="100%"
                    ),
                    flex="1"
                ),
                width="100%"
            ),
            align="center"
        ),
        align="center",
        content_size="1"
    )