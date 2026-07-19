# 🧺 Tintorería Laredo — Sistema de Gestión (Prototipo Demo)

> **Prototype desktop application** for dry-cleaning / laundry management.  
> Built in Python + CustomTkinter. Intended for client demonstration purposes.

---

## Screenshots (what you will see)

| Screen | Description |
|--------|-------------|
| **Dashboard** | KPI cards, pending orders table, F1/F2/F3 action buttons |
| **Recoger Prendas** | Customer card, garment table, pricing summary, notes |
| **Entregar Prendas** | Customer search, order lookup, status badges |
| **Reimprimir Recogida** | Ticket options, live preview, checkbox controls |

---

## Quick Start (Windows)

### 1. Prerequisites

- Python 3.12 or later — https://python.org/downloads  
  ✅ During install, check **"Add Python to PATH"**

### 2. Create and activate a virtual environment

```bat
cd tintoreria_laredo
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bat
pip install -r requirements.txt
```

### 4. Run the application

```bat
python main.py
```

The window opens immediately — no database, no network required.

---

## Quick Start (macOS / Linux)

```bash
cd tintoreria_laredo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `F1` | Recoger Prendas |
| `F2` | Entregar Prendas |
| `F3` | Reimprimir Recogida |
| `Escape` | Volver al Dashboard |
| `Ctrl + D` | Toggle Demo Mode |

---

## Demo Mode

Demo mode is **ON by default**. When active:

- All screens are pre-populated with realistic sample data
- Every navigation path works and looks production-ready
- The sidebar shows a purple **MODO DEMO** badge
- Toggle via the switch at the bottom of the sidebar, or `Ctrl+D`

---

## Project Structure

```
tintoreria_laredo/
├── main.py                     # Entry point + root window + sidebar + router
├── requirements.txt
├── README.md
└── app/
    ├── config.py               # All colours, fonts, spacing — edit here
    ├── demo_data.py            # All fake data — customers, orders, garments
    ├── state.py                # Shared runtime state (demo toggle, selections)
    └── views/
        ├── base_view.py        # Base class: widget factories, navigation helper
        ├── dashboard.py        # Main dashboard (Procesos Diarios)
        ├── recoger.py          # F1: Recoger Prendas
        ├── entregar.py         # F2: Entregar Prendas
        └── reimprimir.py       # F3: Reimprimir Recogida
```

---

## Customisation

| What to change | Where |
|----------------|-------|
| Colours / fonts | `app/config.py` |
| Sample customers | `app/demo_data.py → CUSTOMERS` |
| Sample orders | `app/demo_data.py → ORDERS` |
| Garment catalogue | `app/demo_data.py → GARMENT_CATALOGUE` |
| KPI stats | `app/demo_data.py → DASHBOARD_STATS` |
| Add a new screen | Create `app/views/myview.py`, register in `main.py → _register_views()` |

---

## What is NOT implemented (demo stubs)

The following features show a **"Versión Demo"** dialog when triggered:

- Database connectivity (PostgreSQL / Access / SQLite)
- QR code generation
- Ticket printing (thermal printer / PDF)
- VeriFactu fiscal integration
- Excel / Access export
- User authentication
- Carga de Trabajo, Consultas, Facturación, Listados, Estadísticas, Utilidades, Empresas

---

## Packaging into a ZIP for delivery

**Windows (PowerShell):**

```powershell
Compress-Archive -Path .\tintoreria_laredo -DestinationPath .\tintoreria_laredo_demo.zip
```

**macOS / Linux:**

```bash
zip -r tintoreria_laredo_demo.zip tintoreria_laredo/
```

Deliver the ZIP with this README. The recipient needs only Python 3.12+ installed.

---

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `customtkinter` | 5.2.2 | Modern Tkinter widget library |

CustomTkinter brings in `darkdetect` automatically — no other dependencies.

---

*Prototipo desarrollado para demostración comercial. Versión 1.0.*
