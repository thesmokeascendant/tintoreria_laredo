# =============================================================================
# dashboard.py
# Tintorería Laredo — Main Dashboard (Procesos Diarios)
#
# Layout:
#   ┌─────────────────────────────────────────────────────┐
#   │  Header bar: title + demo badge                     │
#   ├─────────────────────────────────────────────────────┤
#   │  Stats row: 4 KPI cards                             │
#   ├─────────────────────────────────────────────────────┤
#   │  Main action buttons: F1 / F2 / F3                  │
#   ├─────────────────────────────────────────────────────┤
#   │  Pending orders table (today's queue)               │
#   ├─────────────────────────────────────────────────────┤
#   │  Bottom bar: Copias | Finalizar                     │
#   └─────────────────────────────────────────────────────┘
# =============================================================================

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from app.views.base_view import BaseView
from app import config as C
from app import demo_data as D


class DashboardView(BaseView):

    def _build_ui(self):
        self._build_header()
        self._build_stats_row()
        self._build_action_buttons()
        self._build_orders_panel()
        self._build_bottom_bar()

    # ── Header ────────────────────────────────────────────────────────────────

    def _build_header(self):
        header = ctk.CTkFrame(self, fg_color=C.HEADER_BG, corner_radius=0, height=C.HEADER_HEIGHT)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        # Thin bottom border
        border = ctk.CTkFrame(header, fg_color=C.HEADER_BORDER, height=1, corner_radius=0)
        border.pack(side="bottom", fill="x")

        # Title
        ctk.CTkLabel(
            header,
            text="Procesos Diarios",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=17, weight="bold"),
            text_color=C.TEXT_PRIMARY,
        ).pack(side="left", padx=C.PAD_LG, anchor="w")

        # Date indicator
        ctk.CTkLabel(
            header,
            text="Martes, 09 de Junio de 2026",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
            text_color=C.TEXT_MUTED,
        ).pack(side="left", padx=(0, C.PAD_LG), anchor="w")

        # Demo badge (right side)
        demo_lbl = ctk.CTkLabel(
            header,
            text="  MODO DEMO  ",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            fg_color=C.DEMO_BANNER_BG,
            text_color=C.DEMO_BANNER_TEXT,
            corner_radius=10,
        )
        demo_lbl.pack(side="right", padx=C.PAD_LG, anchor="e")

    # ── KPI stats row ─────────────────────────────────────────────────────────

    def _build_stats_row(self):
        row = ctk.CTkFrame(self, fg_color=C.CONTENT_BG, corner_radius=0)
        row.pack(fill="x", padx=C.PAD_LG, pady=(C.PAD_MD, 0))

        stats = [
            ("Recogidas hoy",    str(D.DASHBOARD_STATS["recogidas_hoy"]),   C.BTN_PRIMARY_BG),
            ("Entregas hoy",     str(D.DASHBOARD_STATS["entregas_hoy"]),    C.BTN_SUCCESS_BG),
            ("Pendientes",       str(D.DASHBOARD_STATS["pendientes"]),      "#D97706"),
            ("Facturación mes",  D.DASHBOARD_STATS["facturacion_mes"],      "#0891B2"),
        ]

        for i, (label, value, accent) in enumerate(stats):
            card = ctk.CTkFrame(
                row,
                fg_color=C.PANEL_BG,
                corner_radius=C.RADIUS_MD,
                border_width=1,
                border_color=C.PANEL_BORDER,
                height=80,
            )
            card.grid(row=0, column=i, padx=(0 if i == 0 else C.PAD_SM, 0), sticky="ew")
            card.grid_propagate(False)
            row.grid_columnconfigure(i, weight=1)

            # Left accent stripe
            stripe = ctk.CTkFrame(card, fg_color=accent, width=5, corner_radius=0)
            stripe.pack(side="left", fill="y")

            inner = ctk.CTkFrame(card, fg_color="transparent")
            inner.pack(side="left", padx=C.PAD_MD, pady=C.PAD_SM)

            ctk.CTkLabel(
                inner,
                text=value,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=24, weight="bold"),
                text_color=accent,
            ).pack(anchor="w")

            ctk.CTkLabel(
                inner,
                text=label,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
                text_color=C.TEXT_SECONDARY,
            ).pack(anchor="w")

    # ── F-key action buttons ──────────────────────────────────────────────────

    def _build_action_buttons(self):
        panel = ctk.CTkFrame(
            self,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        panel.pack(fill="x", padx=C.PAD_LG, pady=C.PAD_MD)

        # Section label
        ctk.CTkLabel(
            panel,
            text="ACCIONES RÁPIDAS",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, C.PAD_SM))

        btn_row = ctk.CTkFrame(panel, fg_color="transparent")
        btn_row.pack(fill="x", padx=C.PAD_MD, pady=(0, C.PAD_MD))

        self._make_fkey_btn(btn_row, "F1", "Recoger Prendas",
                            "📥", "recoger", "F1")
        self._make_fkey_btn(btn_row, "F2", "Entregar Prendas",
                            "📦", "entregar", "F2")
        self._make_fkey_btn(btn_row, "F3", "Reimprimir Recogida",
                            "🖨️", "reimprimir", "F3")

    def _make_fkey_btn(self, parent, key, label, icon, view_name, fkey):
        bg, hover = C.FKEY_COLORS[key]

        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(side="left", padx=(0, C.PAD_MD))

        btn = ctk.CTkButton(
            frame,
            text=f"  {icon}  {label}",
            command=lambda v=view_name: self.navigate(v),
            fg_color=bg,
            hover_color=hover,
            text_color="#FFFFFF",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=13, weight="bold"),
            width=200,
            height=52,
            corner_radius=C.RADIUS_MD,
        )
        btn.pack()

        # Key hint label below button
        ctk.CTkLabel(
            frame,
            text=f"Tecla {fkey}",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9),
            text_color=C.TEXT_MUTED,
        ).pack(pady=(3, 0))

        # Bind the actual F-key globally on parent window
        self.controller.bind(f"<{fkey}>", lambda e, v=view_name: self.navigate(v))

    # ── Today's pending orders table ──────────────────────────────────────────

    def _build_orders_panel(self):
        panel = ctk.CTkFrame(
            self,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        panel.pack(fill="both", expand=True, padx=C.PAD_LG, pady=(0, C.PAD_MD))

        # Panel header row
        hdr = ctk.CTkFrame(panel, fg_color="transparent")
        hdr.pack(fill="x", padx=C.PAD_MD, pady=(C.PAD_MD, C.PAD_SM))

        ctk.CTkLabel(
            hdr,
            text="RECOGIDAS PENDIENTES — HOY",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10, weight="bold"),
            text_color=C.TEXT_SECONDARY,
        ).pack(side="left")

        ctk.CTkLabel(
            hdr,
            text=f"  {len(D.ORDERS)} registros  ",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            fg_color=C.BTN_SECONDARY_BG,
            text_color=C.BTN_SECONDARY_TEXT,
            corner_radius=10,
        ).pack(side="right")

        sep = ctk.CTkFrame(panel, fg_color=C.PANEL_BORDER, height=1, corner_radius=0)
        sep.pack(fill="x")

        # Table
        columns = [
            {"id": "recogida", "label": "Nº Recogida",  "width": 120, "anchor": "w"},
            {"id": "fecha",    "label": "Fecha",         "width": 90,  "anchor": "center"},
            {"id": "cliente",  "label": "Cliente",       "width": 180, "anchor": "w", "stretch": True},
            {"id": "prendas",  "label": "Prendas",       "width": 70,  "anchor": "center"},
            {"id": "pendiente","label": "Estado",        "width": 90,  "anchor": "center"},
            {"id": "importe",  "label": "Importe",       "width": 90,  "anchor": "e"},
            {"id": "notas",    "label": "Observaciones", "width": 200, "anchor": "w", "stretch": True},
        ]

        tbl_frame, self.orders_tree = self.make_table(panel, columns, height=10)
        tbl_frame.pack(fill="both", expand=True, padx=C.PAD_MD, pady=C.PAD_SM)

        # Populate
        rows = []
        for o in D.ORDERS:
            rows.append((
                o["recogida"],
                o["fecha"],
                o["nombre"],
                str(o["prendas"]),
                o["pendiente"],
                o["importe"],
                o["notas"],
            ))
        self.populate_table(self.orders_tree, rows)

        # Colour-code the Estado column via row tags
        for i, child in enumerate(self.orders_tree.get_children()):
            estado = D.ORDERS[i]["pendiente"]
            existing_tags = self.orders_tree.item(child, "tags")
            if estado == "Pendiente":
                self.orders_tree.item(child, tags=existing_tags + ("pending",))
            elif estado == "Listo":
                self.orders_tree.item(child, tags=existing_tags + ("ready",))
            elif estado == "Parcial":
                self.orders_tree.item(child, tags=existing_tags + ("partial",))

    # ── Bottom action bar ─────────────────────────────────────────────────────

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
            bar, "  Copias", lambda: self.not_implemented("Copias"),
            style="neutral", width=110
        ).pack(side="left", padx=C.PAD_MD, pady=C.PAD_SM)

        self.make_btn(
            bar, "  Finalizar", self.controller.quit_app,
            style="danger", width=110
        ).pack(side="right", padx=C.PAD_MD, pady=C.PAD_SM)

    # ── Keyboard shortcut wiring ──────────────────────────────────────────────

    def on_show(self):
        # Re-bind F-keys each time the dashboard is shown
        self.controller.bind("<F1>", lambda e: self.navigate("recoger"))
        self.controller.bind("<F2>", lambda e: self.navigate("entregar"))
        self.controller.bind("<F3>", lambda e: self.navigate("reimprimir"))
