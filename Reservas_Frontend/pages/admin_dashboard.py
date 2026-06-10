import reflex as rx
from Reservas_Frontend.pages.admin_login import AdminLoginState


RESERVAS_MOCK = [
    {"id": 1, "nombre": "María Rodríguez", "email": "maria@email.com", "telefono": "809-555-0101", "destino": "Playa Rincón, Samaná",    "personas": 2, "fecha": "2025-08-15", "pago": "Tarjeta",       "estado": "Confirmada"},
    {"id": 2, "nombre": "Carlos Méndez",   "email": "carlos@email.com","telefono": "829-555-0234", "destino": "Laguna Dudú, Río San Juan","personas": 4, "fecha": "2025-09-02", "pago": "Transferencia", "estado": "Pendiente"},
    {"id": 3, "nombre": "Ana Jiménez",     "email": "ana.j@email.com", "telefono": "849-555-0378", "destino": "Isla Saona, La Romana",    "personas": 2, "fecha": "2025-09-20", "pago": "Efectivo",      "estado": "Confirmada"},
    {"id": 4, "nombre": "Luis Peña",       "email": "lpeña@email.com", "telefono": "809-555-0492", "destino": "27 Charcos de Damajagua",  "personas": 3, "fecha": "2025-10-05", "pago": "Tarjeta",       "estado": "Pendiente"},
]

DESTINOS_MOCK = [
    {"id": 1, "nombre": "Playa Rincón, Samaná",    "precio": 4500, "duracion": "1 día completo", "activo": True},
    {"id": 2, "nombre": "Laguna Dudú, Río San Juan","precio": 3800, "duracion": "1 día completo", "activo": True},
    {"id": 3, "nombre": "Isla Saona, La Romana",    "precio": 6200, "duracion": "1 día completo", "activo": True},
    {"id": 4, "nombre": "27 Charcos de Damajagua",  "precio": 5100, "duracion": "1 día completo", "activo": False},
]

ESTADOS_RESERVA = ["Confirmada", "Pendiente", "Cancelada"]

GOLD   = "#C8902A"
DARK   = "#2C2416"
MUTED  = "#9B8A6E"
BORDER = "#EDE0C4"
BG     = "#FAF6EF"
WHITE  = "white"


