# Chill Plans — Plataforma de Reservas Turísticas Dominicanas

Plataforma web para explorar y reservar paquetes turísticos en la República Dominicana. Desarrollada como proyecto académico con **Reflex 0.9.4** (frontend) y **FastAPI + MySQL** (backend).

---

## Descripción del proyecto

Chill Plans permite a los usuarios:

- Buscar destinos turísticos por nombre y fecha
- Ver detalles completos de cada destino (galería, itinerario, hospedaje, incluye/no incluye)
- Realizar reservas en línea
- Administrar reservas y destinos desde un panel de control privado

### Tecnologías

| Capa | Tecnología |
|------|------------|
| Frontend | Python + Reflex 0.9.4 |
| Backend | Python + FastAPI + SQLAlchemy |
| Base de datos | MySQL |
| Comunicación | HTTP REST (httpx) |

---

## Instalación y ejecución

### Requisitos previos

- Python 3.10+
- Node.js 18+ (requerido por Reflex internamente)
- Git

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/Reservas_Frontend.git
cd Reservas_Frontend
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install reflex==0.9.4 httpx
```

### 4. Ejecutar el frontend

```bash
reflex run
```

La app quedará disponible en `http://localhost:3000`.

> **Nota:** El backend debe estar corriendo en `http://localhost:8000` para que las llamadas a la API funcionen. Mientras no esté conectado, la app usa datos de `mock_data.py`.

### Ejecutar el backend (repositorio separado)

```bash
# En el repositorio del backend
pip install fastapi sqlalchemy pymysql python-dotenv uvicorn

uvicorn main:app --reload --host 0.0.0.0
```

---

## Estructura de carpetas

```
Reservas_Frontend/
│
├── Reservas_Frontend/          # Paquete principal de la app
│   ├── pages/
│   │   ├── admin_login.py      # Página de login del administrador
│   │   ├── admin_dashboard.py  # Panel CRUD de reservas y destinos
│   │   └── descripcion.py      # Página de detalle de un destino
│   │
│   ├── components/
│   │   ├── cards.py            # Tarjetas de destinos (home)
│   │   └── search.py           # Buscador con filtro por nombre y fecha
│   │
│   ├── state.py                # HomeState — estado global del inicio
│   ├── mock_data.py            # Datos de prueba (5 imágenes por destino)
│   └── Reservas_Frontend.py    # Página principal (home)
│
├── assets/                     # Imágenes y recursos estáticos
├── rxconfig.py                 # Configuración de Reflex
└── README.md
```

### Descripción de archivos clave

**`state.py` — HomeState**
Maneja el buscador, el filtrado de resultados y la navegación hacia `/descripcion`. Campos: `ofertas`, `busqueda_nombre`, `busqueda_fecha`, `resultados`, `destino_id_seleccionado`.

**`mock_data.py`**
Lista de destinos con estructura completa: 5 campos de imagen (`imagen_url`, `imagen_secundaria`, `imagen_galeria_1/2/3`), precio, duración, itinerario, incluye, no incluye.

**`pages/admin_dashboard.py`**
Panel privado con CRUD completo de reservas (cambiar estado, eliminar) y destinos (crear, editar, activar/desactivar, eliminar). Acceso por `/admin_login`.

---

## Backend

Repositorio del backend: `https://github.com/Mauelm1109/Reservas-turisticas-Back-End.git`

### Tecnologías

- Python 3.10+
- FastAPI
- SQLAlchemy + pymysql
- MySQL
- python-dotenv

### Instalación y ejecución

```bash
git clone https://github.com/TU_USUARIO/Reservas_Backend.git
cd Reservas_Backend

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install fastapi sqlalchemy pymysql python-dotenv uvicorn

uvicorn main:app --reload --host 0.0.0.0
```

El backend queda disponible en `http://localhost:8000` (o en la IP local de la laptop dentro de la red WiFi, ej: `http://192.168.x.x:8000`).

### Estructura

```
Reservas_Backend/
├── main.py              # Punto de entrada, configuración CORS
├── database.py          # Conexión a MySQL
├── models.py             # Modelos SQLAlchemy
├── schemas.py            # Esquemas Pydantic
└── routers/
    ├── ofertas.py
    └── reservas.py
```

### Endpoints disponibles

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/ofertas` | Listar destinos activos |
| POST | `/reservas` | Crear reserva |
| GET | `/reservas` | Listar reservas (admin) |
| PATCH | `/reservas/{id}/estado` | Cambiar estado de reserva |
| DELETE | `/reservas/{id}` | Eliminar reserva |

CORS está configurado para `localhost:3000`.

---

## Conexión Frontend ↔ Backend

Ambas laptops deben estar en la misma red WiFi. En la laptop del backend, correr `uvicorn main:app --reload --host 0.0.0.0` y obtener su IP local (`ipconfig` en Windows o `ip a` en Linux/Mac).

En el frontend, configurar la IP del backend en:

```python
# Reservas_Frontend/config.py (o al inicio de state.py / reservas.py / admin_dashboard.py)
API_URL = "http://<IP_DE_LA_LAPTOP_BACKEND>:8000"
```

Luego descomentar los bloques `httpx` en:
- `state.py` — `cargar_ofertas()` → `GET /ofertas`
- `pages/reservas.py` — `enviar_reserva()` → `POST /reservas`
- `pages/admin_dashboard.py` — `cargar_reservas()`, `guardar_estado()`, `confirmar_del_reserva()` → `GET /reservas`, `PATCH /reservas/{id}/estado`, `DELETE /reservas/{id}`

### Carga inicial de datos

Los destinos se cargan desde el panel de administración (`/admin_dashboard` → pestaña Destinos → "Nuevo destino") una vez la conexión esté activa. Las reservas se generan automáticamente cuando un usuario completa el formulario en `/reservas`.

---

## Créditos

Proyecto académico desarrollado por:

- **[Arianna]** — Interfaz de usuario con Reflex (este repositorio)
- **[Manuel]** — API REST con FastAPI y MySQL

---

## Enlaces útiles

- Repositorio backend: `https://github.com/Mauelm1109/Reservas-turisticas-Back-End.git`
- Documentación de Reflex: https://reflex.dev/docs
- Documentación de FastAPI: https://fastapi.tiangolo.com
- Python 3.10+: https://www.python.org
