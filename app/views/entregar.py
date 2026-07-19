# =============================================================================
# entregar.py
# Tintorería Laredo — Pantalla F2: Entregar Prendas
#
# Layout:
#   ┌─────────────────────────────────────────────────────┐
#   │  Header                                             │
#   ├──────────────────┬──────────────────────────────────┤
#   │  Search panel    │  Customer table                  │
#   │  (left column)   │  Pending orders table            │
#   ├──────────────────┴──────────────────────────────────┤
#   │  Bottom bar: Entregar | Cancelar | Cerrar           │
#   └─────────────────────────────────────────────────────┘
# =============================================================================

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

from app.views.base_view import BaseView
from app import config as C
from app import demo_data as D


class EntregarView(BaseView):

    def _build_ui(self):
        self._build_header()
        self._build_body()
        self._build_bottom_bar()

    # ── Header ────────────────────────────────────────────────────────────────

    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color=C.HEADER_BG, corner_radius=0, height=C.HEADER_HEIGHT)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        ctk.CTkFrame(header, fg_color=C.HEADER_BORDER, height=1, corner_radius=0).pack(
            side="bottom", fill="x"
        )

        # Back button
        back_btn = ctk.CTkButton(
            header,
            text="← Volver",
            command=lambda: self.navigate("dashboard"),
            fg_color="transparent",
            hover_color=C.CONTENT_BG,
            text_color=C.BTN_PRIMARY_BG,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
            width=80,
            height=32,
        )
        back_btn.pack(side="left", padx=C.PAD_MD)

        ctk.CTkLabel(
            header,
            text="F2 — Entregar Prendas",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=17, weight="bold"),
            text_color=C.TEXT_PRIMARY,
        ).pack(side="left", padx=(0, C.PAD_LG))

        ctk.CTkLabel(
            header,
            text="  MODO DEMO  ",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            fg_color=C.DEMO_BANNER_BG,
            text_color=C.DEMO_BANNER_TEXT,
            corner_radius=10,
        ).pack(side="right", padx=C.PAD_LG)

    # ── Body (search panel + tables) ──────────────────────────────────────────

    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=C.CONTENT_BG, corner_radius=0)
        body.pack(fill="both", expand=True, padx=C.PAD_LG, pady=C.PAD_MD)

        # Left column: search controls
        left = ctk.CTkFrame(
            body,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
            width=240,
        )
        left.pack(side="left", fill="y", padx=(0, C.PAD_MD))
        left.pack_propagate(False)

        self._build_search_panel(left)

        # Right column: customer table + pending orders table
        right = ctk.CTkFrame(body, fg_color="transparent")
        right.pack(side="left", fill="both", expand=True)

        self._build_customer_table(right)
        self._build_orders_table(right)

    # ── Search panel (left) ───────────────────────────────────────────────────

    def _build_search_panel(self, parent):
        ctk.CTkLabel(
            parent,
            text="BÚSQUEDA",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))

        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=(C.PAD_SM, C.PAD_MD)
        )

        # Search input
        ctk.CTkLabel(
            parent,
            text="Buscar:",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
            text_color=C.TEXT_SECONDARY,
        ).pack(anchor="w", padx=C.PAD_MD)

        self.search_var = tk.StringVar()
        self.search_entry = ctk.CTkEntry(
            parent,
            textvariable=self.search_var,
            width=200,
            height=32,
            placeholder_text="Escribir y pulsar Enter…",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
            fg_color=C.PANEL_BG,
            border_color=C.BTN_PRIMARY_BG,
            text_color=C.TEXT_PRIMARY,
        )
        self.search_entry.pack(padx=C.PAD_MD, pady=(C.PAD_XS, C.PAD_MD))
        self.search_entry.bind("<Return>", self._do_search)

        # Search by radio group
        ctk.CTkLabel(
            parent,
            text="Buscar por:",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10, weight="bold"),
            text_color=C.TEXT_SECONDARY,
        ).pack(anchor="w", padx=C.PAD_MD)

        self.search_by = tk.StringVar(value="recogida")
        search_options = [
            ("Recogida Nº",  "recogida"),
            ("Teléfono",     "telefono"),
            ("Apellidos",    "apellidos"),
        ]
        for lbl, val in search_options:
            rb = ctk.CTkRadioButton(
                parent,
                text=lbl,
                variable=self.search_by,
                value=val,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
                text_color=C.TEXT_PRIMARY,
                fg_color=C.BTN_PRIMARY_BG,
            )
            rb.pack(anchor="w", padx=C.PAD_LG, pady=(C.PAD_XS, 0))

        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_MD
        )

        # Search button
        self.make_btn(
            parent, "🔍  Buscar", self._do_search,
            style="primary", width=200, height=36,
        ).pack(padx=C.PAD_MD)

        # Quick demo shortcut
        ctk.CTkLabel(
            parent,
            text="(Demo: cualquier búsqueda\nmuestra datos de ejemplo)",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9),
            text_color=C.TEXT_MUTED,
            justify="center",
        ).pack(pady=(C.PAD_SM, 0))

    # ── Customer results table ─────────────────────────────────────────────────

    def _build_customer_table(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        card.pack(fill="x", pady=(0, C.PAD_MD))

        hdr = ctk.CTkFrame(card, fg_color="transparent")
        hdr.pack(fill="x", padx=C.PAD_MD, pady=(C.PAD_MD, C.PAD_SM))
        ctk.CTkLabel(
            hdr,
            text="CLIENTES ENCONTRADOS",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10, weight="bold"),
            text_color=C.TEXT_SECONDARY,
        ).pack(side="left")

        ctk.CTkFrame(card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(fill="x")

        columns = [
            {"id": "codigo",    "label": "Código",    "width": 70,  "anchor": "w"},
            {"id": "nombre",    "label": "Nombre",    "width": 90,  "anchor": "w"},
            {"id": "apellido1", "label": "Apellido 1","width": 100, "anchor": "w", "stretch": True},
            {"id": "apellido2", "label": "Apellido 2","width": 100, "anchor": "w"},
            {"id": "telefono",  "label": "Teléfono",  "width": 100, "anchor": "center"},
            {"id": "direccion", "label": "Dirección", "width": 180, "anchor": "w", "stretch": True},
        ]

        tbl_frame, self.customer_tree = self.make_table(card, columns, height=4)
        tbl_frame.pack(fill="x", padx=C.PAD_MD, pady=C.PAD_SM)
        self.customer_tree.bind("<<TreeviewSelect>>", self._on_customer_select)

        # Pre-populate in demo mode
        if self.state.demo_mode:
            self._load_customers(D.CUSTOMERS)

    # ── Pending orders table ───────────────────────────────────────────────────

    def _build_orders_table(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        card.pack(fill="both", expand=True)

        hdr = ctk.CTkFrame(card, fg_color="transparent")
        hdr.pack(fill="x", padx=C.PAD_MD, pady=(C.PAD_MD, C.PAD_SM))
        ctk.CTkLabel(
            hdr,
            text="RECOGIDAS PENDIENTES DEL CLIENTE",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10, weight="bold"),
            text_color=C.TEXT_SECONDARY,
        ).pack(side="left")

        ctk.CTkFrame(card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(fill="x")

        columns = [
            {"id": "recogida",  "label": "Recogida",  "width": 120, "anchor": "w"},
            {"id": "fecha",     "label": "Fecha",     "width": 90,  "anchor": "center"},
            {"id": "pendiente", "label": "Estado",    "width": 90,  "anchor": "center"},
            {"id": "importe",   "label": "Importe",   "width": 90,  "anchor": "e"},
        ]

        tbl_frame, self.orders_tree = self.make_table(card, columns, height=8)
        tbl_frame.pack(fill="both", expand=True, padx=C.PAD_MD, pady=C.PAD_SM)

        # Pre-populate in demo mode
        if self.state.demo_mode:
            self._load_orders_for_all()

    # ── Data loading helpers ───────────────────────────────────────────────────

    def _load_customers(self, customers: list):
        rows = [
            (
                c["codigo"],
                c["nombre"],
                c["apellido1"],
                c["apellido2"],
                c["telefono"],
                c["direccion"],
            )
            for c in customers
        ]
        self.populate_table(self.customer_tree, rows)

    def _load_orders_for_all(self):
        rows = []
        for i, o in enumerate(D.ORDERS):
            tag = "odd" if i % 2 == 0 else "even"
            rows.append((
                o["recogida"],
                o["fecha"],
                o["pendiente"],
                o["importe"],
            ))
        self.populate_table(self.orders_tree, rows)

        # Apply status colouring
        for i, child in enumerate(self.orders_tree.get_children()):
            estado = D.ORDERS[i]["pendiente"]
            existing = self.orders_tree.item(child, "tags")
            if estado == "Pendiente":
                self.orders_tree.item(child, tags=existing + ("pending",))
            elif estado == "Listo":
                self.orders_tree.item(child, tags=existing + ("ready",))
            elif estado == "Parcial":
                self.orders_tree.item(child, tags=existing + ("partial",))

    def _load_orders_for_customer(self, codigo: str):
        matching = [o for o in D.ORDERS if o["cliente"] == codigo]
        if not matching:
            # Demo fallback: show all orders
            matching = D.ORDERS
        rows = [(o["recogida"], o["fecha"], o["pendiente"], o["importe"]) for o in matching]
        self.populate_table(self.orders_tree, rows)

    # ── Event handlers ────────────────────────────────────────────────────────

    def _do_search(self, event=None):
        query = self.search_var.get().strip()
        # Demo: always show all customers regardless of query
        self._load_customers(D.CUSTOMERS)
        self._load_orders_for_all()

    def _on_customer_select(self, event=None):
        sel = self.customer_tree.selection()
        if not sel:
            return
        values = self.customer_tree.item(sel[0], "values")
        codigo = values[0]
        self._load_orders_for_customer(codigo)

    # ── Bottom bar ────────────────────────────────────────────────────────────

    def _build_bottom_bar(self):
        bar = ctk.CTkFrame(
            self,
            fg_color=C.PANEL_BG,
            corner_radius=0,
            height=50,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        bar.pack(fill="x", side="bottom")
        bar.pack_propagate(False)

        self.make_btn(
            bar, "✔  Entregar",
            lambda: self.not_implemented("Entregar Prendas"),
            style="success", width=140,
        ).pack(side="left", padx=C.PAD_MD, pady=C.PAD_SM)

        self.make_btn(
            bar, "🖨  Reimprimir",
            lambda: self.navigate("reimprimir"),
            style="secondary", width=140,
        ).pack(side="left", padx=(0, C.PAD_MD), pady=C.PAD_SM)

        self.make_btn(
            bar, "✖  Cerrar",
            lambda: self.navigate("dashboard"),
            style="neutral", width=110,
        ).pack(side="right", padx=C.PAD_MD, pady=C.PAD_SM)

    # ── on_show: refresh for demo mode ────────────────────────────────────────

    def on_show(self):
        self.controller.bind("<Escape>", lambda e: self.navigate("dashboard"))
        if self.state.demo_mode:
            self._load_customers(D.CUSTOMERS)
            self._load_orders_for_all()
