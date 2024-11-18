from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Header, Footer

class ActionsApp(App):
    
    CSS = """
        Screen {
            background: $background;
        }
    """
    
    BINDINGS = [
        ("q", "quit", "Quit application"),
        ("d", "toggle_dark", "Toggle dark mode"),
    ]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()

    def action_set_background(self, color: str) -> None:
        """Set the background color of the screen."""
        self.screen.styles.background = color

    async def on_key(self, event: events.Key) -> None:
        """Handle key press events."""
        if event.key == "r":
            await self.run_action("set_background('red')")
        elif event.key == "b":
            await self.run_action("set_background('blue')")
        elif event.key == "g":
            await self.run_action("set_background('green')")
            
    def on_toggle_dark(self) -> None:
        self.dark = not self.dark
    
    def on_quit(self) -> None:
        self.exit("User quit")

if __name__ == "__main__":
    app = ActionsApp()
    reply = app.run()
    print("User reply:", reply)
