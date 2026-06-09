"""
Página de Reservas — Chill Plans
Ruta: /reservas

Cómo funciona:
- ReservaState: guarda todos los campos del formulario.
- Cada rx.input tiene value=State.campo y on_change=State.set_campo.
  Esto conecta el input con el State — lo que escribes se guarda automáticamente.
- enviar_reserva: cuando el usuario hace click en "Confirmar", 
  envía un POST a la API con los datos del formulario.
- Por ahora el POST está comentado y solo muestra un mensaje de éxito.
  Cuando tu compañero tenga la API lista, descomentas esa parte.
"""

import reflex as rx
from Reservas_Frontend.components.navbar import navbar_buttons
from Reservas_Frontend.components.footer import footer
from Reservas_Frontend.mock_data import OFERTAS_MOCK

# URL de la API — cuando tu compañero la tenga lista, pon la URL aquí
API_URL = "http://localhost:8000"


# ─── STATE ────────────────────────────────────────────────────────────────────

class ReservaState(rx.State):
    # Datos de contacto
    nombre: str = ""
    email: str = ""
    telefono: str = ""

    # Detalles del viaje
    destino_id: int = 1
    destino_nombre: str = "Playa Rincón, Samaná"
    cantidad_personas: int = 1
    fecha_viaje: str = ""

    # Pago
    metodo_pago: str = "Transferencia bancaria"

    # UI
    enviando: bool = False          # para deshabilitar el botón mientras envía
    mensaje: str = ""               # mensaje de éxito o error
    exito: bool = False             # si fue exitoso o no
    precio_total: float = 0.0      # se calcula según personas y destino

    def set_nombre(self, v: str):
        self.nombre = v

    def set_email(self, v: str):
        self.email = v

    def set_telefono(self, v: str):
        self.telefono = v

    def set_fecha(self, v: str):
        self.fecha_viaje = v

    def set_personas(self, v: str):
        """Convierte el string del input a número y recalcula el precio."""
        try:
            self.cantidad_personas = int(v)
        except ValueError:
            self.cantidad_personas = 1
        self.calcular_precio()

    def set_destino(self, nombre: str):
        """Cuando cambia el destino, actualiza el ID y el precio."""
        self.destino_nombre = nombre
        for o in OFERTAS_MOCK:
            if o["nombre"] == nombre:
                self.destino_id = o["id"]
                break
        self.calcular_precio()

    def set_metodo_pago(self, v: str):
        self.metodo_pago = v

    def calcular_precio(self):
        """Calcula el precio total según destino y cantidad de personas."""
        for o in OFERTAS_MOCK:
            if o["id"] == self.destino_id:
                self.precio_total = o["precio"] * self.cantidad_personas
                break

    def validar(self) -> bool:
        """Valida que los campos obligatorios estén llenos."""
        if not self.nombre.strip():
            self.mensaje = "Por favor escribe tu nombre completo."
            self.exito = False
            return False
        if not self.email.strip() or "@" not in self.email:
            self.mensaje = "Por favor escribe un email válido."
            self.exito = False
            return False
        if not self.telefono.strip():
            self.mensaje = "Por favor escribe tu teléfono."
            self.exito = False
            return False
        if not self.fecha_viaje:
            self.mensaje = "Por favor selecciona una fecha de viaje."
            self.exito = False
            return False
        return True

    async def enviar_reserva(self):
        """
        Envía los datos del formulario a la API.
        
        Por ahora simula el envío con un mensaje de éxito.
        Cuando la API esté lista, descomenta el bloque de httpx.
        """
        if not self.validar():
            return

        self.enviando = True
        self.mensaje = ""

        # ── CUANDO LA API ESTÉ LISTA, DESCOMENTAR ESTO ──────────────────────
        # import httpx
        # try:
        #     async with httpx.AsyncClient() as client:
        #         response = await client.post(
        #             f"{API_URL}/reservas",
        #             json={
        #                 "nombre_cliente": self.nombre,
        #                 "email": self.email,
        #                 "telefono": self.telefono,
        #                 "oferta_id": self.destino_id,
        #                 "cantidad_personas": self.cantidad_personas,
        #                 "fecha_reserva": self.fecha_viaje,
        #                 "metodo_pago": self.metodo_pago,
        #             },
        #             timeout=10.0,
        #         )
        #         if response.status_code == 200:
        #             self.exito = True
        #             self.mensaje = f"¡Reserva confirmada! Nos contactaremos a {self.email} pronto."
        #             # Limpia el formulario
        #             self.nombre = ""
        #             self.email = ""
        #             self.telefono = ""
        #             self.fecha_viaje = ""
        #         else:
        #             self.exito = False
        #             self.mensaje = "Hubo un problema al registrar tu reserva. Inténtalo de nuevo."
        # except Exception:
        #     self.exito = False
        #     self.mensaje = "No pudimos conectar con el servidor. Inténtalo más tarde."
        # ────────────────────────────────────────────────────────────────────

        # SIMULACIÓN TEMPORAL (borra esto cuando conectes la API)
        self.exito = True
        self.mensaje = f"¡Reserva recibida! Te contactaremos a {self.email} en breve. ✓"
        self.enviando = False