# ═══════════════════════════════════════════════════════
#  ESTADO
# ═══════════════════════════════════════════════════════
class AdminDashboardState(rx.State):
    pestana_activa: str = "Reservas"

    # Reservas
    reservas: list[dict] = RESERVAS_MOCK
    cargando_reservas: bool = False
    modal_estado_abierto: bool = False
    reserva_sel_id: int = -1
    nuevo_estado: str = ""
    modal_del_reserva_abierto: bool = False
    reserva_del_id: int = -1

    # Destinos
    destinos: list[dict] = DESTINOS_MOCK
    cargando_destinos: bool = False
    modal_destino_abierto: bool = False
    destino_edit_id: int = -1
    form_nombre: str = ""
    form_precio: str = ""
    form_duracion: str = ""
    form_activo: bool = True
    form_error: str = ""
    modal_del_destino_abierto: bool = False
    destino_del_id: int = -1

    # Toast
    toast_msg: str = ""
    toast_tipo: str = "ok"

    @rx.var
    def total_reservas(self) -> int:
        return len(self.reservas)

    @rx.var
    def reservas_confirmadas(self) -> int:
        return sum(1 for r in self.reservas if r.get("estado") == "Confirmada")

    @rx.var
    def reservas_pendientes(self) -> int:
        return sum(1 for r in self.reservas if r.get("estado") == "Pendiente")

    @rx.var
    def destinos_activos(self) -> int:
        return sum(1 for d in self.destinos if d.get("activo"))

    @rx.var
    def modal_destino_titulo(self) -> str:
        return "Nuevo destino" if self.destino_edit_id == -1 else "Editar destino"

    # ── Navegación ──
    def cambiar_pestana(self, p: str):
        self.pestana_activa = p

    def cerrar_sesion(self):
        AdminLoginState.logged_in = False
        return rx.redirect("/admin")

    def on_load_check(self):
        if not AdminLoginState.logged_in:
            return rx.redirect("/admin")

    # ── Toast ──
    async def _toast(self, msg: str, tipo: str = "ok"):
        self.toast_msg = msg
        self.toast_tipo = tipo
        yield
        import asyncio; await asyncio.sleep(3)
        self.toast_msg = ""

    # ══════════════════════════════════════════
    #  RESERVAS
    # ══════════════════════════════════════════
    async def cargar_reservas(self):
        self.cargando_reservas = True; yield
        import asyncio; await asyncio.sleep(0.6)
        self.reservas = RESERVAS_MOCK          # ← reemplazar: httpx GET /reservas
        self.cargando_reservas = False

    def abrir_modal_estado(self, rid: int):
        self.reserva_sel_id = rid
        for r in self.reservas:
            if r["id"] == rid:
                self.nuevo_estado = r["estado"]; break
        self.modal_estado_abierto = True

    def cerrar_modal_estado(self):
        self.modal_estado_abierto = False

    def set_nuevo_estado(self, v: str):
        self.nuevo_estado = v

    async def guardar_estado(self):
        self.reservas = [
            {**r, "estado": self.nuevo_estado} if r["id"] == self.reserva_sel_id else r
            for r in self.reservas
        ]
        self.modal_estado_abierto = False
        # ← reemplazar: httpx PATCH /reservas/{id}/estado
        async for _ in self._toast(f"Estado → {self.nuevo_estado}"): yield

    def abrir_del_reserva(self, rid: int):
        self.reserva_del_id = rid
        self.modal_del_reserva_abierto = True

    def cerrar_del_reserva(self):
        self.modal_del_reserva_abierto = False

    async def confirmar_del_reserva(self):
        self.reservas = [r for r in self.reservas if r["id"] != self.reserva_del_id]
        self.modal_del_reserva_abierto = False
        # ← reemplazar: httpx DELETE /reservas/{id}
        async for _ in self._toast("Reserva eliminada", "error"): yield

    # ══════════════════════════════════════════
    #  DESTINOS
    # ══════════════════════════════════════════
    async def cargar_destinos(self):
        self.cargando_destinos = True; yield
        import asyncio; await asyncio.sleep(0.6)
        self.destinos = DESTINOS_MOCK           # ← reemplazar: httpx GET /ofertas
        self.cargando_destinos = False

    def abrir_nuevo_destino(self):
        self.destino_edit_id = -1
        self.form_nombre = ""; self.form_precio = ""
        self.form_duracion = ""; self.form_activo = True
        self.form_error = ""
        self.modal_destino_abierto = True

    def abrir_editar_destino(self, did: int):
        for d in self.destinos:
            if d["id"] == did:
                self.destino_edit_id = did
                self.form_nombre   = d["nombre"]
                self.form_precio   = str(d["precio"])
                self.form_duracion = d["duracion"]
                self.form_activo   = d["activo"]
                break
        self.form_error = ""
        self.modal_destino_abierto = True

    def cerrar_modal_destino(self):
        self.modal_destino_abierto = False

    def set_form_nombre(self, v: str):   self.form_nombre = v
    def set_form_precio(self, v: str):   self.form_precio = v
    def set_form_duracion(self, v: str): self.form_duracion = v
    def toggle_activo(self):             self.form_activo = not self.form_activo

    async def guardar_destino(self):
        if not self.form_nombre.strip():
            self.form_error = "El nombre es obligatorio."; return
        if not self.form_precio.strip() or not self.form_precio.replace(".","").isdigit():
            self.form_error = "Ingresa un precio válido."; return
        if not self.form_duracion.strip():
            self.form_error = "La duración es obligatoria."; return

        if self.destino_edit_id == -1:
            nid = max((d["id"] for d in self.destinos), default=0) + 1
            self.destinos = self.destinos + [{
                "id": nid, "nombre": self.form_nombre.strip(),
                "precio": float(self.form_precio),
                "duracion": self.form_duracion.strip(),
                "activo": self.form_activo,
            }]
            # ← reemplazar: httpx POST /ofertas
            async for _ in self._toast(f'"{self.form_nombre}" agregado'): yield
        else:
            self.destinos = [
                {**d, "nombre": self.form_nombre.strip(),
                 "precio": float(self.form_precio),
                 "duracion": self.form_duracion.strip(),
                 "activo": self.form_activo}
                if d["id"] == self.destino_edit_id else d
                for d in self.destinos
            ]
            # ← reemplazar: httpx PUT /ofertas/{id}
            async for _ in self._toast("Destino actualizado"): yield
        self.modal_destino_abierto = False

    def abrir_del_destino(self, did: int):
        self.destino_del_id = did
        self.modal_del_destino_abierto = True

    def cerrar_del_destino(self):
        self.modal_del_destino_abierto = False

    async def confirmar_del_destino(self):
        self.destinos = [d for d in self.destinos if d["id"] != self.destino_del_id]
        self.modal_del_destino_abierto = False
        # ← reemplazar: httpx DELETE /ofertas/{id}
        async for _ in self._toast("Destino eliminado", "error"): yield

    async def toggle_activo_destino(self, did: int):
        self.destinos = [
            {**d, "activo": not d["activo"]} if d["id"] == did else d
            for d in self.destinos
        ]
        # ← reemplazar: httpx PATCH /ofertas/{id}/activo
        async for _ in self._toast("Visibilidad actualizada"): yield


