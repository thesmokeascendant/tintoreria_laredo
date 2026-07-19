# =============================================================================
# config.py
# Tintorería Laredo — Global configuration
# All colors, fonts, sizes, and layout constants live here.
# Changing a value here propagates everywhere.
# =============================================================================

APP_TITLE   = "Tintorería Laredo"
APP_VERSION = "v1.0 — Demo"

# Window
WINDOW_MIN_W = 1100
WINDOW_MIN_H = 680
WINDOW_START = "1280x760"

# ── Palette ──────────────────────────────────────────────────────────────────
# Sidebar
SIDEBAR_BG          = "#1A1F2E"   # near-black navy
SIDEBAR_HOVER       = "#252B3D"
SIDEBAR_ACTIVE      = "#2E3650"
SIDEBAR_ACCENT      = "#3B82F6"   # blue stripe for active item
SIDEBAR_TEXT        = "#CBD5E1"
SIDEBAR_TEXT_ACTIVE = "#FFFFFF"
SIDEBAR_WIDTH       = 200

# Main content
CONTENT_BG          = "#F0F4F8"
PANEL_BG            = "#FFFFFF"
PANEL_BORDER        = "#E2E8F0"

# Top header bar
HEADER_BG           = "#FFFFFF"
HEADER_BORDER       = "#E2E8F0"
HEADER_HEIGHT       = 56

# Buttons — primary (blue)
BTN_PRIMARY_BG      = "#2563EB"
BTN_PRIMARY_HOVER   = "#1D4ED8"
BTN_PRIMARY_TEXT    = "#FFFFFF"

# Buttons — secondary (light)
BTN_SECONDARY_BG    = "#EFF6FF"
BTN_SECONDARY_HOVER = "#DBEAFE"
BTN_SECONDARY_TEXT  = "#1E40AF"

# Buttons — danger (red)
BTN_DANGER_BG       = "#DC2626"
BTN_DANGER_HOVER    = "#B91C1C"
BTN_DANGER_TEXT     = "#FFFFFF"

# Buttons — success (green)
BTN_SUCCESS_BG      = "#16A34A"
BTN_SUCCESS_HOVER   = "#15803D"
BTN_SUCCESS_TEXT    = "#FFFFFF"

# Buttons — neutral
BTN_NEUTRAL_BG      = "#64748B"
BTN_NEUTRAL_HOVER   = "#475569"
BTN_NEUTRAL_TEXT    = "#FFFFFF"

# Accent function buttons (F1 / F2 / F3)
FKEY_COLORS = {
    "F1": ("#2563EB", "#1D4ED8"),   # blue
    "F2": ("#16A34A", "#15803D"),   # green
    "F3": ("#7C3AED", "#6D28D9"),   # purple
}

# Table / Treeview
TABLE_HEADING_BG    = "#1E3A5F"
TABLE_HEADING_TEXT  = "#FFFFFF"
TABLE_ROW_ODD       = "#F8FAFC"
TABLE_ROW_EVEN      = "#FFFFFF"
TABLE_SELECT        = "#BFDBFE"
TABLE_SELECT_TEXT   = "#1E3A5F"
TABLE_BORDER        = "#CBD5E1"

# Text colours
TEXT_PRIMARY        = "#0F172A"
TEXT_SECONDARY      = "#475569"
TEXT_MUTED          = "#94A3B8"
TEXT_DANGER         = "#DC2626"

# Status badge colours
STATUS_PENDING_BG   = "#FEF3C7"
STATUS_PENDING_TEXT = "#92400E"
STATUS_READY_BG     = "#D1FAE5"
STATUS_READY_TEXT   = "#065F46"
STATUS_PARTIAL_BG   = "#DBEAFE"
STATUS_PARTIAL_TEXT = "#1E40AF"

# ── Typography ────────────────────────────────────────────────────────────────
FONT_FAMILY         = "Segoe UI"   # Windows; falls back gracefully on macOS/Linux

FONT_TITLE          = (FONT_FAMILY, 20, "bold")
FONT_SUBTITLE       = (FONT_FAMILY, 13, "bold")
FONT_BODY           = (FONT_FAMILY, 11)
FONT_BODY_BOLD      = (FONT_FAMILY, 11, "bold")
FONT_SMALL          = (FONT_FAMILY, 10)
FONT_SMALL_BOLD     = (FONT_FAMILY, 10, "bold")
FONT_SIDEBAR        = (FONT_FAMILY, 11)
FONT_SIDEBAR_ACTIVE = (FONT_FAMILY, 11, "bold")
FONT_FKEY           = (FONT_FAMILY, 12, "bold")
FONT_TABLE_HEAD     = (FONT_FAMILY, 10, "bold")
FONT_TABLE_BODY     = (FONT_FAMILY, 10)
FONT_MONOSPACE      = ("Consolas", 11)

# ── Spacing ───────────────────────────────────────────────────────────────────
PAD_XS  = 4
PAD_SM  = 8
PAD_MD  = 14
PAD_LG  = 20
PAD_XL  = 28

RADIUS_SM   = 4
RADIUS_MD   = 8
RADIUS_LG   = 12

# ── Demo banner ───────────────────────────────────────────────────────────────
DEMO_BANNER_BG   = "#7C3AED"
DEMO_BANNER_TEXT = "#FFFFFF"
