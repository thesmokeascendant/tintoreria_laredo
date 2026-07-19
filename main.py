#!/usr/bin/env python3
# =============================================================================
# main.py
# Tintorería Laredo — Application entry point
#
# Responsibilities:
#   • Bootstrap CustomTkinter appearance
#   • Create the root window
#   • Build the persistent sidebar navigation
#   • Instantiate all views and manage which is visible
#   • Wire global keyboard shortcuts
# =============================================================================

import sys
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk

from app import config as C
from app.state import app_state
from app import demo_data as D


# ── CustomTkinter global appearance ──────────────────────────────────────────
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    """
    Root application window.
    Contains the sidebar (persistent) and a content area where views are
    swapped in/out.
    """

    def __init__(self):
        super().__init__()

        self.title(C.APP_TITLE)
        self.geometry(C.WINDOW_START)
        self.minsize(C.WINDOW_MIN_W, C.WINDOW_MIN_H)

        # Give the window an icon-like appearance on Windows
        try:
            self.iconbitmap(default="")
        except Exception:
            pass

        self._views: dict = {}           # name → view instance
        self._active_view: str = ""      # currently visible view name
        self._sidebar_btns: dict = {}    # section_name → button widget

        self._build_layout()
        self._register_views()
        self._wire_global_shortcuts()

        # Start on dashboard
        self.show_view("dashboard")
        self._set_sidebar_active("dashboard")

    # ── Layout skeleton ───────────────────────────────────────────────────────

    def _build_layout(self):
        """Create the two-column layout: sidebar | content."""

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ── Sidebar ──
        self.sidebar = ctk.CTkFrame(
            self,
            width=C.SIDEBAR_WIDTH,
            fg_color=C.SIDEBAR_BG,
            corner_radius=0,
        )
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        self._build_sidebar(self.sidebar)

        # ── Content area ──
        self.content_area = ctk.CTkFrame(
            self,
            fg_color=C.CONTENT_BG,
            corner_radius=0,
        )
        self.content_area.grid(row=0, column=1, sticky="nsew")
        self.content_area.grid_rowconfigure(0, weight=1)
        self.content_area.grid_columnconfigure(0, weight=1)

    def _build_sidebar(self, parent):
        """Build the full sidebar with logo, nav items, and demo toggle."""

        # ── Logo / branding block ──
        logo_frame = ctk.CTkFrame(parent, fg_color="transparent", height=90)
        logo_frame.pack(fill="x")
        logo_frame.pack_propagate(False)

        ctk.CTkLabel(
            logo_frame,
            text="🧺",
            font=ctk.CTkFont(size=28),
            text_color=C.SIDEBAR_ACCENT,
        ).pack(pady=(C.PAD_LG, 0))

        ctk.CTkLabel(
            logo_frame,
            text="Tintorería\nLaredo",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=13, weight="bold"),
            text_color=C.SIDEBAR_TEXT_ACTIVE,
            justify="center",
        ).pack()

        # Divider
        ctk.CTkFrame(
            parent, fg_color=C.SIDEBAR_HOVER, height=1, corner_radius=0
        ).pack(fill="x", padx=C.PAD_MD, pady=(C.PAD_MD, 0))

        # Section label
        ctk.CTkLabel(
            parent,
            text="MENÚ PRINCIPAL",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=8, weight="bold"),
            text_color="#475569",
        ).pack(anchor="w", padx=C.PAD_MD, pady=(C.PAD_SM, C.PAD_XS))

        # ── Navigation items ──
        for icon, label, action in D.SIDEBAR_ITEMS:
            self._add_sidebar_item(parent, icon, label, action)

        # ── Spacer pushes demo toggle to bottom ──
        spacer = ctk.CTkFrame(parent, fg_color="transparent")
        spacer.pack(fill="both", expand=True)

        # ── Demo mode toggle ──
        ctk.CTkFrame(
            parent, fg_color=C.SIDEBAR_HOVER, height=1, corner_radius=0
        ).pack(fill="x", padx=C.PAD_MD)

        demo_frame = ctk.CTkFrame(parent, fg_color="transparent")
        demo_frame.pack(fill="x", padx=C.PAD_MD, pady=C.PAD_SM)

        ctk.CTkLabel(
            demo_frame,
            text="Modo Demo",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
            text_color=C.TEXT_MUTED,
        ).pack(side="left")

        self.demo_switch = ctk.CTkSwitch(
            demo_frame,
            text="",
            command=self._toggle_demo,
            fg_color="#374151",
            progress_color=C.DEMO_BANNER_BG,
            width=40,
            height=20,
        )
        self.demo_switch.pack(side="right")
        if app_state.demo_mode:
            self.demo_switch.select()

        # Version label
        ctk.CTkLabel(
            parent,
            text=C.APP_VERSION,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=8),
            text_color="#374151",
        ).pack(pady=(0, C.PAD_SM))

    def _add_sidebar_item(self, parent, icon: str, label: str, action: str):
        """Add a single sidebar navigation button."""

        def on_click():
            if action == "quit":
                self.quit_app()
            elif action == "not_implemented":
                messagebox.showinfo(
                    "Versión Demo",
                    f"{label}\n\nVersión Demo — funcionalidad no implementada todavía.",
                    parent=self,
                )
            else:
                self.show_view(action)
                self._set_sidebar_active(action)

        btn = ctk.CTkButton(
            parent,
            text=f"  {icon}  {label}",
            command=on_click,
            anchor="w",
            fg_color="transparent",
            hover_color=C.SIDEBAR_HOVER,
            text_color=C.SIDEBAR_TEXT,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
            height=38,
            corner_radius=C.RADIUS_SM,
            border_spacing=0,
        )
        btn.pack(fill="x", padx=C.PAD_SM, pady=1)

        self._sidebar_btns[action] = btn
        return btn

    def _set_sidebar_active(self, section: str):
        """Highlight the active sidebar item."""
        for key, btn in self._sidebar_btns.items():
            if key == section:
                btn.configure(
                    fg_color=C.SIDEBAR_ACTIVE,
                    text_color=C.SIDEBAR_TEXT_ACTIVE,
                    font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
                )
            else:
                btn.configure(
                    fg_color="transparent",
                    text_color=C.SIDEBAR_TEXT,
                    font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
                )
        app_state.active_section = section

    # ── View registration & routing ───────────────────────────────────────────

    def _register_views(self):
        """Instantiate all views and stack them in the content area."""
        from app.views.dashboard  import DashboardView
        from app.views.recoger    import RecogerView
        from app.views.entregar   import EntregarView
        from app.views.reimprimir import ReimprimirView

        view_map = {
            "dashboard":  DashboardView,
            "recoger":    RecogerView,
            "entregar":   EntregarView,
            "reimprimir": ReimprimirView,
        }

        for name, ViewClass in view_map.items():
            view = ViewClass(self.content_area, controller=self, state=app_state)
            view.grid(row=0, column=0, sticky="nsew")
            self._views[name] = view

    def show_view(self, name: str):
        """Raise the named view to front. Calls lifecycle hooks."""
        if name not in self._views:
            messagebox.showinfo(
                "Versión Demo",
                f"Pantalla «{name}» no disponible en esta versión demo.",
                parent=self,
            )
            return

        # Hide current
        if self._active_view and self._active_view in self._views:
            self._views[self._active_view].on_hide()

        # Show new
        self._views[name].tkraise()
        self._views[name].on_show()
        self._active_view = name

        # Keep sidebar in sync for the 3 main sub-screens
        sidebar_map = {
            "recoger":    "dashboard",
            "entregar":   "dashboard",
            "reimprimir": "dashboard",
            "dashboard":  "dashboard",
        }
        self._set_sidebar_active(sidebar_map.get(name, name))

    # ── Global keyboard shortcuts ──────────────────────────────────────────────

    def _wire_global_shortcuts(self):
        self.bind("<F1>", lambda e: self.show_view("recoger"))
        self.bind("<F2>", lambda e: self.show_view("entregar"))
        self.bind("<F3>", lambda e: self.show_view("reimprimir"))
        self.bind("<Escape>", lambda e: self.show_view("dashboard"))
        # Hidden demo toggle: Ctrl+D
        self.bind("<Control-d>", lambda e: self._toggle_demo())

    # ── Demo mode toggle ──────────────────────────────────────────────────────

    def _toggle_demo(self):
        new_state = app_state.toggle_demo()
        if new_state:
            self.demo_switch.select()
        else:
            self.demo_switch.deselect()
        # Refresh current view
        if self._active_view in self._views:
            self._views[self._active_view].on_show()

    # ── Quit ──────────────────────────────────────────────────────────────────

    def quit_app(self):
        if messagebox.askyesno(
            "Salir",
            "¿Desea cerrar Tintorería Laredo?",
            parent=self,
        ):
            self.destroy()
            sys.exit(0)


# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = App()
    app.mainloop()
