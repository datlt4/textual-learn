from textual.app import App, ComposeResult
from textual.widgets import Header, Footer

class BasicApp(App):
    """A Textual application."""
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),]
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the application"""
        yield Header()
        yield Footer()
        
    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
        
if __name__ == "__main__":
    app = BasicApp()
    app.run()

# python3 tui_app.py
