# descripcion.py
# Vive en: Reservas_Frontend/pages/descripcion.py

import reflex as rx
from Reservas_Frontend.components.navbar import navbar_buttons
from Reservas_Frontend.components.footer import footer
from Reservas_Frontend.mock_data import OFERTAS_MOCK
 
 
class DescripcionState(rx.State):
    destino: dict = OFERTAS_MOCK[0]
    itinerario: list[str] = OFERTAS_MOCK[0]["itinerario"]
    incluye: list[str] = OFERTAS_MOCK[0]["incluye"]
    no_incluye: list[str] = OFERTAS_MOCK[0]["no_incluye"]
 
    def cargar_destino(self, id: int = 0):
        if 0 <= id < len(OFERTAS_MOCK):
            self.destino = OFERTAS_MOCK[id]
            self.itinerario = OFERTAS_MOCK[id]["itinerario"]
            self.incluye = OFERTAS_MOCK[id].get("incluye", [])
            self.no_incluye = OFERTAS_MOCK[id].get("no_incluye", [])
 
 
def hero_descripcion() -> rx.Component:
    return rx.box(
        rx.image(
            src=DescripcionState.destino["imagen_url"],
            width="100%",
            height="55vh",
            object_fit="cover",
            position="absolute",
            top="0",
            left="0",
            z_index="0",
        ),
        rx.box(
            width="100%",
            height="55vh",
            position="absolute",
            top="0",
            left="0",
            bg="rgba(0,0,0,0.55)",
            z_index="1",
        ),
        rx.vstack(
            rx.text(
                "Destino destacado",
                size="2",
                color="rgba(255,255,255,0.85)",
                font_family="Playfair Display",
                font_style="italic",
                letter_spacing="2px",
                text_transform="uppercase",
            ),
            rx.heading(
                DescripcionState.destino["nombre"],
                size="8",
                color="white",
                font_family="Playfair Display",
                text_align="center",
                text_shadow="2px 2px 10px rgba(0,0,0,0.7)",
            ),
            rx.hstack(
                rx.badge(DescripcionState.destino["duracion"], color_scheme="orange", size="2"),
                rx.badge(DescripcionState.destino["transporte"], color_scheme="green", size="2"),
                spacing="3",
                justify="center",
                flex_wrap="wrap",
            ),
            spacing="4",
            justify="center",
            align_items="center",
            width="100%",
            position="relative",
            z_index="2",
        ),
        width="100%",
        height="55vh",
        position="relative",
        overflow="hidden",
        display="flex",
        align_items="center",
        justify_content="center",
    )
 
 
def tarjeta_descripcion() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.vstack(
                rx.text(
                    "Descripción del paquete",
                    size="2",
                    weight="bold",
                    color="#e6a950",
                    font_family="Playfair Display",
                    text_transform="uppercase",
                    letter_spacing="1px",
                    padding = "20px",
                ),
                rx.box(width="40px", height="3px", bg="#e6a950", border_radius="2px"),
                rx.text(
                    DescripcionState.destino["descripcion_general"],
                    size="3",
                    color="#4a5568",
                    line_height="1.9",
                    text_align="justify",
                    padding = "20px",
                ),
                align_items="start",
                spacing="3",
                padding="6",
                flex="1",
                justify="center",
            ),
            rx.image(
                src=DescripcionState.destino["imagen_url"],
                width="320px",
                height="100%",
                min_height="280px",
                object_fit="cover",
                flex_shrink="0",
            ),
            direction="row",
            width="100%",
            align_items="stretch",
        ),
        border="1px solid #E2E8F0",
        border_radius="16px",
        overflow="hidden",
        bg="white",
        box_shadow="0 4px 16px rgba(0,0,0,0.07)",
        width="100%",
    )
 
 
def galeria_section() -> rx.Component:
    return rx.grid(
        rx.image(
            src=DescripcionState.destino["imagen_url"],
            width="100%",
            height="180px",
            object_fit="cover",
            border_radius="12px",
            border="1px solid #E2E8F0",
        ),
        rx.image(
            src=DescripcionState.destino["imagen_secundaria"],
            width="100%",
            height="180px",
            object_fit="cover",
            border_radius="12px",
            border="1px solid #E2E8F0",
        ),
        rx.image(
            src=DescripcionState.destino["imagen_url"],
            width="100%",
            height="180px",
            object_fit="cover",
            border_radius="12px",
            border="1px solid #E2E8F0",
            filter="brightness(0.85)",
        ),
        columns="3",
        gap="4",
        width="100%",
    )
 
 
def columna_izquierda() -> rx.Component:
    return rx.vstack(
        tarjeta_descripcion(),
        galeria_section(),
        spacing="4",
        align_items="start",
        width="100%",
        flex="2",
    )
 
 
def fila_resumen(label: str, valor) -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.text(label, size="1", color="#718096", weight="bold",
                    text_transform="uppercase", letter_spacing="0.5px"),
            rx.text(valor, size="2", color="#2D3748", weight="medium"),
            spacing="0",
            align_items="start",
        ),
        align_items="start",
        spacing="3",
        width="100%",
        padding="20px",
        border_bottom="1px solid #f0f0f0",
    )
 
 