# ═══════════════════════════════════════════════════════
#  HELPERS UI
# ═══════════════════════════════════════════════════════
def btn(label, on_click, var="primario", ico=None, sm=False):
    pad = "7px 14px" if sm else "10px 20px"
    fs  = "0.82rem" if sm else "0.9rem"
    V = {
        "primario":   {"background": f"linear-gradient(135deg,{GOLD} 0%,#A0701A 100%)", "color": WHITE, "border": "none", "_hover": {"opacity":"0.88","transform":"translateY(-1px)"}},
        "secundario": {"background": WHITE,       "color": GOLD,     "border": f"1.5px solid {GOLD}",   "_hover": {"background":"#FDF8F0"}},
        "peligro":    {"background": WHITE,       "color": "#C0392B","border": "1.5px solid #F5C6C0",   "_hover": {"background":"#FEF0EE"}},
        "fantasma":   {"background": "transparent","color": MUTED,   "border": f"1.5px solid {BORDER}", "_hover": {"border_color":GOLD,"color":GOLD}},
    }[var]
    return rx.box(
        rx.hstack(
            *([rx.icon(ico, size=13)] if ico else []),
            rx.text(label, style={"font_size":fs,"font_weight":"600","font_family":"Inter, sans-serif","color":V.get("color",DARK)}),
            spacing="1", align="center",
        ),
        on_click=on_click,
        style={**V,"padding":pad,"border_radius":"8px","cursor":"pointer",
               "transition":"all 0.18s","display":"inline-flex","align_items":"center"},
    )


# ═══════════════════════════════════════════════════════
#  NAVBAR ADMIN
# ═══════════════════════════════════════════════════════
def admin_navbar():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.box(
                    rx.image(src="/LogoChill2.png", width="30px", height="30px", style={"object_fit":"contain"}),
                    style={"background":WHITE,"border_radius":"8px","padding":"4px","box_shadow":"0 1px 4px rgba(200,144,42,0.2)"},
                ),
                rx.text("Chill Plans · Admin",
                        style={"font_family":"'Playfair Display',serif","font_size":"1.05rem","font_weight":"700","color":DARK}),
                spacing="3", align="center",
            ),
            btn("Cerrar sesión", AdminDashboardState.cerrar_sesion, var="fantasma", ico="log-out", sm=True),
            justify="between", align="center", style={"width":"100%"},
        ),
        style={"background":WHITE,"border_bottom":f"1px solid {BORDER}","padding":"14px 32px",
               "position":"sticky","top":"0","z_index":"100","box_shadow":"0 1px 8px rgba(44,36,22,0.06)"},
    )


# ═══════════════════════════════════════════════════════
#  TABS
# ═══════════════════════════════════════════════════════
def tab_btn(nombre, ico):
    activo = AdminDashboardState.pestana_activa == nombre
    return rx.box(
        rx.hstack(
            rx.icon(ico, size=15),
            rx.text(nombre, style={"font_size":"0.9rem","font_weight":"600","font_family":"Inter, sans-serif"}),
            spacing="2", align="center",
        ),
        on_click=lambda: AdminDashboardState.cambiar_pestana(nombre),
        style=rx.cond(activo,
            {"padding":"9px 20px","border_radius":"8px","cursor":"pointer","background":GOLD,"color":WHITE,"box_shadow":"0 2px 8px rgba(200,144,42,0.3)"},
            {"padding":"9px 20px","border_radius":"8px","cursor":"pointer","background":WHITE,"color":MUTED,"border":f"1px solid {BORDER}","_hover":{"border_color":GOLD,"color":GOLD}},
        ),
    )


