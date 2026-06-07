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
                    navbar_link("Inicio", "/"),
                    navbar_link("Descripciones", "/descripcion"),
                    navbar_link("Reservas", "/reservas"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.link(
                        rx.button(
                            "Log in", 
                            size="3", 
                            variant="outline", 
                            bg="#e6a950", 
                            color="#ffffff", 
                            border_radius="15px"
                        ),
                        href="/admin_login"
                    ),
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
                    rx.menu.trigger(rx.icon("menu", size=30, color="white")),
                    rx.menu.content(
                        rx.menu.item("Inicio", on_click=rx.redirect("/")),
                        rx.menu.item("Descripciones", on_click=rx.redirect("/descripcion")),
                        rx.menu.item("Reservas", on_click=rx.redirect("/reservas")),
                        rx.menu.separator(),
                        rx.menu.item("Log in", on_click=rx.redirect("/admin_login")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg="#f5f0e9",
        padding="1em",
        width="100%",
    )