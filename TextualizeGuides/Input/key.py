from textual.app import App, ComposeResult
from textual import events
from textual.widgets import Footer, Header, RichLog

class KeyLogger(RichLog):
    def on_key(self, event: events.Key) -> None:
        self.write(event)

class InputApp(App):
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
        Screen {
            layout: grid;
            grid-size: 2;
            grid-gutter: 1 3;
        }
        
        KeyLogger {
            border: solid green;
        }
        """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield KeyLogger()
        yield KeyLogger()
        yield KeyLogger()
        yield KeyLogger()
        
    def on_toggle_dark(self) -> None:
        self.dark = not self.dark

    def on_quit(self) -> None:
        self.exit("User quit")
        
if __name__ == "__main__":
    app = InputApp()
    reply = app.run()
    print("User reply:", reply)
