"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from Reservas_Frontend.components.navbar import navbar_buttons
from Reservas_Frontend.components.footer import footer


class State(rx.State):
    """The app state."""


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            navbar_buttons(),
            footer()
        ),
        width="100%",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap",
    ],
)
app.add_page(index)
