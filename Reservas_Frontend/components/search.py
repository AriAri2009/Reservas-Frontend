import reflex as rx

def form_field(label: str, placeholder: str, type: str, name: str) -> rx.Component:
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
            name=name,
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
    return rx.box(                          # rx.box en vez de rx.card para control total
        rx.flex(
            # --- SECCIÓN IZQUIERDA: formulario ---
            rx.vstack(
                rx.heading(
                    "Busca tu Viaje",
                    size="6",
                    weight="bold",
                    color="#2D3748",
                    font_family="Playfair Display",
                    margin_bottom="6",
                    margin_top="2",
                ),
                rx.form.root(
                    rx.vstack(
                        rx.flex(
                            form_field(
                                "Destino",
                                "Ej. Samaná, Saona, Las Terrenas...",
                                "text",
                                "destino",
                            ),
                            form_field(
                                "Fecha de viaje",
                                "",
                                "date",
                                "fecha_viaje",
                            ),
                            spacing="4",
                            direction="column",
                            width="100%",
                            margin_bottom="4",
                        ),
                        rx.form.submit(
                            rx.button(
                                rx.icon("search", size=18),
                                "Buscar Planes",
                                bg="#198375",
                                color="white",
                                _hover={"bg": "#0D3D37"},
                                size="3",
                                cursor="pointer",
                                border_radius="10px",
                                width="100%",
                                padding_y="1.5em",
                            ),
                            as_child=True,
                            width="100%",
                        ),
                    ),
                    on_submit=rx.redirect("/descripcion"),
                    reset_on_submit=False,
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
 
            # --- SECCIÓN DERECHA: imagen ---
            rx.image(
                src="/Palmera.jpg",
                display=["none", "none", "block"],  # oculta en móvil
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
 