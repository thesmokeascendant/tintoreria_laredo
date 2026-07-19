# =============================================================================
# recoger.py
# Tintorería Laredo — Pantalla F1: Recoger Prendas
#
# Layout (two columns):
#   ┌──────────────────────────┬──────────────────────────┐
#   │  LEFT                    │  RIGHT                   │
#   │  • Customer card         │  • Garment table         │
#   │  • Delivery date / notes │  • Add / Remove buttons  │
#   │                          │  • Pricing summary       │
#   ├──────────────────────────┴──────────────────────────┤
#   │  Bottom bar: Guardar | Cobrar | Imprimir | Cancelar │
#   └─────────────────────────────────────────────────────┘
# =============================================================================

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk

from app.views.base_view import BaseView
from app import config as C
from app import demo_data as D


class RecogerView(BaseView):

    def _build_ui(self):
        self._garments = list(D.DEMO_GARMENTS)  # working copy for this session
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

        ctk.CTkButton(
            header,
            text="← Volver",
            command=lambda: self.navigate("dashboard"),
            fg_color="transparent",
            hover_color=C.CONTENT_BG,
            text_color=C.BTN_PRIMARY_BG,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
            width=80,
            height=32,
        ).pack(side="left", padx=C.PAD_MD)

        ctk.CTkLabel(
            header,
            text="F1 — Recoger Prendas",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=17, weight="bold"),
            text_color=C.TEXT_PRIMARY,
        ).pack(side="left", padx=(0, C.PAD_LG))

        # Recogida number badge
        ctk.CTkLabel(
            header,
            text=f"  Nº {D.NEXT_RECOGIDA}  ",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
            fg_color=C.BTN_PRIMARY_BG,
            text_color="#FFFFFF",
            corner_radius=C.RADIUS_SM,
        ).pack(side="left", padx=(0, C.PAD_MD))

        ctk.CTkLabel(
            header,
            text="  MODO DEMO  ",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            fg_color=C.DEMO_BANNER_BG,
            text_color=C.DEMO_BANNER_TEXT,
            corner_radius=10,
        ).pack(side="right", padx=C.PAD_LG)

    # ── Body ──────────────────────────────────────────────────────────────────

    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=C.CONTENT_BG, corner_radius=0)
        body.pack(fill="both", expand=True, padx=C.PAD_LG, pady=C.PAD_MD)

        # Left column
        left = ctk.CTkFrame(body, fg_color="transparent", width=310)
        left.pack(side="left", fill="y", padx=(0, C.PAD_MD))
        left.pack_propagate(False)

        self._build_customer_card(left)
        self._build_delivery_card(left)
        self._build_notes_card(left)
        self._build_print_options_card(left)

        # Right column
        right = ctk.CTkFrame(body, fg_color="transparent")
        right.pack(side="left", fill="both", expand=True)

        self._build_pricing_card(right)
        self._build_garment_table(right)

    # ── Customer card (left) ──────────────────────────────────────────────────

    def _build_customer_card(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        card.pack(fill="x", pady=(0, C.PAD_SM))

        ctk.CTkLabel(
            card,
            text="DATOS DEL CLIENTE",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))
        ctk.CTkFrame(card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        inner = ctk.CTkFrame(card, fg_color="transparent")
        inner.pack(fill="x", padx=C.PAD_MD, pady=(0, C.PAD_MD))

        cust = D.CUSTOMERS[0]  # Demo customer

        def field(lbl, val):
            f = ctk.CTkFrame(inner, fg_color="transparent")
            f.pack(fill="x", pady=2)
            ctk.CTkLabel(
                f, text=lbl,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=9),
                text_color=C.TEXT_MUTED, width=80, anchor="w",
            ).pack(side="left")
            ctk.CTkLabel(
                f, text=val,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
                text_color=C.TEXT_PRIMARY, anchor="w",
            ).pack(side="left")

        field("Código:",    cust["codigo"])
        field("Nombre:",    f"{cust['nombre']} {cust['apellido1']} {cust['apellido2']}")
        field("Teléfono:",  cust["telefono"])
        field("Dirección:", cust["direccion"])

        # Change customer button
        ctk.CTkButton(
            card,
            text="🔄  Cambiar cliente",
            command=lambda: self.not_implemented("Cambiar Cliente"),
            fg_color=C.BTN_SECONDARY_BG,
            hover_color=C.BTN_SECONDARY_HOVER,
            text_color=C.BTN_SECONDARY_TEXT,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
            height=28,
            corner_radius=C.RADIUS_SM,
        ).pack(padx=C.PAD_MD, pady=(0, C.PAD_MD), anchor="w")

    # ── Delivery date card ────────────────────────────────────────────────────

    def _build_delivery_card(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        card.pack(fill="x", pady=(0, C.PAD_SM))

        ctk.CTkLabel(
            card,
            text="FECHA DE ENTREGA",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))
        ctk.CTkFrame(card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        row = ctk.CTkFrame(card, fg_color="transparent")
        row.pack(fill="x", padx=C.PAD_MD, pady=(0, C.PAD_MD))

        self.delivery_var = tk.StringVar(value=D.DELIVERY_DATE)
        delivery_entry = ctk.CTkEntry(
            row,
            textvariable=self.delivery_var,
            width=140,
            height=34,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=12, weight="bold"),
            fg_color=C.PANEL_BG,
            border_color=C.BTN_PRIMARY_BG,
            text_color=C.TEXT_PRIMARY,
        )
        delivery_entry.pack(side="left")

        ctk.CTkLabel(
            row,
            text="  (dd/mm/aaaa)",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9),
            text_color=C.TEXT_MUTED,
        ).pack(side="left")

        # Urgente checkbox
        self.urgente_var = tk.BooleanVar(value=False)
        ctk.CTkCheckBox(
            card,
            text="⚡  Urgente",
            variable=self.urgente_var,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
            text_color="#DC2626",
            fg_color="#DC2626",
            hover_color="#B91C1C",
            checkmark_color="#FFFFFF",
        ).pack(anchor="w", padx=C.PAD_MD, pady=(0, C.PAD_MD))

    # ── Notes card ────────────────────────────────────────────────────────────

    def _build_notes_card(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        card.pack(fill="x", pady=(0, C.PAD_SM))

        ctk.CTkLabel(
            card,
            text="OBSERVACIONES",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))
        ctk.CTkFrame(card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        self.notes_text = ctk.CTkTextbox(
            card,
            width=270,
            height=70,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
            fg_color="#F8FAFC",
            border_color=C.PANEL_BORDER,
            border_width=1,
            text_color=C.TEXT_PRIMARY,
        )
        self.notes_text.pack(padx=C.PAD_MD, pady=(0, C.PAD_MD))
        self.notes_text.insert("1.0", "Traje gris con manchas aceite. Urgente.")

    # ── Print options card ────────────────────────────────────────────────────

    def _build_print_options_card(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        card.pack(fill="x", pady=(0, C.PAD_SM))

        ctk.CTkLabel(
            card,
            text="OPCIONES DE IMPRESIÓN",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))
        ctk.CTkFrame(card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        self.print_cliente_var = tk.BooleanVar(value=True)
        self.print_prendas_var = tk.BooleanVar(value=True)

        for var, text in [
            (self.print_cliente_var, "Ticket del Cliente"),
            (self.print_prendas_var, "Ticket de las Prendas"),
        ]:
            ctk.CTkCheckBox(
                card,
                text=text,
                variable=var,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
                text_color=C.TEXT_PRIMARY,
                fg_color=C.BTN_PRIMARY_BG,
                checkmark_color="#FFFFFF",
            ).pack(anchor="w", padx=C.PAD_LG, pady=(C.PAD_XS, 0))

        ctk.CTkFrame(card, fg_color="transparent", height=C.PAD_SM).pack()

    # ── Garment table (right) ─────────────────────────────────────────────────

    def _build_garment_table(self, parent):
        card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        card.pack(fill="both", expand=True, pady=(0, C.PAD_SM))

        # Table header row with buttons
        hdr = ctk.CTkFrame(card, fg_color="transparent")
        hdr.pack(fill="x", padx=C.PAD_MD, pady=(C.PAD_MD, C.PAD_SM))

        ctk.CTkLabel(
            hdr,
            text="PRENDAS",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10, weight="bold"),
            text_color=C.TEXT_SECONDARY,
        ).pack(side="left")

        # Remove button
        self.make_btn(
            hdr, "➖  Eliminar",
            self._remove_garment,
            style="danger", width=110, height=28,
        ).pack(side="right", padx=(C.PAD_SM, 0))

        # Add button
        self.make_btn(
            hdr, "➕  Añadir",
            self._add_garment,
            style="success", width=110, height=28,
        ).pack(side="right")

        ctk.CTkFrame(card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(fill="x")

        columns = [
            {"id": "ud",      "label": "Ud.",      "width": 35,  "anchor": "center"},
            {"id": "prenda",  "label": "Prenda",   "width": 160, "anchor": "w", "stretch": True},
            {"id": "color",   "label": "Color",    "width": 100, "anchor": "w"},
            {"id": "proceso", "label": "Proceso",  "width": 140, "anchor": "w"},
            {"id": "precio",  "label": "Precio",   "width": 75,  "anchor": "e"},
            {"id": "obs",     "label": "Obs.",     "width": 160, "anchor": "w", "stretch": True},
        ]

        tbl_frame, self.garment_tree = self.make_table(card, columns, height=12)
        tbl_frame.pack(fill="both", expand=True, padx=C.PAD_MD, pady=C.PAD_SM)

        self._refresh_garment_table()

    def _refresh_garment_table(self):
        rows = [
            (g["ud"], g["prenda"], g["color"], g["proceso"], g["precio"], g["obs"])
            for g in self._garments
        ]
        self.populate_table(self.garment_tree, rows)
        self._refresh_pricing()

    def _add_garment(self):
        self.not_implemented("Añadir Prenda")

    def _remove_garment(self):
        sel = self.garment_tree.selection()
        if not sel:
            messagebox.showwarning("Aviso", "Seleccione una prenda para eliminar.", parent=self)
            return
        idx = self.garment_tree.index(sel[0])
        if 0 <= idx < len(self._garments):
            self._garments.pop(idx)
            self._refresh_garment_table()

    # ── Pricing summary (right bottom) ────────────────────────────────────────

    def _build_pricing_card(self, parent):
        self.pricing_card = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        self.pricing_card.pack(fill="x")

        ctk.CTkLabel(
            self.pricing_card,
            text="RESUMEN ECONÓMICO",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))
        ctk.CTkFrame(
            self.pricing_card, fg_color=C.PANEL_BORDER, height=1, corner_radius=0
        ).pack(fill="x", pady=C.PAD_SM)

        self.pricing_inner = ctk.CTkFrame(self.pricing_card, fg_color="transparent")
        self.pricing_inner.pack(fill="x", padx=C.PAD_MD, pady=(0, C.PAD_MD))

        self._refresh_pricing()

    def _refresh_pricing(self):

        if not hasattr(self, "pricing_inner"):
            return
            
        # Clear previous pricing rows
        for w in self.pricing_inner.winfo_children():
            w.destroy()

        def price_row(lbl, val, bold=False, color=C.TEXT_PRIMARY):
            f = ctk.CTkFrame(self.pricing_inner, fg_color="transparent")
            f.pack(fill="x", pady=1)
            ctk.CTkLabel(
                f, text=lbl,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
                text_color=C.TEXT_SECONDARY, anchor="w",
            ).pack(side="left", expand=True, fill="x")
            ctk.CTkLabel(
                f, text=val,
                font=ctk.CTkFont(
                    family=C.FONT_FAMILY, size=11 if not bold else 13,
                    weight="bold" if bold else "normal"
                ),
                text_color=color, anchor="e",
            ).pack(side="right")

        # Parse and sum prices (demo: strip € and commas)
        subtotal = 0.0
        for g in self._garments:
            try:
                price_str = g["precio"].replace("€", "").replace(",", ".").strip()
                subtotal += float(price_str) * int(g["ud"])
            except (ValueError, KeyError):
                pass

        iva = subtotal * 0.21
        total = subtotal + iva

        def fmt(v): return f"{v:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")

        price_row(f"Subtotal ({len(self._garments)} prendas):", fmt(subtotal))
        price_row("IVA (21%):", fmt(iva))
        ctk.CTkFrame(
            self.pricing_inner, fg_color=C.PANEL_BORDER, height=1, corner_radius=0
        ).pack(fill="x", pady=C.PAD_XS)
        price_row("TOTAL:", fmt(total), bold=True, color=C.BTN_PRIMARY_BG)

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
            bar, "💾  Guardar",
            self._save,
            style="primary", width=130,
        ).pack(side="left", padx=C.PAD_MD, pady=C.PAD_SM)

        self.make_btn(
            bar, "💳  Cobrar",
            lambda: self.not_implemented("Cobrar"),
            style="success", width=130,
        ).pack(side="left", padx=(0, C.PAD_MD), pady=C.PAD_SM)

        self.make_btn(
            bar, "🖨  Imprimir",
            lambda: self.not_implemented("Imprimir"),
            style="secondary", width=130,
        ).pack(side="left", pady=C.PAD_SM)

        self.make_btn(
            bar, "✖  Cancelar",
            lambda: self.navigate("dashboard"),
            style="neutral", width=110,
        ).pack(side="right", padx=C.PAD_MD, pady=C.PAD_SM)

    # ── Actions ───────────────────────────────────────────────────────────────

    def _save(self):
        messagebox.showinfo(
            "Versión Demo — Guardado",
            f"Recogida {D.NEXT_RECOGIDA} registrada correctamente.\n\n"
            f"Cliente: {D.CUSTOMERS[0]['nombre']} {D.CUSTOMERS[0]['apellido1']}\n"
            f"Prendas: {len(self._garments)}\n\n"
            "Versión Demo — los datos no se han almacenado en ninguna base de datos.",
            parent=self,
        )

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    def on_show(self):
        self.controller.bind("<Escape>", lambda e: self.navigate("dashboard"))
        if self.state.demo_mode:
            self._garments = list(D.DEMO_GARMENTS)
            self._refresh_garment_table()