# ═══════════════════════════════════════════════════════
#  STATS
# ═══════════════════════════════════════════════════════
def stat_card(titulo, valor, color, ico):
    return rx.box(
        rx.vstack(
            rx.box(rx.icon(ico, size=20, color=color),
                   style={"background":f"{color}18","border_radius":"10px","padding":"10px","width":"fit-content"}),
            rx.text(valor, style={"font_size":"2rem","font_weight":"800","color":DARK,
                                   "font_family":"'Playfair Display',serif","line_height":"1"}),
            rx.text(titulo, style={"font_size":"0.75rem","color":MUTED,"font_family":"Inter, sans-serif",
                                    "font_weight":"500","text_transform":"uppercase","letter_spacing":"0.06em"}),
            spacing="2", align="start",
        ),
        style={"background":WHITE,"border_radius":"14px","padding":"22px",
               "box_shadow":"0 2px 12px rgba(44,36,22,0.07)","border":f"1px solid {BORDER}",
               "flex":"1","min_width":"140px"},
    )


# ═══════════════════════════════════════════════════════
#  BADGES
# ═══════════════════════════════════════════════════════
def badge_estado(estado):
    return rx.cond(
        estado == "Confirmada",
        rx.box(rx.text(estado, style={"font_size":"0.75rem","font_weight":"600","font_family":"Inter, sans-serif","color":"#1E7E44"}),
               style={"background":"#E8F8EE","border":"1px solid #A8DFB8","border_radius":"20px","padding":"3px 10px","display":"inline-block"}),
        rx.cond(
            estado == "Pendiente",
            rx.box(rx.text(estado, style={"font_size":"0.75rem","font_weight":"600","font_family":"Inter, sans-serif","color":"#C07A00"}),
                   style={"background":"#FFF3CD","border":"1px solid #FFD97D","border_radius":"20px","padding":"3px 10px","display":"inline-block"}),
            rx.box(rx.text(estado, style={"font_size":"0.75rem","font_weight":"600","font_family":"Inter, sans-serif","color":"#C0392B"}),
                   style={"background":"#FEF0EE","border":"1px solid #F5C6C0","border_radius":"20px","padding":"3px 10px","display":"inline-block"}),
        ),
    )

def badge_activo(activo):
    return rx.cond(
        activo,
        rx.box(rx.text("Visible", style={"font_size":"0.75rem","font_weight":"600","font_family":"Inter, sans-serif","color":"#1E7E44"}),
               style={"background":"#E8F8EE","border":"1px solid #A8DFB8","border_radius":"20px","padding":"3px 10px","display":"inline-block"}),
        rx.box(rx.text("Oculto",  style={"font_size":"0.75rem","font_weight":"600","font_family":"Inter, sans-serif","color":"#6B7280"}),
               style={"background":"#F3F4F6","border":"1px solid #D1D5DB","border_radius":"20px","padding":"3px 10px","display":"inline-block"}),
    )


# ═══════════════════════════════════════════════════════
#  TABLA HELPERS
# ═══════════════════════════════════════════════════════
def th(t):
    return rx.box(rx.text(t, style={"font_size":"0.7rem","font_weight":"700","color":MUTED,
                                     "letter_spacing":"0.08em","text_transform":"uppercase","font_family":"Inter, sans-serif"}),
                  style={"padding":"11px 14px","flex":"1","min_width":"80px"})

def td(t, bold=False, color=DARK):
    return rx.box(rx.text(t, style={"font_size":"0.86rem","font_family":"Inter, sans-serif",
                                     "color":color,"font_weight":"600" if bold else "400","white_space":"nowrap"}),
                  style={"padding":"13px 14px","flex":"1","min_width":"80px"})

def accion_btn(ico, color, bg, bg_hover, on_click):
    return rx.box(rx.icon(ico, size=14, color=color),
                  on_click=on_click,
                  style={"cursor":"pointer","padding":"5px","border_radius":"6px","background":bg,
                         "_hover":{"background":bg_hover}})


