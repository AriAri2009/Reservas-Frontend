import reflex as rx

class AdminLoginState(rx.State):
    usuario: str = ""
    password: str = ""
    error: str = ""
    cargando: bool = False
    logged_in: bool = False
 
    # Credenciales simuladas hasta que el backend tenga el endpoint
    USUARIO_MOCK: str = "admin"
    PASSWORD_MOCK: str = "chillplans2025"
 
    def set_usuario(self, value: str):
        self.usuario = value
        self.error = ""
 
    def set_password(self, value: str):
        self.password = value
        self.error = ""
 
    async def iniciar_sesion(self):
        # Validación básica
        if not self.usuario.strip() or not self.password.strip():
            self.error = "Por favor completa todos los campos."
            return
 
        self.cargando = True
        yield
 
        # ── OPCIÓN A: Login simulado (activo por ahora) ──────────────────
        import asyncio
        await asyncio.sleep(0.8)  # Simula latencia de red
 
        if self.usuario == self.USUARIO_MOCK and self.password == self.PASSWORD_MOCK:
            self.logged_in = True
            self.error = ""
            self.cargando = False
            yield rx.redirect("/admin/dashboard")
        else:
            self.error = "Usuario o contraseña incorrectos."
            self.cargando = False
 
        # ── OPCIÓN B: Login real con API (descomentar cuando el backend esté listo) ──
        # import httpx
        # API_URL = "http://localhost:8000"  # Cambiar por URL de Render en producción
        # try:
        #     async with httpx.AsyncClient() as client:
        #         resp = await client.post(
        #             f"{API_URL}/admin/login",
        #             json={"usuario": self.usuario, "password": self.password},
        #             timeout=10.0,
        #         )
        #     if resp.status_code == 200:
        #         self.logged_in = True
        #         self.error = ""
        #         self.cargando = False
        #         yield rx.redirect("/admin/dashboard")
        #     else:
        #         self.error = "Usuario o contraseña incorrectos."
        #         self.cargando = False
        # except Exception:
        #     self.error = "No se pudo conectar con el servidor. Intenta de nuevo."
        #     self.cargando = False
 
 
# ─────────────────────────────────────────────
#  Componentes internos
# ─────────────────────────────────────────────
 
def campo_input(
    label: str,
    placeholder: str,
    value,
    on_change,
    tipo: str = "text",
) -> rx.Component:
    return rx.box(
        rx.text(
            label,
            style={
                "font_size": "0.78rem",
                "font_weight": "600",
                "color": "#6B5A3E",
                "letter_spacing": "0.07em",
                "text_transform": "uppercase",
                "margin_bottom": "6px",
                "font_family": "Inter, sans-serif",
            },
        ),
        rx.input(
            placeholder=placeholder,
            value=value,
            on_change=on_change,
            type=tipo,
            style={
                "width": "100%",
                "height": "42px",
                "padding": "12px 16px",
                "border": "1.5px solid #D6C9B0",
                "border_radius": "10px",
                "font_size": "0.97rem",
                "font_family": "Inter, sans-serif",
                "color": "#2C2416",
                "background": "#FDFBF7",
                "outline": "none",
                "transition": "border 0.2s",
                "_focus": {
                    "border_color": "#C8902A",
                    "box_shadow": "0 0 0 3px rgba(200,144,42,0.15)",
                },
                "_placeholder": {"color": "#B0A090"},
            },
        ),
        style={"width": "100%", "margin_bottom": "20px"},
    )
 
 
def mensaje_error() -> rx.Component:
    return rx.cond(
        AdminLoginState.error != "",
        rx.box(
            rx.hstack(
                rx.icon("circle-alert", size=16, color="#C0392B"),
                rx.text(
                    AdminLoginState.error,
                    style={
                        "font_size": "0.88rem",
                        "color": "#C0392B",
                        "font_family": "Inter, sans-serif",
                    },
                ),
                spacing="2",
                align="center",
            ),
            style={
                "background": "#FEF0EE",
                "border": "1px solid #F5C6C0",
                "border_radius": "8px",
                "padding": "10px 14px",
                "margin_bottom": "18px",
                "width": "100%",
            },
        ),
        rx.box(),  # vacío si no hay error
    )
 
 
