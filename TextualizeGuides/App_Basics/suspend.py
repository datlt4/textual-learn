import os
from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Label, Button

class SuspendApp(App):
    def compose(self)-> ComposeResult:
        yield Button("Suspend", id="suspend_button")
    
    @on(Button.Pressed, "#suspend_button")
    def run_external_editor(self, event) -> None:
        self.suspend()
        os.system("nano")
        
if __name__ == "__main__":
    app = SuspendApp()
    app.run()
