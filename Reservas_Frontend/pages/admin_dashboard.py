import reflex as rx

 
 
RESERVAS_MOCK = [
    {"id": 1, "nombre": "María Rodríguez", "email": "maria@email.com", "telefono": "809-555-0101", "destino": "Playa Rincón, Samaná",     "personas": 2, "fecha": "2025-08-15", "pago": "Tarjeta",       "estado": "Confirmada"},
    {"id": 2, "nombre": "Carlos Méndez",   "email": "carlos@email.com","telefono": "829-555-0234", "destino": "Laguna Dudú, Río San Juan", "personas": 4, "fecha": "2025-09-02", "pago": "Transferencia", "estado": "Pendiente"},
    {"id": 3, "nombre": "Ana Jiménez",     "email": "ana.j@email.com", "telefono": "849-555-0378", "destino": "Isla Saona, La Romana",     "personas": 2, "fecha": "2025-09-20", "pago": "Efectivo",      "estado": "Confirmada"},
    {"id": 4, "nombre": "Luis Peña",       "email": "lpeña@email.com", "telefono": "809-555-0492", "destino": "27 Charcos de Damajagua",   "personas": 3, "fecha": "2025-10-05", "pago": "Tarjeta",       "estado": "Pendiente"},
]
 
DESTINOS_MOCK = [
    {
        "id": 1, "nombre": "Playa Rincón, Samaná", "precio": 4500, "duracion": "1 día completo", "activo": True,
        "descripcion_corta": "Una de las playas más vírgenes del Caribe.",
        "descripcion_general": "Playa Rincón es considerada una de las diez playas más hermosas del mundo.",
        "imagen_url": "/playa_rincon.jpg",           # inicio + hero descripción
        "imagen_secundaria": "/playa_rincon2.jpg",   # tarjeta principal descripción
        "imagen_galeria_1": "/playa_rincon3.jpg",    # galería descripción
        "imagen_galeria_2": "/playa_rincon4.jpg",
        "imagen_galeria_3": "/playa_rincon5.jpg",
        "hospedaje": "No incluido (day trip)", "transporte": "Lancha incluida", "comidas": "Almuerzo de pescado incluido",
        "incluye": "Transporte en lancha, Almuerzo de pescado, Guía local, Equipo de snorkel",
        "no_incluye": "Bebidas adicionales, Propinas, Gastos personales",
        "itinerario": "07:00 AM — Salida desde Santo Domingo\n10:30 AM — Llegada a Las Galeras\n11:00 AM — Llegada a Playa Rincón\n01:00 PM — Almuerzo\n03:30 PM — Regreso",
    },
    {
        "id": 2, "nombre": "Laguna Dudú, Río San Juan", "precio": 3800, "duracion": "1 día completo", "activo": True,
        "descripcion_corta": "Lagunas azul turquesa rodeadas de palmeras.",
        "descripcion_general": "La Laguna Dudú es un sistema de lagunas naturales de aguas azul intenso.",
        "imagen_url": "/laguna_dudu.jpg",
        "imagen_secundaria": "/laguna_dudu2.jpg",
        "imagen_galeria_1": "/laguna_dudu3.jpg",
        "imagen_galeria_2": "/laguna_dudu4.jpg",
        "imagen_galeria_3": "/laguna_dudu5.jpg",
        "hospedaje": "No incluido", "transporte": "Autobús incluido desde SD", "comidas": "Snacks incluidos",
        "incluye": "Transporte ida y vuelta, Entrada a las lagunas, Tirolesa, Snacks y agua, Guía local",
        "no_incluye": "Almuerzo, Propinas, Fotografías profesionales",
        "itinerario": "06:30 AM — Salida desde Santo Domingo\n10:00 AM — Llegada a Laguna Dudú\n10:15 AM — Tirolesa\n04:30 PM — Salida de regreso",
    },
    {
        "id": 3, "nombre": "Isla Saona, La Romana", "precio": 6200, "duracion": "1 día completo", "activo": True,
        "descripcion_corta": "La postal perfecta del Caribe.",
        "descripcion_general": "Isla Saona forma parte del Parque Nacional del Este.",
        "imagen_url": "/isla_saona.jpg",
        "imagen_secundaria": "/isla_saona2.jpg",
        "imagen_galeria_1": "/isla_saona3.jpg",
        "imagen_galeria_2": "/isla_saona4.jpg",
        "imagen_galeria_3": "/isla_saona5.jpg",
        "hospedaje": "No incluido", "transporte": "Catamarán y lancha incluidos", "comidas": "Almuerzo buffet y open bar",
        "incluye": "Lancha rápida de ida, Catamarán de regreso con open bar, Piscina natural, Almuerzo buffet, Snorkel",
        "no_incluye": "Bebidas fuera del open bar, Propinas, Fotos profesionales",
        "itinerario": "08:00 AM — Salida en lancha\n09:30 AM — Piscina natural\n11:00 AM — Isla Saona\n03:00 PM — Regreso en catamarán",
    },
    {
        "id": 4, "nombre": "27 Charcos de Damajagua", "precio": 5100, "duracion": "1 día completo", "activo": False,
        "descripcion_corta": "Adrenalina pura entre cascadas naturales.",
        "descripcion_general": "Sistema de cascadas naturales de roca caliza ubicadas cerca de Puerto Plata.",
        "imagen_url": "/damajagua.jpg",
        "imagen_secundaria": "/damajagua2.jpg",
        "imagen_galeria_1": "/damajagua3.jpg",
        "imagen_galeria_2": "/damajagua4.jpg",
        "imagen_galeria_3": "/damajagua5.jpg",
        "hospedaje": "No incluido", "transporte": "Autobús desde Puerto Plata", "comidas": "No incluidas",
        "incluye": "Transporte, Entrada y guía certificado, Casco y chaleco, Opción de 7/12/27 charcos",
        "no_incluye": "Alimentación, Propinas, Zapatos de agua",
        "itinerario": "08:30 AM — Encuentro en Puerto Plata\n09:30 AM — Llegada a Damajagua\n10:00 AM — Caminata\n04:00 PM — Regreso",
    },
]
 
