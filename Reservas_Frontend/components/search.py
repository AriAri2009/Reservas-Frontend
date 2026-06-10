import reflex as rx
from Reservas_Frontend.state import HomeState


def form_field(label: str, placeholder: str, type: str, on_change) -> rx.Component:
    return rx.vstack(
        rx.text(
            label,
            size="2",
            weight="medium",
            color="#4a5568",
            font_family="Inter",
            margin_bottom="2",
        ),
        rx.input(
            placeholder=placeholder,
            type=type,
            on_change=on_change,
            bg="#f5f5f5",
            border_color="#e2e8f0",
            border_radius="12px",
            padding_y="1.5em",
            width="100%",
            margin_top="1",
        ),
        spacing="1",
        width="100%",
    )


def search_form() -> rx.Component:
    return rx.box(
        rx.flex(
            # ── SECCIÓN IZQUIERDA: formulario ──
            rx.vstack(
                rx.heading(
                    "Busca tu Viaje",
                    size="6",
                    weight="bold",
                    color="#2D3748",
                    font_family="Playfair Display",
                    margin_bottom="6",
                    margin_top="2",
                    padding="20px",
                    align="center",
                ),
                rx.vstack(
                    rx.flex(
                        # Campo nombre — filtra en tiempo real
                        form_field(
                            "Destino",
                            "Ej. Samaná, Saona, Las Terrenas...",
                            "text",
                            HomeState.set_busqueda_nombre,
                        ),
                        # Campo fecha — valida al buscar
                        form_field(
                            "Fecha de viaje",
                            "",
                            "date",
                            HomeState.set_busqueda_fecha,
                        ),
                        spacing="4",
                        direction="column",
                        width="100%",
                        margin_bottom="4",
                        padding="20px",
                    ),
                    # Mensaje de error debajo de los campos
                    rx.cond(
                        HomeState.error_busqueda != "",
                        rx.box(
                            rx.hstack(
                                rx.icon("circle-alert", size=14, color="#C0392B"),
                                rx.text(
                                    HomeState.error_busqueda,
                                    size="2",
                                    color="#C0392B",
                                    font_family="Inter",
                                ),
                                spacing="2",
                                align="center",
                            ),
                            bg="#FEF0EE",
                            border="1px solid #F5C6C0",
                            border_radius="8px",
                            padding="10px 14px",
                            margin_x="20px",
                            margin_bottom="8px",
                        ),
                        rx.box(),  # vacío si no hay error
                    ),
                    # Botón buscar
                    rx.box(
                        rx.button(
                            rx.icon("search", size=18),
                            "Buscar Planes",
                            on_click=HomeState.buscar,
                            bg="#198375",
                            color="white",
                            _hover={"bg": "#0D3D37"},
                            size="3",
                            cursor="pointer",
                            border_radius="10px",
                            width="100%",
                            padding="20px",
                        ),
                        width="100%",
                        padding_x="20px",
                        padding_bottom="20px",
                    ),
                    width="100%",
                ),
                align_items="start",
                justify="center",
                flex="1.2",
                bg="#ffffff",
                border_radius="15px",
                padding_x=["5", "6", "8"],
                padding_y="8",
                width="100%",
            ),

            # ── SECCIÓN DERECHA: imagen ──
            rx.image(
                src="/Palmera.jpg",
                display=["none", "none", "block"],
                border_radius="0 15px 15px 0",
                width="40%",
                height="100%",
                object_fit="cover",
                flex_shrink="0",
            ),

            direction="row",
            width="100%",
            align_items="stretch",
        ),
        bg="#f8f9fa",
        padding="4",
        border_radius="15px",
        box_shadow="0px 15px 35px rgba(0,0,0,0.06)",
        width="90%",
        max_width="850px",
        overflow="hidden",
        border="1px solid #e2e8f0",
    )