# ═══════════════════════════════════════════════════════
#  TABLA RESERVAS
# ═══════════════════════════════════════════════════════
def fila_reserva(r: dict):
    return rx.box(
        rx.hstack(
            td(r["id"], color=MUTED),
            td(r["nombre"], bold=True),
            td(r["email"],    color="#6B7280"),
            td(r["telefono"], color="#6B7280"),
            td(r["destino"]),
            td(r["personas"]),
            td(r["fecha"], color="#6B7280"),
            td(r["pago"]),
            rx.box(badge_estado(r["estado"]), style={"padding":"13px 14px","flex":"1","min_width":"100px"}),
            rx.box(
                rx.hstack(
                    accion_btn("pencil",  GOLD,      "#FDF8F0","#F5EDD8", lambda: AdminDashboardState.abrir_modal_estado(r["id"])),
                    accion_btn("trash-2", "#C0392B", "#FEF0EE","#FAD7D0", lambda: AdminDashboardState.abrir_del_reserva(r["id"])),
                    spacing="2",
                ),
                style={"padding":"13px 14px","min_width":"80px"},
            ),
            style={"width":"100%","align_items":"center"},
        ),
        style={"border_bottom":f"1px solid {BORDER}","transition":"background 0.15s","_hover":{"background":"#FDFBF7"}},
    )

def seccion_reservas():
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Reservas", style={"font_family":"'Playfair Display',serif","font_size":"1.35rem","font_weight":"700","color":DARK}),
                rx.text("Gestiona y actualiza el estado de cada reserva", style={"font_size":"0.83rem","color":MUTED,"font_family":"Inter, sans-serif"}),
                spacing="1", align="start",
            ),
            btn("Actualizar", AdminDashboardState.cargar_reservas, var="secundario", ico="refresh-cw", sm=True),
            justify="between", align="end", style={"margin_bottom":"18px"},
        ),
        rx.box(
            rx.box(
                rx.box(rx.hstack(*[th(c) for c in ["ID","Nombre","Email","Teléfono","Destino","Personas","Fecha","Pago","Estado","Acciones"]], style={"width":"100%"}),
                       style={"background":"#FDF8F0","border_bottom":f"2px solid {BORDER}","border_radius":"12px 12px 0 0"}),
                rx.foreach(AdminDashboardState.reservas, fila_reserva),
                style={"background":WHITE,"border_radius":"12px","border":f"1px solid {BORDER}",
                       "box_shadow":"0 2px 12px rgba(44,36,22,0.06)","overflow":"hidden","min_width":"960px"},
            ),
            style={"overflow_x":"auto","width":"100%"},
        ),
    )


# ═══════════════════════════════════════════════════════
#  TABLA DESTINOS
# ═══════════════════════════════════════════════════════
def fila_destino(d: dict):
    return rx.box(
        rx.hstack(
            td(d["id"], color=MUTED),
            td(d["nombre"], bold=True),
            td(d["precio"]),
            td(d["duracion"]),
            rx.box(badge_activo(d["activo"]), style={"padding":"13px 14px","flex":"1","min_width":"90px"}),
            rx.box(
                rx.hstack(
                    accion_btn(
                        rx.cond(d["activo"],"eye-off","eye"),
                        rx.cond(d["activo"], MUTED, GOLD),
                        "#F3F4F6","#E5E7EB",
                        lambda: AdminDashboardState.toggle_activo_destino(d["id"]),
                    ),
                    accion_btn("pencil",  GOLD,      "#FDF8F0","#F5EDD8", lambda: AdminDashboardState.abrir_editar_destino(d["id"])),
                    accion_btn("trash-2", "#C0392B", "#FEF0EE","#FAD7D0", lambda: AdminDashboardState.abrir_del_destino(d["id"])),
                    spacing="2",
                ),
                style={"padding":"13px 14px","min_width":"120px"},
            ),
            style={"width":"100%","align_items":"center"},
        ),
        style={"border_bottom":f"1px solid {BORDER}","transition":"background 0.15s","_hover":{"background":"#FDFBF7"}},
    )