def columna_derecha() -> rx.Component:
    return rx.vstack(
        rx.vstack(
            rx.text("Desde", size="2", color="#718096"),
            rx.text(
                DescripcionState.destino["precio"].to_string(),
                size="7",
                color="#198375",
                weight="bold",
                font_family="Playfair Display",
                padding = "15px",
            ),
            rx.text("por persona", size="2", color="#718096"),
            align_items="start",
            spacing="0",
            padding_bottom="4",
            border_bottom="1px solid #e2e8f0",
            width="100%",
            padding = "20px",
        ),
        rx.text(
            "Detalles del viaje",
            size="3",
            weight="bold",
            color="#0D3D37",
            font_family="Playfair Display",
            padding_top="2",
            padding_x = "20px",
        ),
        fila_resumen("Duración", DescripcionState.destino["duracion"]),
        fila_resumen("Hospedaje", DescripcionState.destino["hospedaje"]),
        fila_resumen("Transporte", DescripcionState.destino["transporte"]),
        fila_resumen("Comidas", DescripcionState.destino["comidas"]),
        rx.box(height="8px"),
        rx.link(
            rx.button(
                "¡Reservar este viaje! →",
                bg="#e6a950",
                color="white",
                width="100%",
                border_radius="12px",
                size="3",
                _hover={"bg": "#cf9340"},
                cursor="pointer",
                padding = "20px",
                box_shadow="0 4px 14px rgba(230,169,80,0.35)",
            ),
            href="/reservas",
            width="100%",
        ),
        rx.link(
            rx.button(
                "Cotizar por WhatsApp",
                width="100%",
                variant="outline",
                color="#198375",
                border_color="#198375",
                border_radius="12px",
                size="2",
                _hover={"bg": "#f0fff4"},
                cursor="pointer",
                padding = "20px",
            ),
            href="https://wa.me/18090000000",
            is_external=True,
            width="100%",
        ),
        bg="white",
        padding="6",
        border_radius="16px",
        border="1px solid #e2e8f0",
        box_shadow="0 4px 24px rgba(0,0,0,0.07)",
        spacing="2",
        align_items="start",
        width="100%",
        flex="1",
        min_width="260px",
    )
 
 
def itinerario_item(item: str) -> rx.Component:
    return rx.hstack(
        rx.box(
            width="10px",
            height="10px",
            border_radius="50%",
            bg="#e6a950",
            flex_shrink="0",
            margin_top="5px",
        ),
        rx.text(item, size="3", color="#4a5568", line_height="1.6"),
        align_items="start",
        spacing="3",
        width="100%",
    )
 
 
def itinerario_section() -> rx.Component:
    return rx.vstack(
        rx.heading("Itinerario", size="5", font_family="Playfair Display", color="#0D3D37"),
        rx.divider(border_color="#e6a950", border_width="2px", width="60px", margin_bottom="2"),
        rx.vstack(
            rx.foreach(DescripcionState.itinerario, itinerario_item),
            spacing="3",
            width="100%",
            bg="white",
            padding="20px",
            border_radius="12px",
            border="1px solid #e2e8f0",
        ),
        align_items="start",
        width="100%",
        spacing="3",
    )
 
 
def item_incluye(item: str) -> rx.Component:
    return rx.hstack(
        rx.text("✓", color="#1D9E75", weight="bold", size="3"),
        rx.text(item, size="2", color="#4a5568"),
        spacing="2",
        align_items="start",
        padding="20px",
    )
 
 
def item_no_incluye(item: str) -> rx.Component:
    return rx.hstack(
        rx.text("✗", color="#e53e3e", weight="bold", size="3"),
        rx.text(item, size="2", color="#4a5568"),
        spacing="2",
        align_items="start",
        padding="20px",
    )
 
 
def incluye_section() -> rx.Component:
    return rx.grid(
        rx.vstack(
            rx.heading("El precio incluye", size="4", font_family="Playfair Display", color="#0D3D37"),
            rx.divider(border_color="#1D9E75", border_width="2px", width="50px", margin_bottom="2"),
            rx.foreach(DescripcionState.incluye, item_incluye),
            align_items="start",
            spacing="3",
            bg="white",
            padding="20px",
            border_radius="12px",
            border="1px solid #e2e8f0",
            width="100%",
        ),
        rx.vstack(
            rx.heading("El precio NO incluye", size="4", font_family="Playfair Display", color="#0D3D37"),
            rx.divider(border_color="#e53e3e", border_width="2px", width="50px", margin_bottom="2"),
            rx.foreach(DescripcionState.no_incluye, item_no_incluye),
            align_items="start",
            spacing="3",
            bg="white",
            padding="20px",
            border_radius="12px",
            border="1px solid #e2e8f0",
            width="100%",
        ),
        columns="2",
        gap="4",
        width="100%",
    )
 
 
def descripcion() -> rx.Component:
    return rx.vstack(
        navbar_buttons(),
        hero_descripcion(),
        rx.box(
            rx.vstack(
                rx.flex(
                    columna_izquierda(),
                    columna_derecha(),
                    direction="row",
                    spacing="6",
                    width="100%",
                    align_items="start",
                    flex_wrap="wrap",
                ),
                rx.divider(border_color="#d7ba98", margin_y="4"),
                itinerario_section(),
                rx.divider(border_color="#d7ba98", margin_y="4"),
                incluye_section(),
                spacing="0",
                width="100%",
                align_items="start",
            ),
            width="100%",
            max_width="1100px",
            margin_x="auto",
            padding_x=["4", "8", "12"],
            padding_y="10",
        ),
        footer(),
        width="100%",
        min_height="100vh",
        bg="#d7ba98",
        spacing="0",
    )