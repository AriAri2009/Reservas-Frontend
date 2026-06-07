import reflex as rx

def cards(imagen_url: str, titulo_destino: str, precio_destino: str, descripcion_corta: str) -> rx.Component:
    return rx.vstack(
        rx.image(
            src=imagen_url, 
            width="100%", 
            height="200px", 
            object_fit="cover", 
            border_radius="10px"
            ),
    rx.vstack(
        rx.heading(
            titulo_destino, 
            size="3", 
            weight="bold", 
            font_family="Playfair Display", 
            color="#198375"),
     rx.text(
                descripcion_corta,
                size="2",
                color="#718096",
                line_height="1.4"
            ),
            
            # Precio destacado
            rx.text(
                f"Desde {precio_destino}", 
                size="3", 
                weight="bold", 
                color="#2D3748",
                margin_top="2"
            ),
            
            # 3. Botón de Acción con Enlace directo a descripciones
            rx.link(
                rx.button(
                    "Ver Detalles →", 
                    size="2", 
                    bg="#f68f42", 
                    color="white", 
                    width="100%",
                    cursor="pointer",
                    _hover={"bg": "#f3a56a"}  # Efecto sutil al pasar el mouse
                ),
                href="/descripcion",  # Redirecciona a pages/descripcion.py
                width="100%",
                margin_top="auto"     # Empuja el botón al fondo si los textos varían de tamaño
            ),
            
            align_items="start",
            spacing="2",
            width="100%",
            padding="4",
        ),
        
        border="1px solid #E2E8F0",
        border_radius="xl",
        overflow="hidden",
        bg="#f5f5f5",
        box_shadow="md",
        width="100%",
        transition="transform 0.2s ease, box_shadow 0.2s ease",
        _hover={
            "transform": "translateY(-4px)", # Pequeña animación flotante al pasar el mouse
            "box_shadow": "lg"
        }
    )