def seccion_destinos():
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Destinos turísticos", style={"font_family":"'Playfair Display',serif","font_size":"1.35rem","font_weight":"700","color":DARK}),
                rx.text("Agrega, edita o desactiva paquetes turísticos", style={"font_size":"0.83rem","color":MUTED,"font_family":"Inter, sans-serif"}),
                spacing="1", align="start",
            ),
            rx.hstack(
                btn("Actualizar",    AdminDashboardState.cargar_destinos,  var="fantasma",  ico="refresh-cw", sm=True),
                btn("Nuevo destino", AdminDashboardState.abrir_nuevo_destino, var="primario", ico="plus",       sm=True),
                spacing="3",
            ),
            justify="between", align="end", style={"margin_bottom":"18px"},
        ),
        rx.box(
            rx.box(
                rx.box(rx.hstack(*[th(c) for c in ["ID","Nombre","Precio (RD$)","Duración","Estado","Acciones"]], style={"width":"100%"}),
                       style={"background":"#FDF8F0","border_bottom":f"2px solid {BORDER}","border_radius":"12px 12px 0 0"}),
                rx.foreach(AdminDashboardState.destinos, fila_destino),
                style={"background":WHITE,"border_radius":"12px","border":f"1px solid {BORDER}",
                       "box_shadow":"0 2px 12px rgba(44,36,22,0.06)","overflow":"hidden","min_width":"700px"},
            ),
            style={"overflow_x":"auto","width":"100%"},
        ),
    )


# ═══════════════════════════════════════════════════════
#  MODALES
# ═══════════════════════════════════════════════════════
def overlay(contenido, abierto):
    return rx.cond(
        abierto,
        rx.box(
            rx.box(contenido,
                   style={"background":WHITE,"border_radius":"16px","padding":"32px",
                          "width":"100%","max_width":"440px","box_shadow":"0 16px 60px rgba(44,36,22,0.2)"}),
            style={"position":"fixed","inset":"0","z_index":"1000","background":"rgba(44,36,22,0.45)",
                   "display":"flex","align_items":"center","justify_content":"center","padding":"20px"},
        ),
        rx.box(),
    )

def modal_header(titulo, on_close):
    return rx.hstack(
        rx.text(titulo, style={"font_family":"'Playfair Display',serif","font_size":"1.2rem","font_weight":"700","color":DARK}),
        rx.box(rx.icon("x", size=18, color=MUTED), on_click=on_close,
               style={"cursor":"pointer","padding":"4px","border_radius":"6px","_hover":{"background":"#F3F4F6"}}),
        justify="between", align="center", style={"width":"100%"},
    )

# Modal cambiar estado
def modal_estado():
    opciones = rx.vstack(
        *[
            rx.box(
                rx.hstack(
                    rx.cond(AdminDashboardState.nuevo_estado == est,
                            rx.icon("circle-check-big", size=16, color=GOLD),
                            rx.icon("circle", size=16, color=BORDER)),
                    rx.text(est, style={"font_size":"0.92rem","font_family":"Inter, sans-serif","font_weight":"500","color":DARK}),
                    spacing="3", align="center",
                ),
                on_click=lambda: AdminDashboardState.set_nuevo_estado(est),
                style={"padding":"12px 16px","border_radius":"10px","cursor":"pointer",
                       "border":f"1.5px solid {BORDER}","width":"100%",
                       "transition":"all 0.15s","_hover":{"border_color":GOLD,"background":"#FDF8F0"}},
            )
            for est in ESTADOS_RESERVA
        ],
        spacing="3", style={"width":"100%","margin":"20px 0"},
    )
    contenido = rx.vstack(
        modal_header("Cambiar estado", AdminDashboardState.cerrar_modal_estado),
        rx.text("Selecciona el nuevo estado para esta reserva.",
                style={"font_size":"0.86rem","color":MUTED,"font_family":"Inter, sans-serif"}),
        opciones,
        rx.hstack(
            btn("Cancelar", AdminDashboardState.cerrar_modal_estado, var="fantasma"),
            btn("Guardar",  AdminDashboardState.guardar_estado,      var="primario"),
            spacing="3", justify="end", style={"width":"100%"},
        ),
        spacing="2", style={"width":"100%"},
    )
    return overlay(contenido, AdminDashboardState.modal_estado_abierto)

