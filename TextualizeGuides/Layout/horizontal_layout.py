from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer

class HorizontalApp(App):
    
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
    Screen {
        layout: horizontal;
    }
    .box {
        width: 1fr; # fr: fraction
        height: 100%; # fr: fraction
        border: solid green;
        content-align: center middle;
    }
    """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Left", classes="box")
        yield Static("Center", classes="box")
        yield Static("Right", classes="box")
    
    def on_toogle_dark(self):
        self.dark = not self.dark
        
    def on_quit(self):
        self.exit("User quit")

if __name__ == "__main__":
    app = HorizontalApp()
    reply = app.run()
    print("User reply:", reply)
