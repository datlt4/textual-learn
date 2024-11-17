from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
from textual.color import Color
from textual.binding import Binding

class Bar(Static):
    pass

class ColorChangerApp(App):
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),
                ("r", "add_bar('red')", "Add Red Bar"),
                ("g", "add_bar('green')", "Add Green Bar"),
                ("b", "add_bar('blue')", "Add Blue Bar"),
                ("w", "add_bar('white')", "Add White Bar"),
                Binding("ctrl+c", "quit", "Quit", show=False, priority=True),
                Binding("tab", "focus_next", "Focus Next", show=False),
                Binding("shift+tab", "focus_previous", "Focus Previous", show=False),
                ]
    
    CSS = """
        Screen {
            layout: grid;
            grid-size: 12;
        }
        Bar {
            height: 5;
            border: solid $panel-darken-1;
            content-align: center middle;
        }
        """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        
    def action_add_bar(self, color: str) -> None:
        bar = Bar(color)
        bar.styles.background = Color.parse(color).with_alpha(0.5)
        self.mount(bar)
        self.call_after_refresh(self.screen.scroll_end, animate=True)
        
    def on_toggle_dark(self) -> None:
        self.dark = not self.dark
        
    def on_quit(self) -> None:
        self.exit("User quit")
        
if __name__ == "__main__":
    app = ColorChangerApp()
    reply = app.run()
    print("User reply:", reply)
    