# Modal confirmar eliminar reserva
def modal_del_reserva():
    contenido = rx.vstack(
        rx.box(rx.icon("triangle-alert", size=32, color="#C0392B"),
               style={"background":"#FEF0EE","border_radius":"12px","padding":"14px","width":"fit-content","margin":"0 auto 8px"}),
        rx.text("¿Eliminar reserva?",
                style={"font_family":"'Playfair Display',serif","font_size":"1.2rem","font_weight":"700","color":DARK,"text_align":"center"}),
        rx.text("Esta acción no se puede deshacer.",
                style={"font_size":"0.86rem","color":MUTED,"text_align":"center","font_family":"Inter, sans-serif"}),
        rx.hstack(
            btn("Cancelar", AdminDashboardState.cerrar_del_reserva,    var="fantasma"),
            btn("Eliminar", AdminDashboardState.confirmar_del_reserva, var="peligro", ico="trash-2"),
            spacing="3", justify="center", style={"width":"100%","margin_top":"8px"},
        ),
        spacing="3", align="center", style={"width":"100%"},
    )
    return overlay(contenido, AdminDashboardState.modal_del_reserva_abierto)

# Modal nuevo / editar destino
def campo_form(label, placeholder, value, on_change, tipo="text"):
    return rx.vstack(
        rx.text(label, style={"font_size":"0.76rem","font_weight":"600","color":"#6B5A3E",
                               "letter_spacing":"0.07em","text_transform":"uppercase","font_family":"Inter, sans-serif"}),
        rx.input(placeholder=placeholder, value=value, on_change=on_change, type=tipo,
                 style={"width":"100%","padding":"10px 14px","border":f"1.5px solid {BORDER}",
                        "border_radius":"8px","font_size":"0.92rem","font_family":"Inter, sans-serif",
                        "background":"#FDFBF7","color":DARK,
                        "_focus":{"border_color":GOLD,"box_shadow":"0 0 0 3px rgba(200,144,42,0.12)"}}),
        spacing="1", style={"width":"100%"},
    )

def modal_destino():
    contenido = rx.vstack(
        modal_header(AdminDashboardState.modal_destino_titulo, AdminDashboardState.cerrar_modal_destino),
        campo_form("Nombre del destino", "Ej: Playa Rincón, Samaná",
                   AdminDashboardState.form_nombre, AdminDashboardState.set_form_nombre),
        rx.hstack(
            campo_form("Precio (RD$)", "Ej: 4500",
                       AdminDashboardState.form_precio, AdminDashboardState.set_form_precio, tipo="number"),
            campo_form("Duración", "Ej: 1 día completo",
                       AdminDashboardState.form_duracion, AdminDashboardState.set_form_duracion),
            spacing="3", style={"width":"100%"},
        ),
        rx.hstack(
            rx.box(
                style=rx.cond(AdminDashboardState.form_activo,
                    {"width":"42px","height":"24px","border_radius":"12px","background":GOLD,
                     "cursor":"pointer","transition":"background 0.2s"},
                    {"width":"42px","height":"24px","border_radius":"12px","background":"#D1D5DB",
                     "cursor":"pointer","transition":"background 0.2s"},
                ),
                on_click=AdminDashboardState.toggle_activo,
            ),
            rx.text("Visible en la plataforma",
                    style={"font_size":"0.88rem","font_family":"Inter, sans-serif","color":DARK,"font_weight":"500"}),
            spacing="3", align="center",
        ),
        rx.cond(
            AdminDashboardState.form_error != "",
            rx.box(rx.text(AdminDashboardState.form_error,
                           style={"font_size":"0.84rem","color":"#C0392B","font_family":"Inter, sans-serif"}),
                   style={"background":"#FEF0EE","border":"1px solid #F5C6C0","border_radius":"8px",
                          "padding":"10px 14px","width":"100%"}),
            rx.box(),
        ),
        rx.hstack(
            btn("Cancelar", AdminDashboardState.cerrar_modal_destino, var="fantasma"),
            btn("Guardar",  AdminDashboardState.guardar_destino,      var="primario", ico="save"),
            spacing="3", justify="end", style={"width":"100%"},
        ),
        spacing="4", style={"width":"100%"},
    )
    return overlay(contenido, AdminDashboardState.modal_destino_abierto)