ESTADOS_RESERVA = ["Confirmada", "Pendiente", "Cancelada"]
 
GOLD   = "#C8902A"
DARK   = "#2C2416"
MUTED  = "#9B8A6E"
BORDER = "#EDE0C4"
BG     = "#FAF6EF"
WHITE  = "white"
 
# Anchos fijos para cada columna de la tabla de reservas
COL_WIDTHS_RESERVA = {
    "id":       "50px",
    "nombre":   "150px",
    "email":    "180px",
    "telefono": "130px",
    "destino":  "180px",
    "personas": "80px",
    "fecha":    "100px",
    "pago":     "110px",
    "estado":   "110px",
    "acciones": "90px",
}
 
COL_WIDTHS_DESTINO = {
    "id":       "50px",
    "nombre":   "220px",
    "precio":   "110px",
    "duracion": "140px",
    "estado":   "90px",
    "acciones": "110px",
}
 
 
# ═══════════════════════════════════════════════════════
#  ESTADO
# ═══════════════════════════════════════════════════════
class AdminDashboardState(rx.State):
    pestana_activa: str = "Reservas"
 
    sesion_activa: bool = False
    logged_in_cache: bool = False
    # Reservas
    reservas: list[dict] = RESERVAS_MOCK
    cargando_reservas: bool = False
    modal_estado_abierto: bool = False
    reserva_sel_id: int = -1
    nuevo_estado: str = ""
    modal_del_reserva_abierto: bool = False
    reserva_del_id: int = -1
 
    # Destinos — campos del formulario completo
    destinos: list[dict] = DESTINOS_MOCK
    cargando_destinos: bool = False
    modal_destino_abierto: bool = False
    destino_edit_id: int = -1
    form_nombre: str = ""
    form_precio: str = ""
    form_duracion: str = ""
    form_activo: bool = True
    form_descripcion_corta: str = ""
    form_descripcion_general: str = ""
    form_imagen_url: str = ""
    form_imagen_secundaria: str = ""
    form_imagen_galeria_1: str = ""
    form_imagen_galeria_2: str = ""
    form_imagen_galeria_3: str = ""
    form_hospedaje: str = ""
    form_transporte: str = ""
    form_comidas: str = ""
    form_incluye: str = ""
    form_no_incluye: str = ""
    form_itinerario: str = ""
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
 
    def cambiar_pestana(self, p: str):
        self.pestana_activa = p
    
    def activar_sesion(self):
        """Llamado desde admin_login cuando el login es exitoso."""
        self.sesion_activa = True
 
    def cerrar_sesion(self):
        self.sesion_activa = False
        return rx.redirect("/admin_login")
 
    def on_load_check(self):
    # Copia el valor al State local para poder usarlo con if normal
       if not self.sesion_activa:
            return rx.redirect("/admin_login")
 
    async def _toast(self, msg: str, tipo: str = "ok"):
        self.toast_msg = msg
        self.toast_tipo = tipo
        yield
        import asyncio; await asyncio.sleep(3)
        self.toast_msg = ""
 
    # ── Reservas ──
    async def cargar_reservas(self):
        self.cargando_reservas = True; yield
        import asyncio; await asyncio.sleep(0.6)
        self.reservas = RESERVAS_MOCK
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
        async for _ in self._toast(f"Estado → {self.nuevo_estado}"): yield
 
    def abrir_del_reserva(self, rid: int):
        self.reserva_del_id = rid
        self.modal_del_reserva_abierto = True
 
    def cerrar_del_reserva(self):
        self.modal_del_reserva_abierto = False
 
    async def confirmar_del_reserva(self):
        self.reservas = [r for r in self.reservas if r["id"] != self.reserva_del_id]
        self.modal_del_reserva_abierto = False
        async for _ in self._toast("Reserva eliminada", "error"): yield
 
    # ── Destinos ──
    async def cargar_destinos(self):
        self.cargando_destinos = True; yield
        import asyncio; await asyncio.sleep(0.6)
        self.destinos = DESTINOS_MOCK
        self.cargando_destinos = False
 
    def _limpiar_form(self):
        self.destino_edit_id = -1
        self.form_nombre = ""; self.form_precio = ""
        self.form_duracion = ""; self.form_activo = True
        self.form_descripcion_corta = ""; self.form_descripcion_general = ""
        self.form_imagen_url = ""; self.form_imagen_secundaria = ""
        self.form_imagen_galeria_1 = ""; self.form_imagen_galeria_2 = ""; self.form_imagen_galeria_3 = ""
        self.form_hospedaje = ""; self.form_transporte = ""; self.form_comidas = ""
        self.form_incluye = ""; self.form_no_incluye = ""; self.form_itinerario = ""
        self.form_error = ""
 
    def abrir_nuevo_destino(self):
        self._limpiar_form()
        self.modal_destino_abierto = True
 
    def abrir_editar_destino(self, did: int):
        self._limpiar_form()
        for d in self.destinos:
            if d["id"] == did:
                self.destino_edit_id        = did
                self.form_nombre            = d.get("nombre", "")
                self.form_precio            = str(d.get("precio", ""))
                self.form_duracion          = d.get("duracion", "")
                self.form_activo            = d.get("activo", True)
                self.form_descripcion_corta   = d.get("descripcion_corta", "")
                self.form_descripcion_general = d.get("descripcion_general", "")
                self.form_imagen_url          = d.get("imagen_url", "")
                self.form_imagen_secundaria   = d.get("imagen_secundaria", "")
                self.form_imagen_galeria_1    = d.get("imagen_galeria_1", "")
                self.form_imagen_galeria_2    = d.get("imagen_galeria_2", "")
                self.form_imagen_galeria_3    = d.get("imagen_galeria_3", "")
                self.form_hospedaje           = d.get("hospedaje", "")
                self.form_transporte          = d.get("transporte", "")
                self.form_comidas             = d.get("comidas", "")
                self.form_incluye             = d.get("incluye", "")
                self.form_no_incluye          = d.get("no_incluye", "")
                self.form_itinerario          = d.get("itinerario", "")
                break
        self.modal_destino_abierto = True
 
    def cerrar_modal_destino(self):
        self.modal_destino_abierto = False
 
    def set_form_nombre(self, v: str):              self.form_nombre = v
    def set_form_precio(self, v: str):              self.form_precio = v
    def set_form_duracion(self, v: str):            self.form_duracion = v
    def toggle_activo(self):                        self.form_activo = not self.form_activo
    def set_form_desc_corta(self, v: str):          self.form_descripcion_corta = v
    def set_form_desc_general(self, v: str):        self.form_descripcion_general = v
    def set_form_imagen_url(self, v: str):          self.form_imagen_url = v
    def set_form_imagen_secundaria(self, v: str):   self.form_imagen_secundaria = v
    def set_form_imagen_galeria_1(self, v: str):    self.form_imagen_galeria_1 = v
    def set_form_imagen_galeria_2(self, v: str):    self.form_imagen_galeria_2 = v
    def set_form_imagen_galeria_3(self, v: str):    self.form_imagen_galeria_3 = v
    def set_form_hospedaje(self, v: str):           self.form_hospedaje = v
    def set_form_transporte(self, v: str):          self.form_transporte = v
    def set_form_comidas(self, v: str):             self.form_comidas = v
    def set_form_incluye(self, v: str):             self.form_incluye = v
    def set_form_no_incluye(self, v: str):          self.form_no_incluye = v
    def set_form_itinerario(self, v: str):          self.form_itinerario = v
 
    async def guardar_destino(self):
        if not self.form_nombre.strip():
            self.form_error = "El nombre es obligatorio."; return
        if not self.form_precio.strip() or not self.form_precio.replace(".","").isdigit():
            self.form_error = "Ingresa un precio válido."; return
        if not self.form_duracion.strip():
            self.form_error = "La duración es obligatoria."; return
        if not self.form_imagen_url.strip():
            self.form_error = "La imagen principal es obligatoria."; return
 
        nuevo_data = {
            "nombre":               self.form_nombre.strip(),
            "precio":               float(self.form_precio),
            "duracion":             self.form_duracion.strip(),
            "activo":               self.form_activo,
            "descripcion_corta":    self.form_descripcion_corta.strip(),
            "descripcion_general":  self.form_descripcion_general.strip(),
            "imagen_url":           self.form_imagen_url.strip(),
            "imagen_secundaria":    self.form_imagen_secundaria.strip(),
            "imagen_galeria_1":     self.form_imagen_galeria_1.strip(),
            "imagen_galeria_2":     self.form_imagen_galeria_2.strip(),
            "imagen_galeria_3":     self.form_imagen_galeria_3.strip(),
            "hospedaje":            self.form_hospedaje.strip(),
            "transporte":           self.form_transporte.strip(),
            "comidas":              self.form_comidas.strip(),
            "incluye":              self.form_incluye.strip(),
            "no_incluye":           self.form_no_incluye.strip(),
            "itinerario":           self.form_itinerario.strip(),
        }
 
        if self.destino_edit_id == -1:
            nid = max((d["id"] for d in self.destinos), default=0) + 1
            self.destinos = self.destinos + [{"id": nid, **nuevo_data}]
            async for _ in self._toast(f'"{self.form_nombre}" agregado'): yield
        else:
            self.destinos = [
                {**d, **nuevo_data} if d["id"] == self.destino_edit_id else d
                for d in self.destinos
            ]
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
        async for _ in self._toast("Destino eliminado", "error"): yield
 
    async def toggle_activo_destino(self, did: int):
        self.destinos = [
            {**d, "activo": not d["activo"]} if d["id"] == did else d
            for d in self.destinos
        ]
        async for _ in self._toast("Visibilidad actualizada"): yield
 
 
