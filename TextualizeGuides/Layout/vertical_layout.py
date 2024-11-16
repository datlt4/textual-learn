from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer

class VerticalApp(App):
    
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
    Screen {
        layout: vertical;
    }
    .box {
        height: 1fr; # fr: fraction
        border: solid green;
        content-align: center middle;
    }
    """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Top", classes="box")
        yield Static("Middle", classes="box")
        yield Static("Bottom", classes="box")
    
    def on_toogle_dark(self):
        self.dark = not self.dark
        
    def on_quit(self):
        self.exit("User quit")

if __name__ == "__main__":
    app = VerticalApp()
    reply = app.run()
    print("User reply:", reply)
