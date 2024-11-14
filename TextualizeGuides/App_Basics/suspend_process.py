from textual.app import App, ComposeResult
from textual.widgets import Label, Footer
from textual.binding import Binding

class SuspendProcessApp(App):
    
    BINDINGS = [("s", "suspend_process", "Suspend the process"),
                ("ctrl+s", "suspend_process", "Suspend the process"),
                ("q", "quit", "Quit")]
    
    def compose(self) -> ComposeResult:
        yield Label("Suspending process...")
        yield Footer()

    def action_quit(self):
        self.exit()

if __name__ == "__main__":
    app = SuspendProcessApp()
    app.run()