# ═══════════════════════════════════════════════════════
#  HELPERS UI
# ═══════════════════════════════════════════════════════
def btn(label, on_click, var="primario", ico=None, sm=False):
    pad = "7px 14px" if sm else "10px 20px"
    fs  = "0.82rem" if sm else "0.9rem"
    V = {
        "primario":   {"background": f"linear-gradient(135deg,{GOLD} 0%,#A0701A 100%)", "color": WHITE, "border": "none", "_hover": {"opacity":"0.88","transform":"translateY(-1px)"}},
        "secundario": {"background": WHITE,        "color": GOLD,      "border": f"1.5px solid {GOLD}",   "_hover": {"background":"#FDF8F0"}},
        "peligro":    {"background": WHITE,        "color": "#C0392B", "border": "1.5px solid #F5C6C0",   "_hover": {"background":"#FEF0EE"}},
        "fantasma":   {"background": "transparent","color": MUTED,     "border": f"1.5px solid {BORDER}", "_hover": {"border_color":GOLD,"color":GOLD}},
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
#  NAVBAR
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
#  TABLA HELPERS — anchos fijos, sin flex:"1"
# ═══════════════════════════════════════════════════════
def th(t, w):
    return rx.box(
        rx.text(t, style={"font_size":"0.7rem","font_weight":"700","color":MUTED,
                           "letter_spacing":"0.08em","text_transform":"uppercase",
                           "font_family":"Inter, sans-serif","white_space":"nowrap"}),
        style={"padding":"11px 14px","width":w,"min_width":w,"flex_shrink":"0"},
    )
 
def td(t, w, bold=False, color=DARK):
    return rx.box(
        rx.text(t, style={"font_size":"0.86rem","font_family":"Inter, sans-serif",
                           "color":color,"font_weight":"600" if bold else "400",
                           "white_space":"nowrap","overflow":"hidden",
                           "text_overflow":"ellipsis"}),
        style={"padding":"13px 14px","width":w,"min_width":w,"flex_shrink":"0"},
    )
 
def accion_btn(ico, color, bg, bg_hover, on_click):
    return rx.box(
        rx.icon(ico, size=14, color=color),
        on_click=on_click,
        style={"cursor":"pointer","padding":"5px","border_radius":"6px","background":bg,
               "_hover":{"background":bg_hover}},
    )
 
 
# ═══════════════════════════════════════════════════════
#  TABLA RESERVAS
# ═══════════════════════════════════════════════════════
def fila_reserva(r: dict):
    w = COL_WIDTHS_RESERVA
    return rx.box(
        rx.hstack(
            td(r["id"],       w["id"],       color=MUTED),
            td(r["nombre"],   w["nombre"],   bold=True),
            td(r["email"],    w["email"],    color="#6B7280"),
            td(r["telefono"], w["telefono"], color="#6B7280"),
            td(r["destino"],  w["destino"]),
            td(r["personas"], w["personas"]),
            td(r["fecha"],    w["fecha"],    color="#6B7280"),
            td(r["pago"],     w["pago"]),
            rx.box(badge_estado(r["estado"]),
                   style={"padding":"13px 14px","width":w["estado"],"min_width":w["estado"],"flex_shrink":"0"}),
            rx.box(
                rx.hstack(
                    accion_btn("pencil",  GOLD,      "#FDF8F0","#F5EDD8", lambda: AdminDashboardState.abrir_modal_estado(r["id"])),
                    accion_btn("trash-2", "#C0392B", "#FEF0EE","#FAD7D0", lambda: AdminDashboardState.abrir_del_reserva(r["id"])),
                    spacing="2",
                ),
                style={"padding":"13px 14px","width":w["acciones"],"min_width":w["acciones"],"flex_shrink":"0"},
            ),
            spacing="0",
            style={"width":"100%","align_items":"center"},
        ),
        style={"border_bottom":f"1px solid {BORDER}","transition":"background 0.15s","_hover":{"background":"#FDFBF7"}},
    )
 
def seccion_reservas():
    w = COL_WIDTHS_RESERVA
    total_w = sum(int(v.replace("px","")) for v in w.values())
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Reservas", style={"font_family":"'Playfair Display',serif","font_size":"1.35rem","font_weight":"700","color":DARK}),
                rx.text("Gestiona y actualiza el estado de cada reserva",
                        style={"font_size":"0.83rem","color":MUTED,"font_family":"Inter, sans-serif"}),
                spacing="1", align="start",
            ),
            btn("Actualizar", AdminDashboardState.cargar_reservas, var="secundario", ico="refresh-cw", sm=True),
            justify="between", align="end", style={"margin_bottom":"18px"},
        ),
        rx.box(
            rx.box(
                # Cabecera
                rx.box(
                    rx.hstack(
                        th("ID",        w["id"]),
                        th("Nombre",    w["nombre"]),
                        th("Email",     w["email"]),
                        th("Teléfono",  w["telefono"]),
                        th("Destino",   w["destino"]),
                        th("Personas",  w["personas"]),
                        th("Fecha",     w["fecha"]),
                        th("Pago",      w["pago"]),
                        th("Estado",    w["estado"]),
                        th("Acciones",  w["acciones"]),
                        spacing="0", style={"width":"100%"},
                    ),
                    style={"background":"#FDF8F0","border_bottom":f"2px solid {BORDER}","border_radius":"12px 12px 0 0"},
                ),
                rx.foreach(AdminDashboardState.reservas, fila_reserva),
                style={"background":WHITE,"border_radius":"12px","border":f"1px solid {BORDER}",
                       "box_shadow":"0 2px 12px rgba(44,36,22,0.06)","overflow":"hidden",
                       "min_width":f"{total_w}px"},
            ),
            style={"overflow_x":"auto","width":"100%"},
        ),
    )
 
 
