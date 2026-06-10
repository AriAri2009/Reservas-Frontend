import reflex as rx
from Reservas_Frontend.state import HomeState


def cards(
    imagen_url: str,
    titulo_destino: str,
    precio_destino: int,
    descripcion_corta: str,
    destino_id: int,
) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=imagen_url,
            width="100%",
            height="200px",
            object_fit="cover",
            border_radius="10px",
        ),
        rx.vstack(
            rx.heading(
                titulo_destino,
                size="3",
                weight="bold",
                font_family="Playfair Display",
                color="#198375",
                margin_bottom="2",
                padding="20px",
            ),
            rx.text(
                descripcion_corta,
                size="2",
                color="#718096",
                line_height="1.4",
                padding="20px",
            ),
            # Precio formateado como RD$ 4,500
            rx.text(
                rx.el.span("Desde "),
                rx.el.span(
                    rx.el.span("RD$ "),
                    rx.el.span(precio_destino),
                ),
                size="3",
                weight="bold",
                color="#2D3748",
                margin_top="2",
                padding="20px",
            ),
            # Botón que guarda el destino en State antes de navegar
            rx.button(
                "Ver Detalles →",
                on_click=HomeState.seleccionar_destino(destino_id),
                size="2",
                bg="#f68f42",
                color="white",
                width="100%",
                cursor="pointer",
                box_shadow="0 4px 14px rgba(230,169,80,0.35)",
                _hover={"bg": "#f3a56a"},
            ),
            align_items="start",
            spacing="2",
            width="100%",
            padding_x="5",
            padding_bottom="5",
            padding_top="2",
        ),
        border="1px solid #E2E8F0",
        border_radius="xl",
        overflow="hidden",
        bg="#f5f5f5",
        box_shadow="md",
        width="100%",
        max_width="340px",
        transition="transform 0.2s ease, box_shadow 0.2s ease",
        _hover={
            "transform": "translateY(-4px)",
            "box_shadow": "lg",
        },
    )