import reflex as rx
from ..layouts import common_layout


@rx.page(route="/", title="AEWU Project | Index")
def index_page():
    return common_layout(
        rx.vstack(
            rx.heading("Welcome!", size="8"),
            rx.text(
                "It's an interesting project collection created by ",
                rx.code("aewu"),
                " (me). ",
                "My projects is ",
                rx.text.em("open source. "),
                "So, you can do anything.",
                size="4",
                align="center",
                width="50%"
            ),
            align="center"
        )
    )