# ═══════════════════════════════════════════════════════
#  TABLA DESTINOS
# ═══════════════════════════════════════════════════════
def fila_destino(d: dict):
    w = COL_WIDTHS_DESTINO
    return rx.box(
        rx.hstack(
            td(d["id"],       w["id"],      color=MUTED),
            td(d["nombre"],   w["nombre"],  bold=True),
            td(d["precio"],   w["precio"]),
            td(d["duracion"], w["duracion"]),
            rx.box(badge_activo(d["activo"]),
                   style={"padding":"13px 14px","width":w["estado"],"min_width":w["estado"],"flex_shrink":"0"}),
            rx.box(
                rx.hstack(
                    accion_btn(
                        rx.cond(d["activo"], "eye-off", "eye"),
                        rx.cond(d["activo"], MUTED, GOLD),
                        "#F3F4F6","#E5E7EB",
                        lambda: AdminDashboardState.toggle_activo_destino(d["id"]),
                    ),
                    accion_btn("pencil",  GOLD,      "#FDF8F0","#F5EDD8", lambda: AdminDashboardState.abrir_editar_destino(d["id"])),
                    accion_btn("trash-2", "#C0392B", "#FEF0EE","#FAD7D0", lambda: AdminDashboardState.abrir_del_destino(d["id"])),
                    spacing="2",
                ),
                style={"padding":"13px 14px","width":w["acciones"],"min_width":w["acciones"],"flex_shrink":"0"},
            ),
            spacing="0",
            style={"width":"100%","align_items":"center"},
        ),
        style={"border_bottom":f"1px solid {BORDER}","transition":"background 0.15s","_hover":{"background":"#FDFBF7"}},
    )
 
