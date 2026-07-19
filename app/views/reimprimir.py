# =============================================================================
# reimprimir.py
# Tintorería Laredo — Pantalla F3: Reimprimir Recogida
#
# Layout:
#   ┌─────────────────────────────────────────────────────┐
#   │  Header                                             │
#   ├──────────────────────┬──────────────────────────────┤
#   │  Input panel         │  Preview card                │
#   │  • Nº Recogida       │  • Customer info             │
#   │  • Checkboxes        │  • Garment summary           │
#   │  • Botones           │  • Importe                   │
#   └──────────────────────┴──────────────────────────────┘
# =============================================================================

import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

from app.views.base_view import BaseView
from app import config as C
from app import demo_data as D


class ReimprimirView(BaseView):

    def _build_ui(self):
        self._build_header()
        self._build_body()

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
            text="F3 — Reimprimir Recogida",
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

    # ── Body ──────────────────────────────────────────────────────────────────

    def _build_body(self):
        body = ctk.CTkFrame(self, fg_color=C.CONTENT_BG, corner_radius=0)
        body.pack(fill="both", expand=True, padx=C.PAD_LG, pady=C.PAD_LG)

        # Left: controls (fixed width)
        left = ctk.CTkFrame(
            body,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
            width=300,
        )
        left.pack(side="left", fill="y", padx=(0, C.PAD_MD))
        left.pack_propagate(False)
        self._build_controls(left)

        # Right: preview card
        right = ctk.CTkFrame(
            body,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )
        right.pack(side="left", fill="both", expand=True)
        self._build_preview(right)

    # ── Controls (left panel) ─────────────────────────────────────────────────

    def _build_controls(self, parent):
        ctk.CTkLabel(
            parent,
            text="PARÁMETROS DE REIMPRESIÓN",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))

        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        # ── Número de Recogida ──
        ctk.CTkLabel(
            parent,
            text="Número de Recogida:",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
            text_color=C.TEXT_PRIMARY,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, C.PAD_XS))

        self.recogida_var = tk.StringVar(value=self.state.last_reimprimir_num)
        self.recogida_entry = ctk.CTkEntry(
            parent,
            textvariable=self.recogida_var,
            width=250,
            height=36,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=13, weight="bold"),
            fg_color=C.PANEL_BG,
            border_color=C.BTN_PRIMARY_BG,
            text_color=C.TEXT_PRIMARY,
            placeholder_text="Ej: R-2024-0891",
        )
        self.recogida_entry.pack(padx=C.PAD_MD)
        self.recogida_entry.bind("<Return>", self._lookup_recogida)

        ctk.CTkButton(
            parent,
            text="🔍  Buscar Recogida",
            command=self._lookup_recogida,
            fg_color=C.BTN_SECONDARY_BG,
            hover_color=C.BTN_SECONDARY_HOVER,
            text_color=C.BTN_SECONDARY_TEXT,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
            width=250,
            height=32,
            corner_radius=C.RADIUS_SM,
        ).pack(padx=C.PAD_MD, pady=(C.PAD_SM, 0))

        # ── Separator ──
        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_MD, padx=C.PAD_MD
        )

        # ── Checkboxes ──
        ctk.CTkLabel(
            parent,
            text="Opciones de impresión:",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
            text_color=C.TEXT_PRIMARY,
        ).pack(anchor="w", padx=C.PAD_MD)

        self.chk_cliente   = tk.BooleanVar(value=True)
        self.chk_prendas   = tk.BooleanVar(value=True)
        self.chk_qr        = tk.BooleanVar(value=False)

        checkbox_defs = [
            (self.chk_cliente, "🧾  Imprimir Ticket del Cliente"),
            (self.chk_prendas, "👕  Imprimir Ticket de las Prendas"),
            (self.chk_qr,      "📱  Imprimir Ticket con QR"),
        ]

        for var, label in checkbox_defs:
            cb = ctk.CTkCheckBox(
                parent,
                text=label,
                variable=var,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
                text_color=C.TEXT_PRIMARY,
                fg_color=C.BTN_PRIMARY_BG,
                hover_color=C.BTN_PRIMARY_HOVER,
                checkmark_color="#FFFFFF",
            )
            cb.pack(anchor="w", padx=C.PAD_LG, pady=(C.PAD_SM, 0))

        # QR note
        ctk.CTkLabel(
            parent,
            text="* QR: requiere módulo adicional",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_LG + 24, pady=(2, 0))

        # ── Spacer pushes buttons to bottom ──
        spacer = ctk.CTkFrame(parent, fg_color="transparent")
        spacer.pack(fill="both", expand=True)

        # ── Action buttons ──
        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", padx=C.PAD_MD, pady=C.PAD_MD
        )

        self.make_btn(
            parent, "🖨  Imprimir Ticket",
            self._do_print,
            style="primary", width=250, height=40,
        ).pack(padx=C.PAD_MD, pady=(0, C.PAD_SM))

        self.make_btn(
            parent, "✖  Cerrar",
            lambda: self.navigate("dashboard"),
            style="neutral", width=250, height=34,
        ).pack(padx=C.PAD_MD, pady=(0, C.PAD_MD))

    # ── Preview panel (right) ─────────────────────────────────────────────────

    def _build_preview(self, parent):
        ctk.CTkLabel(
            parent,
            text="VISTA PREVIA DEL TICKET",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_MD, 0))

        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        # Scrollable preview area
        scroll_frame = ctk.CTkScrollableFrame(parent, fg_color="transparent")
        scroll_frame.pack(fill="both", expand=True, padx=C.PAD_MD, pady=C.PAD_SM)

        # Mock ticket card
        ticket = ctk.CTkFrame(
            scroll_frame,
            fg_color="#FAFAFA",
            corner_radius=C.RADIUS_SM,
            border_width=1,
            border_color="#D1D5DB",
        )
        ticket.pack(fill="x", pady=C.PAD_SM)

        self._ticket_content = ctk.CTkFrame(ticket, fg_color="transparent")
        self._ticket_content.pack(fill="x", padx=C.PAD_LG, pady=C.PAD_LG)

        self._render_demo_ticket(self._ticket_content, D.ORDERS[0])

    def _render_demo_ticket(self, parent, order: dict):
        """Render a realistic-looking receipt preview."""

        def row(lbl, val, bold=False):
            f = ctk.CTkFrame(parent, fg_color="transparent")
            f.pack(fill="x", pady=1)
            ctk.CTkLabel(
                f, text=lbl,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
                text_color=C.TEXT_MUTED, width=120, anchor="w",
            ).pack(side="left")
            ctk.CTkLabel(
                f, text=val,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=10,
                                  weight="bold" if bold else "normal"),
                text_color=C.TEXT_PRIMARY, anchor="w",
            ).pack(side="left")

        # Header
        ctk.CTkLabel(
            parent,
            text="TINTORERÍA LAREDO",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=14, weight="bold"),
            text_color=C.TABLE_HEADING_BG,
        ).pack(anchor="center", pady=(0, 2))

        ctk.CTkLabel(
            parent,
            text="C/ Laredo 1 · Tel: 942 000 000",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="center", pady=(0, C.PAD_MD))

        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        row("Nº Recogida:",    order["recogida"], bold=True)
        row("Fecha recogida:", order["fecha"])
        row("Cliente:",        order["nombre"], bold=True)
        row("Prendas:",        str(order["prendas"]))
        row("Estado:",         order["pendiente"])

        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        # Garment list
        ctk.CTkLabel(
            parent,
            text="DETALLE DE PRENDAS",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            text_color=C.TEXT_MUTED,
        ).pack(anchor="w", pady=(C.PAD_SM, 2))

        for g in D.DEMO_GARMENTS:
            f = ctk.CTkFrame(parent, fg_color="transparent")
            f.pack(fill="x", pady=1)
            ctk.CTkLabel(
                f,
                text=f"  {g['ud']}x  {g['prenda']}",
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
                text_color=C.TEXT_PRIMARY, anchor="w",
            ).pack(side="left", expand=True)
            ctk.CTkLabel(
                f,
                text=g["precio"],
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=10, weight="bold"),
                text_color=C.TEXT_PRIMARY, anchor="e",
            ).pack(side="right")

        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_SM
        )

        # Total
        tot_frame = ctk.CTkFrame(parent, fg_color="transparent")
        tot_frame.pack(fill="x")
        ctk.CTkLabel(
            tot_frame,
            text="TOTAL:",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=12, weight="bold"),
            text_color=C.TEXT_PRIMARY,
        ).pack(side="left")
        ctk.CTkLabel(
            tot_frame,
            text=order["importe"],
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=13, weight="bold"),
            text_color=C.BTN_SUCCESS_BG,
        ).pack(side="right")

        # QR placeholder
        ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0).pack(
            fill="x", pady=C.PAD_MD
        )

        qr_box = ctk.CTkFrame(
            parent,
            fg_color="#F1F5F9",
            corner_radius=C.RADIUS_SM,
            border_width=1,
            border_color=C.PANEL_BORDER,
            width=100, height=100,
        )
        qr_box.pack(pady=C.PAD_SM)
        qr_box.pack_propagate(False)
        ctk.CTkLabel(
            qr_box,
            text="[ QR Code ]\nVersión Demo",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9),
            text_color=C.TEXT_MUTED,
            justify="center",
        ).pack(expand=True)

    # ── Actions ───────────────────────────────────────────────────────────────

    def _lookup_recogida(self, event=None):
        num = self.recogida_var.get().strip()
        if not num:
            messagebox.showwarning("Aviso", "Introduzca un número de recogida.", parent=self)
            return
        self.state.last_reimprimir_num = num
        # Demo: always "find" data
        messagebox.showinfo(
            "Recogida Localizada",
            f"Recogida {num}\n\nCliente: Alejandro Martínez Ruiz\n"
            f"Prendas: 5  |  Importe: 38,50 €\n\n"
            f"(Versión Demo — datos de ejemplo)",
            parent=self,
        )

    def _do_print(self):
        opts = []
        if self.chk_cliente.get():  opts.append("Ticket del Cliente")
        if self.chk_prendas.get():  opts.append("Ticket de las Prendas")
        if self.chk_qr.get():       opts.append("Ticket con QR")

        if not opts:
            messagebox.showwarning("Aviso", "Seleccione al menos una opción de impresión.", parent=self)
            return

        messagebox.showinfo(
            "Versión Demo — Impresión",
            f"Se imprimirían:\n\n" + "\n".join(f"  ✔ {o}" for o in opts) +
            f"\n\nRecogida: {self.recogida_var.get()}\n\n"
            "Versión Demo — funcionalidad no implementada todavía.",
            parent=self,
        )

    # ── Lifecycle ─────────────────────────────────────────────────────────────

    def on_show(self):
        self.controller.bind("<Escape>", lambda e: self.navigate("dashboard"))
        self.recogida_entry.focus()
