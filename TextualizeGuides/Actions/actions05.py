from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

TEXT = """
[b]Set your background[/b]
[@click=app.set_color('red')]Red[/]
[@click=app.set_color('green')]Green[/]
[@click=app.set_color('blue')]Blue[/]
"""

class ColorSwitcher(Static):
    def set_background(self, color: str) -> None:
        """Set the background color for this widget."""
        self.styles.background = color

class ActionsApp(App):
    BINDINGS = [
        ("q", "quit", "Quit application"),
        ("d", "toggle_dark", "Toggle dark mode"),
        ("r", "set_color('red')", "Set background to red"),
        ("g", "set_color('green')", "Set background to green"),
        ("b", "set_color('blue')", "Set background to blue"),
    ]

    CSS = """
        Screen {
            layout: grid;
            grid-size: 1;
            grid-gutter: 2 4;
            grid-rows: 1fr;
        }

        ColorSwitcher {
            height: 100%;
            margin: 2 4;
        }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        self.color1 = ColorSwitcher(TEXT)
        self.color2 = ColorSwitcher(TEXT)
        yield self.color1
        yield self.color2

    def action_set_color(self, color: str) -> None:
        """Set the background color of the first widget (color1)."""
        self.color1.set_background(color)

    def on_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark

    def on_quit(self) -> None:
        """Exit the application."""
        self.exit("User quit")

if __name__ == "__main__":
    app = ActionsApp()
    reply = app.run()
    print("User reply:", reply)