def boton_login() -> rx.Component:
    return rx.box(
        rx.cond(
            AdminLoginState.cargando,
            # Estado cargando
            rx.box(
                rx.hstack(
                    rx.spinner(size="3", color="white"),
                    rx.text(
                        "Verificando...",
                        style={
                            "color": "white",
                            "font_weight": "600",
                            "font_family": "Inter, sans-serif",
                        },
                    ),
                    spacing="2",
                    justify="center",
                    align="center",
                ),
                style={
                    "width": "100%",
                    "padding": "13px",
                    "background": "#C8902A",
                    "border_radius": "10px",
                    "opacity": "0.8",
                    "text_align": "center",
                    "cursor": "not-allowed",
                },
            ),
            # Estado normal
            rx.box(
                rx.text(
                    "Entrar al panel",
                    style={
                        "color": "white",
                        "font_weight": "700",
                        "font_size": "1rem",
                        "font_family": "Georgia, serif",
                        "font_weight": "bold",
                        "letter_spacing": "0.03em",
                    },
                ),
                on_click=AdminLoginState.iniciar_sesion,
                style={
                    "width": "100%",
                    "padding": "13px",
                    "background": "linear-gradient(135deg, #C8902A 0%, #A0701A 100%)",
                    "border_radius": "10px",
                    "text_align": "center",
                    "cursor": "pointer",
                    "transition": "opacity 0.2s, transform 0.15s",
                    "_hover": {"opacity": "0.9", "transform": "translateY(-1px)"},
                    "_active": {"transform": "translateY(0)"},
                },
            ),
        ),
        style={"width": "100%"},
    )
 
 
def volver_inicio() -> rx.Component:
    return rx.box(
        rx.link(
            rx.hstack(
                rx.icon("arrow-left", size=14, color="#9B8A6E"),
                rx.text(
                    "Volver al inicio",
                    style={
                        "font_size": "0.85rem",
                        "color": "#cf9340",
                        "font_family": "Playfair Display, serif",
                    },
                ),
                spacing="1",
                align="center",
            ),
            href="/",
            style={"text_decoration": "none", "_hover": {"opacity": "0.7"}},
        ),
        style={"margin_top": "24px", "text_align": "center"},
    )
 
 
# ─────────────────────────────────────────────
#  Página principal
# ─────────────────────────────────────────────
 
def admin_login() -> rx.Component:
    return rx.box(
        # Fondo con textura sutil
        rx.box(
            # Tarjeta central
            rx.box(
                # Logo + encabezado
                rx.vstack(
                    rx.box(
                        rx.image(
                            src="/LogoChillP.png",  # Cambia por el path real de tu logo
                            width="56px",
                            height="56px",
                            style={"object_fit": "contain"},
                        ),
                        style={
                            "background": "white",
                            "border_radius": "16px",
                            "padding": "10px",
                            "box_shadow": "0 2px 12px rgba(200,144,42,0.18)",
                            "margin_bottom": "4px",
                        },
                    ),
                    
                    rx.image(
                        src="/Chill.png",
                        width="250px",
                        height="auto",
                        style={"object_fit": "contain"},
                    ),
                    
                    rx.text(
                        "Planes relajados para viajeros auténticos",
                        style={
                            "font_size": "0.85rem",
                            "color": "#198375",
                            "font_family": "Georgia, serif",
                            "font_style": "italic",
                            "margin_top": "-6px",
                            "spacing": "0.1em",
                        },
                    ),
                    
                    rx.text(
                        "Panel de administración",
                        style={
                            "font_size": "0.92rem",
                            "color": "#cf9340",
                            "font_family": "Playfair Display, serif",
                            "font_weight": "bold",
                            "margin_top": "-6px",
                        },
                    ),
                    align="center",
                    spacing="2",
                    style={"margin_bottom": "32px"},
                ),
                # Formulario
                campo_input(
                    "Usuario",
                    "admin",
                    AdminLoginState.usuario,
                    AdminLoginState.set_usuario,
                ),
                campo_input(
                    "Contraseña",
                    "••••••••",
                    AdminLoginState.password,
                    AdminLoginState.set_password,
                    tipo="password",
                ),
                mensaje_error(),
                boton_login(),
                volver_inicio(),
                style={
                    "background": "white",
                    "border_radius": "20px",
                    "padding": "40px 36px",
                    "box_shadow": "0 8px 40px rgba(44,36,22,0.12)",
                    "width": "100%",
                    "max_width": "400px",
                },
            ),
            style={
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
                "min_height": "100vh",
                "padding": "24px",
                "background": "linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),url('/PlayaDomi.jpg')",
            },
        ),
        # Enlace a Google Fonts (Playfair Display + Inter)
        rx.html(
            '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">'
        ),
    )