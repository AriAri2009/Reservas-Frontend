import reflex as rx
from Reservas_Frontend.mock_data import OFERTAS_MOCK


class HomeState(rx.State):
    # ── Lista de ofertas (se reemplaza con GET /ofertas cuando el backend esté listo) ──
    ofertas: list[dict] = OFERTAS_MOCK

    # ── Buscador ──
    busqueda_nombre: str = ""
    busqueda_fecha: str = ""
    error_busqueda: str = ""
    resultados: list[dict] = OFERTAS_MOCK  # arranca mostrando todos

    # ── Destino seleccionado (para pasar a /descripcion) ──
    destino_id_seleccionado: int = -1

    # ─────────────────────────────────────────
    #  Buscador — filtrar en tiempo real por nombre
    # ─────────────────────────────────────────
    def set_busqueda_nombre(self, value: str):
        self.busqueda_nombre = value
        self.error_busqueda = ""
        self._filtrar()

    def set_busqueda_fecha(self, value: str):
        self.busqueda_fecha = value
        self.error_busqueda = ""

    def _filtrar(self):
        """Filtra las ofertas por nombre en tiempo real."""
        texto = self.busqueda_nombre.strip().lower()
        if not texto:
            self.resultados = self.ofertas
        else:
            self.resultados = [
                o for o in self.ofertas
                if texto in o["nombre"].lower()
                or texto in o["descripcion_corta"].lower()
            ]

    def buscar(self):
        """
        Se llama al presionar el botón Buscar.
        Valida que si se escribió un nombre, exista al menos un resultado.
        Si hay resultados → hace scroll a la sección de ofertas.
        """
        nombre = self.busqueda_nombre.strip()
        fecha = self.busqueda_fecha.strip()

        # Validación de fecha: no puede ser en el pasado
        if fecha:
            from datetime import date
            try:
                fecha_elegida = date.fromisoformat(fecha)
                if fecha_elegida < date.today():
                    self.error_busqueda = "La fecha no puede ser en el pasado."
                    return
            except ValueError:
                self.error_busqueda = "Fecha no válida."
                return

        # Validación de nombre: si escribió algo que no existe
        self._filtrar()
        if nombre and not self.resultados:
            self.error_busqueda = f'No encontramos "{nombre}" entre nuestros destinos disponibles.'
            return

        self.error_busqueda = ""
        # Scroll automático a la sección de ofertas
        return rx.call_script(
            "document.getElementById('ofertas').scrollIntoView({ behavior: 'smooth' })"
        )

    # ─────────────────────────────────────────
    #  Seleccionar destino → navegar a /descripcion
    # ─────────────────────────────────────────
    def seleccionar_destino(self, destino_id: int):
        self.destino_id_seleccionado = destino_id
        return rx.redirect("/descripcion")