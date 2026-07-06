import reflex as rx

config = rx.Config(
    app_name="aewu_project",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)