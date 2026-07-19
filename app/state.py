# =============================================================================
# state.py
# Tintorería Laredo — Shared application state.
# A simple class instance shared across all views so they can read/write
# common flags without coupling directly to each other.
# =============================================================================

class AppState:
    """
    Singleton-style state container.
    Instantiated once in main.py and passed into every view.
    """

    def __init__(self):
        # Demo mode: when True, screens auto-populate and look fully loaded.
        # Toggle via the hidden Ctrl+D shortcut.
        self.demo_mode: bool = True          # ON by default for prototype

        # Currently active sidebar section (drives highlight state)
        self.active_section: str = "dashboard"

        # Last customer selected in Entregar flow (carries across screens)
        self.selected_customer: dict | None = None

        # Last order selected in Entregar flow
        self.selected_order: dict | None = None

        # Last recogida number typed in Reimprimir flow
        self.last_reimprimir_num: str = "R-2024-0891"

    def toggle_demo(self):
        self.demo_mode = not self.demo_mode
        return self.demo_mode


# Single shared instance imported by views
app_state = AppState()
