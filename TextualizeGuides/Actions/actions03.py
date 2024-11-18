from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

TEXT = """
[b]Set your background[/b]
[@click=app.set_background('red')]Red[/]
[@click=app.set_background('green')]Green[/]
[@click=app.set_background('blue')]Blue[/]
"""

class ActionsApp(App):
    BINDINGS = [
        ("q", "quit", "Quit application"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("r", "set_background('red')", "Set background to red"),
        ("g", "set_background('green')", "Set background to green"),
        ("b", "set_background('blue')", "Set background to blue"),
    ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static(TEXT)

    def action_set_background(self, color: str) -> None:
        self.screen.styles.background = color

    def on_toggle_dark(self,) -> None:
        self.dark = not self.dark
    
    def on_quit(self) -> None:
        self.exit("User quit")

if __name__ == "__main__":
    app = ActionsApp()
    reply = app.run()
    print("User reply:", reply)