# ─── COMPONENTES ──────────────────────────────────────────────────────────────

def seccion_titulo(emoji: str, titulo: str) -> rx.Component:
    """Título de sección reutilizable."""
    return rx.hstack(
        rx.text(emoji, size="4"),
        rx.heading(titulo, size="4", font_family="Playfair Display", color="#0D3D37"),
        rx.divider(flex="1", border_color="#e2e8f0"),
        align_items="center",
        spacing="3",
        width="100%",
        margin_bottom="4",
    )


def campo_formulario(label: str, componente: rx.Component) -> rx.Component:
    """
    Wrapper para cada campo del formulario.
    Muestra la etiqueta encima del input.
    """
    return rx.vstack(
        rx.text(label, size="2", weight="bold", color="#4a5568"),
        componente,
        align_items="start",
        width="100%",
        spacing="1",
    )


def seccion_contacto() -> rx.Component:
    """Sección de datos personales del usuario."""
    return rx.vstack(
        seccion_titulo("👤", "Datos de contacto"),
        rx.grid(
            campo_formulario(
                "Nombre completo *",
                rx.input(
                    placeholder="Tu nombre y apellido",
                    value=ReservaState.nombre,
                    on_change=ReservaState.set_nombre,
                    size="3",
                    width="100%",
                    border_radius="8px",
                ),
            ),
            campo_formulario(
                "Correo electrónico *",
                rx.input(
                    placeholder="tucorreo@ejemplo.com",
                    value=ReservaState.email,
                    on_change=ReservaState.set_email,
                    type="email",
                    size="3",
                    width="100%",
                    border_radius="8px",
                ),
            ),
            campo_formulario(
                "Teléfono / WhatsApp *",
                rx.input(
                    placeholder="+1 (809) 000-0000",
                    value=ReservaState.telefono,
                    on_change=ReservaState.set_telefono,
                    type="tel",
                    size="3",
                    width="100%",
                    border_radius="8px",
                ),
            ),
            columns="2",
            gap="4",
            width="100%",
        ),
        width="100%",
        spacing="0",
    )


def seccion_actividad() -> rx.Component:
    """
    Sección de detalles del viaje.
    
    rx.select.root / trigger / content: es un dropdown/select de Reflex.
    on_change se dispara cuando el usuario selecciona una opción.
    """
    nombres_destinos = [o["nombre"] for o in OFERTAS_MOCK]

    return rx.vstack(
        seccion_titulo("✈️", "Detalles de la actividad"),
        rx.grid(
            campo_formulario(
                "Destino *",
                rx.select.root(
                    rx.select.trigger(
                        placeholder="Selecciona tu destino",
                        width="100%",
                        border_radius="8px",
                    ),
                    rx.select.content(
                        *[
                            rx.select.item(nombre, value=nombre)
                            for nombre in nombres_destinos
                        ],
                    ),
                    value=ReservaState.destino_nombre,
                    on_change=ReservaState.set_destino,
                    width="100%",
                ),
            ),
            campo_formulario(
                "Cantidad de personas *",
                rx.input(
                    placeholder="1",
                    value=ReservaState.cantidad_personas.to_string(),
                    on_change=ReservaState.set_personas,
                    type="number",
                    min="1",
                    max="20",
                    size="3",
                    width="100%",
                    border_radius="8px",
                ),
            ),
            campo_formulario(
                "Fecha del viaje *",
                rx.input(
                    value=ReservaState.fecha_viaje,
                    on_change=ReservaState.set_fecha,
                    type="date",
                    size="3",
                    width="100%",
                    border_radius="8px",
                ),
            ),
            columns="2",
            gap="4",
            width="100%",
        ),
        width="100%",
        spacing="0",
    )


