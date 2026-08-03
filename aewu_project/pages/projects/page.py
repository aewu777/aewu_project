import reflex as rx

from ...layouts import common_layout

from ...config import PROJECT_LINKS

from .data import PROJECTS


def _tabs_list():
    return rx.tabs.list(
        [rx.tabs.trigger(cat[0].capitalize(), value=cat[0]) for cat in PROJECTS]
    )

def _tabs_content():
    return [rx.tabs.content(
        rx.grid(
            [rx.card(
                rx.vstack(
                    rx.vstack(
                        rx.heading(proj['name'], size="4", text_transform="uppercase"),
                        rx.text(
                            proj['desc'],
                            size="3",
                            color_scheme="gray",
                            overflow="hidden",
                            text_overflow="ellipsis"
                        ),
                        spacing='2'
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.icon("code", size=16),
                                "Source",
                                variant="surface",
                                width="100%"
                            ),
                            href=f"{PROJECT_LINKS['github']}/tree/master/aewu_project/pages/projects/{cat[0]}/{proj['src']}",
                            is_external=True,
                            flex="1"
                        ),
                        rx.link(
                            rx.button(
                                rx.icon("arrow_big_right", size=16),
                                "Check",
                                width="100%"
                            ),
                            href=f"{cat[0]}/{proj['href']}",
                            flex="1"
                        ),
                        width="100%"
                    ),
                    spacing='4'
                ),
                size="2"
            ) for proj in cat[1]],
            columns="4",
            spacing="4",
            margin_top="var(--space-4)"
        ),
        value=cat[0]
    ) for cat in PROJECTS]

@rx.page("/projects", "AEWU Project | Projects")
def projects_page():
    return common_layout(
        rx.tabs.root(
            _tabs_list(),
            _tabs_content(),
            default_value=PROJECTS[0][0]
        ),
        align="start"
    )