def seccion_destinos():
    w = COL_WIDTHS_DESTINO
    total_w = sum(int(v.replace("px","")) for v in w.values())
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Destinos turísticos",
                        style={"font_family":"'Playfair Display',serif","font_size":"1.35rem","font_weight":"700","color":DARK}),
                rx.text("Agrega, edita o desactiva paquetes turísticos",
                        style={"font_size":"0.83rem","color":MUTED,"font_family":"Inter, sans-serif"}),
                spacing="1", align="start",
            ),
            rx.hstack(
                btn("Actualizar",    AdminDashboardState.cargar_destinos,     var="fantasma", ico="refresh-cw", sm=True),
                btn("Nuevo destino", AdminDashboardState.abrir_nuevo_destino, var="primario", ico="plus",       sm=True),
                spacing="3",
            ),
            justify="between", align="end", style={"margin_bottom":"18px"},
        ),
        rx.box(
            rx.box(
                rx.box(
                    rx.hstack(
                        th("ID",          w["id"]),
                        th("Nombre",      w["nombre"]),
                        th("Precio RD$",  w["precio"]),
                        th("Duración",    w["duracion"]),
                        th("Estado",      w["estado"]),
                        th("Acciones",    w["acciones"]),
                        spacing="0", style={"width":"100%"},
                    ),
                    style={"background":"#FDF8F0","border_bottom":f"2px solid {BORDER}","border_radius":"12px 12px 0 0"},
                ),
                rx.foreach(AdminDashboardState.destinos, fila_destino),
                style={"background":WHITE,"border_radius":"12px","border":f"1px solid {BORDER}",
                       "box_shadow":"0 2px 12px rgba(44,36,22,0.06)","overflow":"hidden",
                       "min_width":f"{total_w}px"},
            ),
            style={"overflow_x":"auto","width":"100%"},
        ),
    )
 
 
