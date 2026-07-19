# =============================================================================
# demo_data.py
# Tintorería Laredo — All fake demonstration data lives here.
# UI code imports from this module — no data is hardcoded in views.
# =============================================================================

# ── Customers ─────────────────────────────────────────────────────────────────
CUSTOMERS = [
    {
        "codigo":    "C-0041",
        "nombre":    "Alejandro",
        "apellido1": "Martínez",
        "apellido2": "Ruiz",
        "telefono":  "612 345 678",
        "direccion": "C/ Gran Vía 18, 2ºB",
    },
    {
        "codigo":    "C-0087",
        "nombre":    "Carmen",
        "apellido1": "López",
        "apellido2": "Fernández",
        "telefono":  "689 012 345",
        "direccion": "Av. Constitución 5, 1ºA",
    },
    {
        "codigo":    "C-0112",
        "nombre":    "Fernando",
        "apellido1": "García",
        "apellido2": "Moreno",
        "telefono":  "654 789 012",
        "direccion": "C/ Cervantes 34, Bajo",
    },
    {
        "codigo":    "C-0158",
        "nombre":    "Isabel",
        "apellido1": "Sánchez",
        "apellido2": "Díaz",
        "telefono":  "677 234 567",
        "direccion": "Pz. Mayor 7, 3ºC",
    },
    {
        "codigo":    "C-0203",
        "nombre":    "Roberto",
        "apellido1": "Torres",
        "apellido2": "Jiménez",
        "telefono":  "698 901 234",
        "direccion": "C/ Rosalía de Castro 12",
    },
    {
        "codigo":    "C-0251",
        "nombre":    "María",
        "apellido1": "Vega",
        "apellido2": "Castillo",
        "telefono":  "611 456 789",
        "direccion": "Av. Libertad 3, 4ºD",
    },
    {
        "codigo":    "C-0309",
        "nombre":    "Javier",
        "apellido1": "Romero",
        "apellido2": "Navarro",
        "telefono":  "633 890 123",
        "direccion": "C/ Lope de Vega 21, 2ºA",
    },
]

# ── Pending orders (linked loosely to customers above) ────────────────────────
ORDERS = [
    {
        "recogida": "R-2024-0891",
        "fecha":    "08/06/2026",
        "cliente":  "C-0041",
        "nombre":   "Alejandro Martínez",
        "pendiente":"Pendiente",
        "importe":  "38,50 €",
        "prendas":  5,
        "notas":    "Traje gris con manchas aceite. Urgente.",
    },
    {
        "recogida": "R-2024-0892",
        "fecha":    "08/06/2026",
        "cliente":  "C-0087",
        "nombre":   "Carmen López",
        "pendiente":"Listo",
        "importe":  "22,00 €",
        "prendas":  3,
        "notas":    "",
    },
    {
        "recogida": "R-2024-0893",
        "fecha":    "09/06/2026",
        "cliente":  "C-0112",
        "nombre":   "Fernando García",
        "pendiente":"Pendiente",
        "importe":  "61,00 €",
        "prendas":  7,
        "notas":    "Abrigo de lana — tratamiento especial.",
    },
    {
        "recogida": "R-2024-0894",
        "fecha":    "09/06/2026",
        "cliente":  "C-0158",
        "nombre":   "Isabel Sánchez",
        "pendiente":"Parcial",
        "importe":  "15,50 €",
        "prendas":  2,
        "notas":    "",
    },
    {
        "recogida": "R-2024-0895",
        "fecha":    "10/06/2026",
        "cliente":  "C-0203",
        "nombre":   "Roberto Torres",
        "pendiente":"Pendiente",
        "importe":  "47,75 €",
        "prendas":  6,
        "notas":    "Cliente VIP — llamar al recoger.",
    },
    {
        "recogida": "R-2024-0896",
        "fecha":    "10/06/2026",
        "cliente":  "C-0251",
        "nombre":   "María Vega",
        "pendiente":"Listo",
        "importe":  "9,00 €",
        "prendas":  1,
        "notas":    "",
    },
    {
        "recogida": "R-2024-0897",
        "fecha":    "11/06/2026",
        "cliente":  "C-0309",
        "nombre":   "Javier Romero",
        "pendiente":"Pendiente",
        "importe":  "83,00 €",
        "prendas":  9,
        "notas":    "Bodas: vestido novia + 2 trajes.",
    },
]

# ── Garments catalogue (for Recoger Prendas) ─────────────────────────────────
GARMENT_CATALOGUE = [
    "Traje completo",
    "Chaqueta",
    "Pantalón",
    "Camisa",
    "Corbata",
    "Vestido",
    "Falda",
    "Blusa",
    "Abrigo",
    "Anorak / Cazadora",
    "Jersey / Suéter",
    "Camiseta",
    "Terno (3 piezas)",
    "Esmoquin",
    "Vestido de novia",
    "Traje de comunión",
    "Mantón / Chal",
    "Pañuelo de seda",
    "Bufanda",
    "Guantes",
    "Bolso / Cartera",
    "Zapatos (par)",
    "Cinturón",
    "Manta / Colcha",
    "Nórdico / Edredón",
    "Almohada",
    "Sábana (juego)",
    "Mantel",
    "Servilletas (jgo.)",
    "Cortina (ud.)",
    "Tapicería (ud.)",
    "Peluche / Muñeco",
]

# Pre-filled garments for the Recoger demo screen
DEMO_GARMENTS = [
    {"ud": 1, "prenda": "Traje completo",   "color": "Gris Oxford",  "proceso": "Limpieza en seco", "precio": "22,00 €", "obs": "Manchas aceite solapa"},
    {"ud": 1, "prenda": "Camisa",           "color": "Blanco",       "proceso": "Lavado y planchado","precio":  "5,50 €", "obs": ""},
    {"ud": 1, "prenda": "Corbata",          "color": "Azul marino",  "proceso": "Limpieza en seco", "precio":  "6,00 €", "obs": "Nudo muy apretado"},
    {"ud": 2, "prenda": "Pantalón",         "color": "Negro",        "proceso": "Lavado y planchado","precio":  "9,00 €", "obs": ""},
    {"ud": 1, "prenda": "Abrigo",           "color": "Camel",        "proceso": "Limpieza en seco", "precio": "18,00 €", "obs": "Tratar con cuidado: lana"},
]

# ── Dashboard stats (totals bar) ──────────────────────────────────────────────
DASHBOARD_STATS = {
    "recogidas_hoy":  14,
    "entregas_hoy":    9,
    "pendientes":     37,
    "facturacion_mes": "3.842,50 €",
}

# ── Sidebar navigation items ──────────────────────────────────────────────────
SIDEBAR_ITEMS = [
    ("📋", "Procesos Diarios",  "dashboard"),
    ("⚖️",  "Carga de Trabajo", "not_implemented"),
    ("🔍", "Consultas",         "not_implemented"),
    ("🧾", "Facturación",       "not_implemented"),
    ("📄", "Listados",          "not_implemented"),
    ("📊", "Estadísticas",      "not_implemented"),
    ("🔧", "Utilidades",        "not_implemented"),
    ("🏢", "Empresas",          "not_implemented"),
    ("🚪", "Salir",             "quit"),
]

# ── Next recogida number (auto-increment simulation) ──────────────────────────
NEXT_RECOGIDA = "R-2024-0898"

# ── Delivery date suggestion (T + 3 working days) ─────────────────────────────
DELIVERY_DATE = "12/06/2026"