def seccion_pago() -> rx.Component:
    """
    Sección de método de pago y resumen del total.
    Muestra el precio calculado automáticamente.
    """
    return rx.vstack(
        seccion_titulo("💳", "Información de pago"),
        rx.box(
            rx.vstack(
                # Resumen de precio
                rx.hstack(
                    rx.vstack(
                        rx.text("Total a pagar", size="2", color="#718096", weight="bold"),
                        rx.hstack(
                            rx.text("RD$", size="3", color="#198375"),
                            rx.text(
                                ReservaState.precio_total.to_string(),
                                size="6",
                                weight="bold",
                                color="#198375",
                                font_family="Playfair Display",
                            ),
                            align_items="baseline",
                            spacing="1",
                        ),
                        rx.text(
                            f"({ReservaState.cantidad_personas} persona(s))",
                            size="2",
                            color="#718096",
                        ),
                        align_items="start",
                        spacing="1",
                    ),
                    rx.spacer(),
                    rx.vstack(
                        rx.text("Método de pago", size="2", color="#718096", weight="bold"),
                        rx.select.root(
                            rx.select.trigger(
                                placeholder="Selecciona...",
                                width="220px",
                                border_radius="8px",
                            ),
                            rx.select.content(
                                rx.select.item("Transferencia bancaria", value="Transferencia bancaria"),
                                rx.select.item("Efectivo al llegar", value="Efectivo al llegar"),
                                rx.select.item("Tarjeta de crédito/débito", value="Tarjeta"),
                            ),
                            value=ReservaState.metodo_pago,
                            on_change=ReservaState.set_metodo_pago,
                        ),
                        align_items="start",
                        spacing="1",
                    ),
                    width="100%",
                    align_items="start",
                    flex_wrap="wrap",
                    gap="4",
                ),
                rx.divider(border_color="#e2e8f0", margin_y="4"),
                # Nota informativa
                rx.hstack(
                    rx.text("ℹ️", size="3"),
                    rx.text(
                        "El pago se confirma con nuestro equipo por WhatsApp. "
                        "Te contactaremos dentro de las próximas 24 horas para coordinar.",
                        size="2",
                        color="#718096",
                        line_height="1.6",
                    ),
                    align_items="start",
                    spacing="2",
                ),
                width="100%",
                spacing="0",
            ),
            bg="white",
            padding="6",
            border_radius="12px",
            border="1px solid #e2e8f0",
            width="100%",
        ),
        width="100%",
        spacing="0",
    )


def mensaje_respuesta() -> rx.Component:
    """
    Muestra el mensaje de éxito o error después de enviar.
    
    rx.cond: si exito es True muestra verde, si no muestra rojo.
    Solo se muestra si mensaje no está vacío.
    """
    return rx.cond(
        ReservaState.mensaje != "",
        rx.box(
            rx.hstack(
                rx.text(
                    rx.cond(ReservaState.exito, "✅", "❌"),
                    size="4",
                ),
                rx.text(
                    ReservaState.mensaje,
                    size="3",
                    color=rx.cond(ReservaState.exito, "#198375", "#c53030"),
                    weight="medium",
                ),
                align_items="center",
                spacing="3",
            ),
            bg=rx.cond(ReservaState.exito, "#f0fff4", "#fff5f5"),
            border=rx.cond(
                ReservaState.exito,
                "1px solid #9ae6b4",
                "1px solid #feb2b2",
            ),
            border_radius="10px",
            padding="4",
            width="100%",
        ),
        rx.box(),   # componente vacío cuando no hay mensaje
    )


# ─── PÁGINA COMPLETA ──────────────────────────────────────────────────────────

def reservas() -> rx.Component:
    """
    Ensambla la página de reservas.
    
    Todo el formulario está dentro de un rx.card para darle
    un aspecto de "papel" sobre el fondo.
    """
    return rx.box(
        navbar_buttons(),

        # Banner superior
        rx.box(
            rx.vstack(
                rx.heading(
                    "Haz tu reserva",
                    size="7",
                    color="white",
                    font_family="Playfair Display",
                    text_align="center",
                ),
                rx.text(
                    "Llena el formulario y nos ponemos en contacto contigo en menos de 24 horas",
                    size="3",
                    color="rgba(255,255,255,0.85)",
                    text_align="center",
                ),
                align_items="center",
                spacing="3",
                padding_y="10",
            ),
            width="100%",
            bg="#198375",
            display="flex",
            justify_content="center",
            padding_x="6",
        ),

        # Contenido del formulario
        rx.box(
            rx.vstack(
                # Tarjeta del formulario
                rx.card(
                    rx.vstack(
                        seccion_contacto(),
                        rx.box(height="8px"),
                        seccion_actividad(),
                        rx.box(height="8px"),
                        seccion_pago(),
                        rx.box(height="16px"),
                        mensaje_respuesta(),

                        # Botón de envío
                        rx.button(
                            rx.cond(
                                ReservaState.enviando,
                                "Enviando...",
                                "🚀 Confirmar y registrar reserva",
                            ),
                            on_click=ReservaState.enviar_reserva,
                            size="4",
                            width="100%",
                            bg="#e6a950",
                            color="white",
                            border_radius="12px",
                            font_family="Playfair Display",
                            font_size="16px",
                            padding_y="4",
                            _hover={"bg": "#cf9340"},
                            cursor="pointer",
                            disabled=ReservaState.enviando,
                            box_shadow="0 4px 14px rgba(230,169,80,0.35)",
                        ),
                        width="100%",
                        spacing="0",
                    ),
                    width="100%",
                    padding="8",
                    box_shadow="0 4px 24px rgba(0,0,0,0.08)",
                    border_radius="16px",
                    bg="white",
                ),
                width="100%",
                max_width="800px",
            ),
            width="100%",
            display="flex",
            justify_content="center",
            padding_y="10",
            padding_x=["4", "6", "8"],
            bg="#f5f0e9",
        ),

        footer(),

        width="100%",
        min_height="100vh",
        bg="#f5f0e9",
    )