# ═══════════════════════════════════════════════════════
#  MODALES
# ═══════════════════════════════════════════════════════
def overlay(contenido, abierto, ancho="440px"):
    return rx.cond(
        abierto,
        rx.box(
            rx.box(
                contenido,
                style={"background":WHITE,"border_radius":"16px","padding":"32px",
                       "width":"100%","max_width":ancho,
                       "box_shadow":"0 16px 60px rgba(44,36,22,0.2)",
                       "max_height":"90vh","overflow_y":"auto"},
            ),
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
 
# ── Modal cambiar estado ──
def modal_estado():
    contenido = rx.vstack(
        modal_header("Cambiar estado", AdminDashboardState.cerrar_modal_estado),
        rx.text("Selecciona el nuevo estado para esta reserva.",
                style={"font_size":"0.86rem","color":MUTED,"font_family":"Inter, sans-serif"}),
        rx.vstack(
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
        ),
        rx.hstack(
            btn("Cancelar", AdminDashboardState.cerrar_modal_estado, var="fantasma"),
            btn("Guardar",  AdminDashboardState.guardar_estado,      var="primario"),
            spacing="3", justify="end", style={"width":"100%"},
        ),
        spacing="2", style={"width":"100%"},
    )
    return overlay(contenido, AdminDashboardState.modal_estado_abierto)
 
# ── Modal confirmar eliminar reserva ──
def modal_del_reserva():
    contenido = rx.vstack(
        rx.box(rx.icon("triangle-alert", size=32, color="#C0392B"),
               style={"background":"#FEF0EE","border_radius":"12px","padding":"14px",
                      "width":"fit-content","margin":"0 auto 8px"}),
        rx.text("¿Eliminar reserva?",
                style={"font_family":"'Playfair Display',serif","font_size":"1.2rem",
                       "font_weight":"700","color":DARK,"text_align":"center"}),
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
 
# ── Campos del formulario de destino ──
def campo_input(label, placeholder, value, on_change, tipo="text"):
    return rx.vstack(
        rx.text(label, style={"font_size":"0.74rem","font_weight":"600","color":"#6B5A3E",
                               "letter_spacing":"0.07em","text_transform":"uppercase",
                               "font_family":"Inter, sans-serif"}),
        rx.input(placeholder=placeholder, value=value, on_change=on_change, type=tipo,
                 style={"width":"100%","padding":"9px 12px","border":f"1.5px solid {BORDER}",
                        "border_radius":"8px","font_size":"0.9rem","font_family":"Inter, sans-serif",
                        "background":"#FDFBF7","color":DARK,
                        "_focus":{"border_color":GOLD,"box_shadow":"0 0 0 3px rgba(200,144,42,0.12)"}}),
        spacing="1", style={"width":"100%"},
    )
 
def campo_textarea(label, placeholder, value, on_change, altura="120px"):
    return rx.vstack(
        rx.text(
            label,
            style={
                "font_size": "0.74rem",
                "font_weight": "600",
                "color": "#6B5A3E",
                "letter_spacing": "0.07em",
                "text_transform": "uppercase",
                "font_family": "Inter, sans-serif",
            },
        ),

        rx.text_area(
            placeholder=placeholder,
            value=value,
            on_change=on_change,

            # Reflex 0.9.4 no acepta rows
            min_height=altura,

            # estilos directos, no dentro de style={}
            width="100%",
            padding="9px 12px",
            border=f"1.5px solid {BORDER}",
            border_radius="8px",
            font_size="0.88rem",
            font_family="Inter, sans-serif",
            background="#FDFBF7",
            color=DARK,
            resize="vertical",
        ),

        rx.text(
            "Separa los ítems con comas"
            if "incluye" in label.lower() or "itinerario" not in label.lower()
            else "Escribe cada paso en una línea",

            style={
                "font_size": "0.72rem",
                "color": MUTED,
                "font_family": "Inter, sans-serif",
            },
        ),

        spacing="1",
        style={"width": "100%"},
    )
 
def seccion_form(titulo):
    return rx.text(
        titulo,
        style={"font_size":"0.8rem","font_weight":"700","color":GOLD,"font_family":"Inter, sans-serif",
               "text_transform":"uppercase","letter_spacing":"0.08em",
               "border_bottom":f"1px solid {BORDER}","padding_bottom":"6px",
               "margin_top":"4px","width":"100%"},
    )
 
# ── Modal destino completo ──
def modal_destino():
    contenido = rx.vstack(
        modal_header(AdminDashboardState.modal_destino_titulo, AdminDashboardState.cerrar_modal_destino),
 
        # ── Información básica ──
        seccion_form("Información básica"),
        campo_input("Nombre del destino", "Ej: Playa Rincón, Samaná",
                    AdminDashboardState.form_nombre, AdminDashboardState.set_form_nombre),
        rx.hstack(
            campo_input("Precio (RD$)", "Ej: 4500",
                        AdminDashboardState.form_precio, AdminDashboardState.set_form_precio, tipo="number"),
            campo_input("Duración", "Ej: 1 día completo",
                        AdminDashboardState.form_duracion, AdminDashboardState.set_form_duracion),
            spacing="3", style={"width":"100%"},
        ),
        campo_input("Descripción corta", "Una línea que aparece en la tarjeta del inicio",
                    AdminDashboardState.form_descripcion_corta, AdminDashboardState.set_form_desc_corta),
        campo_textarea("Descripción general", "Texto completo que aparece en la página de descripción",
                       AdminDashboardState.form_descripcion_general, AdminDashboardState.set_form_desc_general, altura="120px"),
 
        # ── Imágenes ──
        seccion_form("Imágenes"),
        rx.text(
            "Escribe la ruta del archivo dentro de la carpeta /assets del proyecto (ej: /playa_rincon.jpg). "
            "La imagen principal se usa en la tarjeta del inicio y en el hero de descripción.",
            style={"font_size":"0.78rem","color":MUTED,"font_family":"Inter, sans-serif","margin_bottom":"4px"},
        ),
        rx.hstack(
            campo_input("Imagen principal ⭐", "/nombre_imagen.jpg",
                        AdminDashboardState.form_imagen_url, AdminDashboardState.set_form_imagen_url),
            campo_input("Imagen secundaria", "/nombre_imagen2.jpg",
                        AdminDashboardState.form_imagen_secundaria, AdminDashboardState.set_form_imagen_secundaria),
            spacing="3", style={"width":"100%"},
        ),
        rx.text("Galería (3 fotos que aparecen en la página de descripción)",
                style={"font_size":"0.78rem","font_weight":"600","color":MUTED,
                       "font_family":"Inter, sans-serif","margin_top":"8px"}),
        rx.hstack(
            campo_input("Galería 1", "/foto3.jpg",
                        AdminDashboardState.form_imagen_galeria_1, AdminDashboardState.set_form_imagen_galeria_1),
            campo_input("Galería 2", "/foto4.jpg",
                        AdminDashboardState.form_imagen_galeria_2, AdminDashboardState.set_form_imagen_galeria_2),
            campo_input("Galería 3", "/foto5.jpg",
                        AdminDashboardState.form_imagen_galeria_3, AdminDashboardState.set_form_imagen_galeria_3),
            spacing="3", style={"width":"100%"},
        ),
 
        # ── Logística ──
        seccion_form("Logística del viaje"),
        rx.hstack(
            campo_input("Hospedaje", "Ej: No incluido / Hotel incluido",
                        AdminDashboardState.form_hospedaje, AdminDashboardState.set_form_hospedaje),
            campo_input("Transporte", "Ej: Autobús incluido",
                        AdminDashboardState.form_transporte, AdminDashboardState.set_form_transporte),
            spacing="3", style={"width":"100%"},
        ),
        campo_input("Comidas", "Ej: Almuerzo incluido",
                    AdminDashboardState.form_comidas, AdminDashboardState.set_form_comidas),
 
        # ── Incluye / No incluye ──
        seccion_form("¿Qué incluye?"),
        campo_textarea("Incluye (separado por comas)", "Transporte, Guía local, Almuerzo, Equipo de snorkel",
                       AdminDashboardState.form_incluye, AdminDashboardState.set_form_incluye, altura="80px"),
        campo_textarea("No incluye (separado por comas)", "Bebidas adicionales, Propinas, Gastos personales",
                       AdminDashboardState.form_no_incluye, AdminDashboardState.set_form_no_incluye, altura="80px"),
 
        # ── Itinerario ──
        seccion_form("Itinerario"),
        campo_textarea("Itinerario (una línea por paso)", "07:00 AM — Salida desde Santo Domingo\n10:30 AM — Llegada al destino",
                       AdminDashboardState.form_itinerario, AdminDashboardState.set_form_itinerario, altura="200px"),
 
        # ── Toggle visible ──
        rx.hstack(
            rx.box(
                style=rx.cond(AdminDashboardState.form_activo,
                    {"width":"42px","height":"24px","border_radius":"12px","background":GOLD,"cursor":"pointer","transition":"background 0.2s"},
                    {"width":"42px","height":"24px","border_radius":"12px","background":"#D1D5DB","cursor":"pointer","transition":"background 0.2s"},
                ),
                on_click=AdminDashboardState.toggle_activo,
            ),
            rx.text("Visible en la plataforma",
                    style={"font_size":"0.88rem","font_family":"Inter, sans-serif","color":DARK,"font_weight":"500"}),
            spacing="3", align="center",
        ),
 
        # ── Error ──
        rx.cond(
            AdminDashboardState.form_error != "",
            rx.box(
                rx.text(AdminDashboardState.form_error,
                        style={"font_size":"0.84rem","color":"#C0392B","font_family":"Inter, sans-serif"}),
                style={"background":"#FEF0EE","border":"1px solid #F5C6C0","border_radius":"8px",
                       "padding":"10px 14px","width":"100%"},
            ),
            rx.box(),
        ),
 
        rx.hstack(
            btn("Cancelar", AdminDashboardState.cerrar_modal_destino, var="fantasma"),
            btn("Guardar",  AdminDashboardState.guardar_destino,      var="primario", ico="save"),
            spacing="3", justify="end", style={"width":"100%"},
        ),
        spacing="3", style={"width":"100%"},
    )
    return overlay(contenido, AdminDashboardState.modal_destino_abierto, ancho="640px")
 
# ── Modal confirmar eliminar destino ──
def modal_del_destino():
    contenido = rx.vstack(
        rx.box(rx.icon("triangle-alert", size=32, color="#C0392B"),
               style={"background":"#FEF0EE","border_radius":"12px","padding":"14px",
                      "width":"fit-content","margin":"0 auto 8px"}),
        rx.text("¿Eliminar destino?",
                style={"font_family":"'Playfair Display',serif","font_size":"1.2rem",
                       "font_weight":"700","color":DARK,"text_align":"center"}),
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
                rx.icon(
                    rx.cond(AdminDashboardState.toast_tipo == "ok","circle-check","circle-x"),
                    size=16,
                    color=rx.cond(AdminDashboardState.toast_tipo == "ok","#1E7E44","#C0392B"),
                ),
                rx.text(AdminDashboardState.toast_msg,
                        style={"font_size":"0.88rem","font_weight":"600",
                               "font_family":"Inter, sans-serif","color":DARK}),
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
            rx.box(
                rx.hstack(
                    stat_card("Total reservas",  AdminDashboardState.total_reservas,       GOLD,      "calendar-check"),
                    stat_card("Confirmadas",      AdminDashboardState.reservas_confirmadas, "#27AE60", "circle-check"),
                    stat_card("Pendientes",       AdminDashboardState.reservas_pendientes,  "#E67E22", "clock"),
                    stat_card("Destinos activos", AdminDashboardState.destinos_activos,     "#2980B9", "map-pin"),
                    spacing="4", style={"flex_wrap":"wrap","width":"100%"},
                ),
                style={"margin_bottom":"32px"},
            ),
            rx.hstack(
                tab_btn("Reservas", "calendar-check"),
                tab_btn("Destinos", "map-pin"),
                spacing="3", style={"margin_bottom":"28px"},
            ),
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