# Modal confirmar eliminar destino
def modal_del_destino():
    contenido = rx.vstack(
        rx.box(rx.icon("triangle-alert", size=32, color="#C0392B"),
               style={"background":"#FEF0EE","border_radius":"12px","padding":"14px","width":"fit-content","margin":"0 auto 8px"}),
        rx.text("¿Eliminar destino?",
                style={"font_family":"'Playfair Display',serif","font_size":"1.2rem","font_weight":"700","color":DARK,"text_align":"center"}),
        rx.text("Este destino dejará de aparecer en la plataforma.",
                style={"font_size":"0.86rem","color":MUTED,"text_align":"center","font_family":"Inter, sans-serif"}),
        rx.hstack(
            btn("Cancelar", AdminDashboardState.cerrar_del_destino,    var="fantasma"),
            btn("Eliminar", AdminDashboardState.confirmar_del_destino, var="peligro", ico="trash-2"),
            spacing="3", justify="center", style={"width":"100%","margin_top":"8px"},
        ),
        spacing="3", align="center", style={"width":"100%"},
    )
    return overlay(contenido, AdminDashboardState.modal_del_destino_abierto)


# ═══════════════════════════════════════════════════════
#  TOAST
# ═══════════════════════════════════════════════════════
def toast():
    return rx.cond(
        AdminDashboardState.toast_msg != "",
        rx.box(
            rx.hstack(
                rx.icon(rx.cond(AdminDashboardState.toast_tipo == "ok","circle-check","circle-x"),
                        size=16,
                        color=rx.cond(AdminDashboardState.toast_tipo == "ok","#1E7E44","#C0392B")),
                rx.text(AdminDashboardState.toast_msg,
                        style={"font_size":"0.88rem","font_weight":"600","font_family":"Inter, sans-serif","color":DARK}),
                spacing="2", align="center",
            ),
            style={"position":"fixed","bottom":"28px","right":"28px","z_index":"2000",
                   "background":WHITE,"border_radius":"10px","padding":"14px 20px",
                   "box_shadow":"0 4px 24px rgba(44,36,22,0.16)",
                   "border":rx.cond(AdminDashboardState.toast_tipo=="ok","1.5px solid #A8DFB8","1.5px solid #F5C6C0"),
                   "animation":"slideIn 0.3s ease"},
        ),
        rx.box(),
    )


# ═══════════════════════════════════════════════════════
#  PÁGINA
# ═══════════════════════════════════════════════════════
def admin_dashboard() -> rx.Component:
    return rx.box(
        rx.html('<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">'),
        rx.html('<style>@keyframes slideIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}</style>'),
        admin_navbar(),
        rx.box(
            rx.vstack(
                rx.text("Panel de control",
                        style={"font_family":"'Playfair Display',serif","font_size":"1.7rem","font_weight":"700","color":DARK}),
                rx.text("Gestiona reservas y destinos de Chill Plans.",
                        style={"font_size":"0.9rem","color":MUTED,"font_family":"Inter, sans-serif"}),
                align="start", spacing="1", style={"margin_bottom":"24px"},
            ),
            # Stats
            rx.box(
                rx.hstack(
                    stat_card("Total reservas",   AdminDashboardState.total_reservas,      GOLD,      "calendar-check"),
                    stat_card("Confirmadas",       AdminDashboardState.reservas_confirmadas,"#27AE60", "circle-check"),
                    stat_card("Pendientes",        AdminDashboardState.reservas_pendientes, "#E67E22", "clock"),
                    stat_card("Destinos activos",  AdminDashboardState.destinos_activos,    "#2980B9", "map-pin"),
                    spacing="4", style={"flex_wrap":"wrap","width":"100%"},
                ),
                style={"margin_bottom":"32px"},
            ),
            # Tabs
            rx.hstack(
                tab_btn("Reservas", "calendar-check"),
                tab_btn("Destinos", "map-pin"),
                spacing="3", style={"margin_bottom":"28px"},
            ),
            # Contenido según pestaña
            rx.cond(
                AdminDashboardState.pestana_activa == "Reservas",
                seccion_reservas(),
                seccion_destinos(),
            ),
            style={"max_width":"1280px","margin":"0 auto","padding":"36px 32px"},
        ),
        modal_estado(),
        modal_del_reserva(),
        modal_destino(),
        modal_del_destino(),
        toast(),
        style={"background":BG,"min_height":"100vh","font_family":"Inter, sans-serif"},
        on_mount=AdminDashboardState.on_load_check,
    )