# =============================================================================
# base_view.py
# Tintorería Laredo — Base class for all screen views.
#
# Provides:
#   • show() / hide() lifecycle
#   • Shared widget factory methods (buttons, labels, separators, tables)
#   • "Not implemented" popup helper
#   • Consistent panel / card framing
# =============================================================================

import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
from app import config as C


class BaseView(ctk.CTkFrame):
    """
    Every screen in the application inherits from BaseView.
    It is a full-size CTkFrame that fills the content area.
    """

    def __init__(self, parent, controller, state):
        super().__init__(
            parent,
            fg_color=C.CONTENT_BG,
            corner_radius=0,
        )
        self.controller = controller   # Reference to the root App window
        self.state      = state        # Shared AppState instance

        self._build_ui()

    # ── Lifecycle ────────────────────────────────────────────────────────────

    def _build_ui(self):
        """Override in subclasses to construct the screen."""
        pass

    def on_show(self):
        """Called every time this view is navigated to. Override to refresh."""
        pass

    def on_hide(self):
        """Called when navigating away from this view."""
        pass

    # ── Navigation helper ────────────────────────────────────────────────────

    def navigate(self, view_name: str):
        """Ask the controller to switch to a named view."""
        self.controller.show_view(view_name)

    # ── 'Not implemented' popup ───────────────────────────────────────────────

    def not_implemented(self, feature: str = "Esta función"):
        messagebox.showinfo(
            "Versión Demo",
            f"{feature}\n\nVersión Demo — funcionalidad no implementada todavía.",
            parent=self,
        )

    # ── Widget factory: section header ────────────────────────────────────────

    def make_section_header(self, parent, title: str, subtitle: str = ""):
        """Returns a header frame with title + optional subtitle."""
        frame = ctk.CTkFrame(parent, fg_color=C.HEADER_BG, corner_radius=0, height=C.HEADER_HEIGHT)
        frame.pack_propagate(False)

        title_lbl = ctk.CTkLabel(
            frame,
            text=title,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=17, weight="bold"),
            text_color=C.TEXT_PRIMARY,
        )
        title_lbl.pack(side="left", padx=C.PAD_LG, pady=0, anchor="w")

        if subtitle:
            sub_lbl = ctk.CTkLabel(
                frame,
                text=subtitle,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
                text_color=C.TEXT_MUTED,
            )
            sub_lbl.pack(side="left", padx=(0, C.PAD_MD), pady=0, anchor="w")

        # Thin bottom border
        border = ctk.CTkFrame(frame, fg_color=C.HEADER_BORDER, height=1, corner_radius=0)
        border.pack(side="bottom", fill="x")

        return frame

    # ── Widget factory: card / panel ─────────────────────────────────────────

    def make_card(self, parent, title: str = "", padx=C.PAD_MD, pady=C.PAD_MD):
        """Returns a white card frame with an optional bold title."""
        outer = ctk.CTkFrame(
            parent,
            fg_color=C.PANEL_BG,
            corner_radius=C.RADIUS_MD,
            border_width=1,
            border_color=C.PANEL_BORDER,
        )

        if title:
            title_lbl = ctk.CTkLabel(
                outer,
                text=title,
                font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
                text_color=C.TEXT_SECONDARY,
            )
            title_lbl.pack(anchor="w", padx=padx, pady=(pady, 0))

            sep = ctk.CTkFrame(outer, fg_color=C.PANEL_BORDER, height=1, corner_radius=0)
            sep.pack(fill="x", padx=0, pady=(PAD_SM := 6, 0))

        return outer

    # ── Widget factory: primary button ────────────────────────────────────────

    def make_btn(self, parent, text, command, style="primary", width=130, height=34):
        """
        style options: 'primary', 'secondary', 'danger', 'success', 'neutral'
        """
        color_map = {
            "primary":   (C.BTN_PRIMARY_BG,   C.BTN_PRIMARY_HOVER,   C.BTN_PRIMARY_TEXT),
            "secondary": (C.BTN_SECONDARY_BG,  C.BTN_SECONDARY_HOVER, C.BTN_SECONDARY_TEXT),
            "danger":    (C.BTN_DANGER_BG,     C.BTN_DANGER_HOVER,    C.BTN_DANGER_TEXT),
            "success":   (C.BTN_SUCCESS_BG,    C.BTN_SUCCESS_HOVER,   C.BTN_SUCCESS_TEXT),
            "neutral":   (C.BTN_NEUTRAL_BG,    C.BTN_NEUTRAL_HOVER,   C.BTN_NEUTRAL_TEXT),
        }
        bg, hover, fg = color_map.get(style, color_map["primary"])

        return ctk.CTkButton(
            parent,
            text=text,
            command=command,
            fg_color=bg,
            hover_color=hover,
            text_color=fg,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11, weight="bold"),
            width=width,
            height=height,
            corner_radius=C.RADIUS_SM,
        )

    # ── Widget factory: labelled entry ────────────────────────────────────────

    def make_labelled_entry(self, parent, label: str, default: str = "",
                            width: int = 220, state: str = "normal"):
        """Returns (container_frame, entry_widget)."""
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        lbl = ctk.CTkLabel(
            frame,
            text=label,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=10),
            text_color=C.TEXT_SECONDARY,
            anchor="w",
        )
        lbl.pack(anchor="w")
        entry = ctk.CTkEntry(
            frame,
            width=width,
            height=30,
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=11),
            fg_color=C.PANEL_BG,
            border_color=C.PANEL_BORDER,
            text_color=C.TEXT_PRIMARY,
            placeholder_text_color=C.TEXT_MUTED,
            state=state,
        )
        if default:
            entry.insert(0, default)
        entry.pack(anchor="w")
        return frame, entry

    # ── Widget factory: Treeview / table ─────────────────────────────────────

    def make_table(self, parent, columns: list, show_scrollbar=True,
                   height=8, selectmode="browse"):
        """
        columns: list of dicts with keys: id, label, width, anchor
        Returns (frame, tree).
        """
        frame = ctk.CTkFrame(parent, fg_color="transparent")

        # Style the native ttk.Treeview to match our palette
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Laredo.Treeview",
            background=C.TABLE_ROW_EVEN,
            fieldbackground=C.TABLE_ROW_EVEN,
            foreground=C.TEXT_PRIMARY,
            rowheight=26,
            font=(C.FONT_FAMILY, 10),
            borderwidth=0,
        )
        style.configure(
            "Laredo.Treeview.Heading",
            background=C.TABLE_HEADING_BG,
            foreground=C.TABLE_HEADING_TEXT,
            font=(C.FONT_FAMILY, 10, "bold"),
            relief="flat",
            padding=(4, 6),
        )
        style.map(
            "Laredo.Treeview",
            background=[("selected", C.TABLE_SELECT)],
            foreground=[("selected", C.TABLE_SELECT_TEXT)],
        )
        style.map("Laredo.Treeview.Heading", relief=[("active", "flat")])

        col_ids = [c["id"] for c in columns]

        tree = ttk.Treeview(
            frame,
            columns=col_ids,
            show="headings",
            style="Laredo.Treeview",
            height=height,
            selectmode=selectmode,
        )

        for col in columns:
            tree.heading(col["id"], text=col["label"])
            tree.column(
                col["id"],
                width=col.get("width", 100),
                minwidth=col.get("minwidth", 40),
                anchor=col.get("anchor", "w"),
                stretch=col.get("stretch", False),
            )

        # Alternating row colours
        tree.tag_configure("odd",  background=C.TABLE_ROW_ODD)
        tree.tag_configure("even", background=C.TABLE_ROW_EVEN)

        # Status badge tags
        tree.tag_configure("pending", foreground=C.STATUS_PENDING_TEXT)
        tree.tag_configure("ready",   foreground=C.STATUS_READY_TEXT)
        tree.tag_configure("partial", foreground=C.STATUS_PARTIAL_TEXT)

        tree.pack(side="left", fill="both", expand=True)

        if show_scrollbar:
            sb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=sb.set)
            sb.pack(side="right", fill="y")

        return frame, tree

    def populate_table(self, tree, rows: list):
        """Clear the tree and insert new rows with alternating stripe tags."""
        tree.delete(*tree.get_children())
        for i, row in enumerate(rows):
            tag = "odd" if i % 2 == 0 else "even"
            tree.insert("", "end", values=row, tags=(tag,))

    # ── Widget factory: horizontal separator ─────────────────────────────────

    def make_hsep(self, parent, pady=C.PAD_SM):
        sep = ctk.CTkFrame(parent, fg_color=C.PANEL_BORDER, height=1, corner_radius=0)
        sep.pack(fill="x", pady=pady)
        return sep

    # ── Widget factory: info badge ────────────────────────────────────────────

    def make_badge(self, parent, text: str, bg: str, fg: str):
        lbl = ctk.CTkLabel(
            parent,
            text=f"  {text}  ",
            font=ctk.CTkFont(family=C.FONT_FAMILY, size=9, weight="bold"),
            fg_color=bg,
            text_color=fg,
            corner_radius=10,
        )
        return lbl
