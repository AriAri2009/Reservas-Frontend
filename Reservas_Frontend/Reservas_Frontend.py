"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from Reservas_Frontend.components.navbar import navbar_buttons
from Reservas_Frontend.components.footer import footer
from Reservas_Frontend.components.cards import cards
from Reservas_Frontend.components.search import search_form

class State(rx.State):
    """The app state."""

def hero_section() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/LogoChill2.png",
            width=["250px", "350px", "450px"],
            height="auto",
            object_fit="contain",
            margin_bottom="4",
        ),
        
        rx.text(
            "Planes relajados para viajeros auténticos",
            size="4",
            color="white",
            text_align="center",
            font_family="Playfair Display",
            font_style="italic",
            text_shadow="2px 2px 4px rgba(0, 0, 0, 0.6)",
        ),
        
        background_image="linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),url('/Travel.jpg')",
        background_size="cover",
        background_position="center",
        background_repeat="no-repeat",
        
        width="100%",
        height="65vh",          # Ocupa el 65% de la altura de la pantalla
        justify="center",       # Centra todo el bloque (imagen + texto) verticalmente
        align_items="center",   # Centra todo horizontalmente uno debajo del otro
        spacing="0", 
     # Controlamos el espacio manualmente con márgenes
    )

def offers_section() -> rx.Component:
    return rx.box(
            rx.vstack(
                rx.heading(
                "Ofertas Destacadas",
                size="6",
                weight="bold",
                font_family="Playfair Display",
                color="white",
                margin_bottom="4"
            ),
            rx.flex(
            cards(
                imagen_url="/Paris.jpg",
                titulo_destino="París, Francia",
                precio_destino="$999",
                descripcion_corta="Descubre la ciudad del amor con nuestro paquete exclusivo."
            ),
            cards(
                imagen_url="/Tokyo.jpg",
                titulo_destino="Tokio, Japón",
                precio_destino="$1299",
                descripcion_corta="Explora la vibrante cultura japonesa con nosotros."
            ),
            cards(
                imagen_url="/NewYork.jpg",
                titulo_destino="Nueva York, EE.UU.",
                precio_destino="$899",
                descripcion_corta="Vive la energía de la Gran Manzana con nuestras ofertas especiales."
            ),
            spacing="6",  
            wrap="wrap",
            justify="center",  
            width="100%", 
            
            ),
            width="100%",
            max_width="1200px",    
            padding_x="4",
            padding_y="12", # Añade un espaciado estético arriba y abajo de la sección
            
        ),
        width="100%",
        display="flex",
        justify_content="center",
        bg = "#d7ba98", 
        )
    
def contact_section() -> rx.Component:
    """Sección de contacto e información de la empresa."""

    return rx.box(

        rx.flex(

            # ---------------- IMAGEN ----------------
            rx.image(
                src="/Mar.jpg",
                width="40%",
                height="300px",
                object_fit="cover",
                border_radius="20px 0 0 20px",
            ),


            # ---------------- CONTENIDO ----------------
            rx.vstack(

                rx.heading(
                    "¿Tienes alguna pregunta?",
                    size="6",
                    font_family="Playfair Display",
                    color="white",
                    text_align="center",
                ),


                rx.text(
                    "Contáctanos y te ayudamos a planear tu próxima aventura dominicana",
                    size="3",
                    font_family="Georgia",
                    color="rgba(255,255,255,0.85)",
                    text_align="center",
                    max_width="500px",
                ),


                # -------- DATOS DE CONTACTO --------
                rx.hstack(

                    rx.vstack(
                        rx.text(
                            "Dirección",
                            font_family="Playfair Display",
                            font_style="italic",
                            weight="bold",
                            color="white",
                            size="3",
                        ),

                        rx.text(
                            "Av. Abraham Lincoln,\nSanto Domingo, RD",
                            color="rgba(255,255,255,0.8)",
                            size="2",
                            text_align="center",
                        ),

                        align_items="center",
                        spacing="2",
                    ),



                    rx.vstack(
                        rx.text(
                            "Email",
                            font_family="Playfair Display",
                            font_style="italic",
                            weight="bold",
                            color="white",
                            size="3",
                        ),

                        rx.text(
                            "hola@chillplans.do",
                            color="rgba(255,255,255,0.8)",
                            size="2",
                            text_align="center",
                        ),

                        align_items="center",
                        spacing="2",
                    ),



                    rx.vstack(
                        rx.text(
                            "WhatsApp",
                            font_family="Playfair Display",
                            font_style="italic",
                            weight="bold",
                            color="white",
                            size="3",
                        ),

                        rx.text(
                            "+1 (809) 000-0000",
                            color="rgba(255,255,255,0.8)",
                            size="2",
                            text_align="center",
                        ),

                        align_items="center",
                        spacing="2",
                    ),


                    spacing="6",
                    justify="center",
                    width="100%",
                ),



                # -------- BOTÓN --------
                rx.link(
                    rx.button(
                        "Hacer una reserva →",
                        size="3",
                        bg="#e6a950",
                        color="white",
                        border_radius="12px",
                        font_family="Playfair Display",
                        cursor="pointer",
                        _hover={
                            "bg": "#cf9340"
                        },
                    ),
                    href="/reservas",
                    margin_top="6",
                ),


                spacing="5",
                align_items="center",
                width="60%",
                padding="8",
            ),


            direction="row",
            width="100%",
            spacing="0",
            align="stretch",
        ),


        width="100%",
        bg="#198375",
        overflow="hidden",
        padding_x="6",
    )
   
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            navbar_buttons(),
            hero_section(),
            
            rx.box(
                search_form(),
                width="100%",
                display="flex",
                justify_content="center",
                margin_top="-50px",
                z_index="10",
                position="relative",
            ),
            
            rx.box(height="40px", bg="#f5f0e9"),
            
            offers_section(),
            
            rx.box(height="40px", bg="#d7ba98"),
            
            contact_section(),
            
                rx.box(height="40px", bg="#198375"),
            
            footer(),
            
            width="100%",  
            spacing="0",
            bg="#f5f0e9",  
        
        ),
        width="100%",
        min_height="100vh", 
        bg="#f5f0e9",
    )


app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap",
    ],
)
app.add_page(index, route="/")
