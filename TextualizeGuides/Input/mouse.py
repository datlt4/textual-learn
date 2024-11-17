from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, RichLog
from textual.color import Color
from textual.binding import Binding
from textual import events

class Ball(Static):
    pass

class MouseApp(App):
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),
                ]
    
    CSS = """
        Screen {
            layers: log ball;
        }

        RichLog {
            layer: log;
        }

        Ball {
            layer: ball;
            width: auto;
            height: 1;
            background: $secondary;
            border: tall $success;
            color: $background;
            box-sizing: content-box;
            text-style: bold;
            padding: 2 4;
        }
        """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield RichLog()
        yield Ball("Textual")
        
    def on_mount(self) -> None:
        """Called when the app is mounted."""
        self.screen.query_one(RichLog).write("App started. Interact with mouse events!")

    def on_mouse_move(self, event: events.MouseMove) -> None:
        """Handle mouse movement."""
        # self.screen.query_one(RichLog).write(f"Mouse moved to {event.screen_offset}")
        self.screen.query_one(RichLog).write(event)
        self.query_one(Ball).offset = event.screen_offset - (8, 3)

    def on_mouse_up(self, event: events.MouseUp) -> None:
        """Handle mouse up events."""
        self.screen.query_one(RichLog).write(event)

    def on_mouse_down(self, event: events.MouseDown) -> None:
        """Handle mouse down events."""
        self.screen.query_one(RichLog).write(event)

    def on_click(self, event: events.Click) -> None:
        """Handle click events."""
        # self.screen.query_one(RichLog).write(f"Mouse clicked at {event.screen_offset} (button={event.button})")
        self.screen.query_one(RichLog).write(event)

    def on_mouse_scroll_up(self, event: events.MouseScrollUp) -> None:
        """Handle scroll up events."""
        self.screen.query_one(RichLog).write(event)

    def on_mouse_scroll_down(self, event: events.MouseScrollDown) -> None:
        """Handle scroll down events."""
        self.screen.query_one(RichLog).write(event)

    def on_quit(self) -> None:
        """Handle quit action."""
        self.screen.query_one(RichLog).write("User quit the application.")
        self.exit("User quit")

if __name__ == "__main__":
    app = MouseApp()
    reply = app.run()
    print("User reply:", reply)
