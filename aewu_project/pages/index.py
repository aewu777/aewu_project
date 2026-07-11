import reflex as rx

from ..layouts import common_layout


@rx.page(route="/", title="AEWU Project | Index")
def index_page():
    return common_layout(
        rx.vstack(
            rx.heading("Welcome!", size="8"),
            rx.text(
                "It's an interesting project collection created by aewu (me). " \
                "My projects are ",
                rx.text.em("open source"),
                " — so, you can do anything.",
                size="4",
                align="center",
                width="50%",
            ),
            align="center"
        ),
        align="center"
    )