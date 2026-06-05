import reflex as rx

config = rx.Config(
    app_name="Reservas_Frontend",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)