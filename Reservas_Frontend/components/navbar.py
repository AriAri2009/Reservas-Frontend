import reflex as rx

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(rx.text(text, size="4", weight="medium"), href=url, font_family="Playfair Display", color="#198375", _hover={"color": "#0D3D37"})


def navbar_buttons() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/LogoChill1.png",
                        width="auto",
                        height="3em",
                        border_radius="25%",
                    ),

                ),
                rx.hstack(
                    navbar_link("Inicio", "/#"),
                    navbar_link("Descripciones", "/#"),
                    navbar_link("Reservas", "/#"),
                    navbar_link("Contacto", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button("Log in", size="3", variant="outline", bg = "#e6a950", color = "#ffffff", border_radius="15px"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/LogoChill1.png",
                        width="auto",
                        height="2.25em",
                        border_radius="25%",
                    ),
                    rx.heading("Reflex", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30, color = "white")),
                    rx.menu.content(
                        rx.menu.item("Inicio"),
                        rx.menu.item("Descripciones"),
                        rx.menu.item("Reservas"),
                        rx.menu.item("Contacto"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg= "#f5f0e9",
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )