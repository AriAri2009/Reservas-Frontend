import reflex as rx

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(rx.text(text, size="3"), href=href)

def footer_items_1() -> rx.Component:
    return rx.flex(
        rx.heading("Descripciones", size="4", weight="bold", as_="h3",  font_family="Georgia", color="#198375"),
        footer_item("Descripción general", "/#"),
        footer_item("Detalles", "/#"),
        footer_item("itinerario", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
        font_family="Georgia",
        color ="#f1d08d",
    )

def footer_items_2() -> rx.Component:
    return rx.flex(
        rx.heading("Reservas", size="4", weight="bold", as_="h3", font_family="Georgia", color="#198375"),
        footer_item("Datos de contacto", "/#"),
        footer_item("Detalles de la actividad", "/#"),
        footer_item("Descripcion de pago", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
        font_family="Georgia",
        color ="#f1d08d",
        
    )

def social_link(label: str, href: str) -> rx.Component:
    return rx.link(rx.text(label, weight="bold"), href=href)


def socials() -> rx.Component:
    return rx.flex(
        social_link("IG", "/#"),
        social_link("X", "/#"),
        social_link("f", "/#"),
        social_link("in", "/#"),
        spacing="3",
        justify="end",
        width="100%",
        color="#198375",
    )


def footer() -> rx.Component:
    return rx.el.footer(
        rx.vstack(
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.image(
                            src="LogoChillP.png",
                            width="3em",
                            height="auto",
                            border_radius="25%",
                        ),
                    ),
                    rx.text(
                        "© 2026 Chill Plans, Inc",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        font_family="Playfair Display",
                        font_style="italic",
                        color="#198375",
                    ),
                    spacing="4",
                    align_items=["center", "center", "start"],
                ),
                footer_items_1(),
                footer_items_2(),
                justify="between",
                spacing="6",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            rx.divider(),
            rx.hstack(
                rx.hstack(
                    footer_item("Privacy Policy", "/#"),
                    footer_item("Terms of Service", "/#"),
                    spacing="4",
                    align="center",
                    width="100%",
                    font_family="Playfair Display",
                    weight="bold",
                    color="#198375",
                ),
                socials(),
                justify="between",
                width="100%",
            ),
            spacing="5",
            width="100%",
        ),
        bg = "#f5f0e9",
        width="100%",
    )