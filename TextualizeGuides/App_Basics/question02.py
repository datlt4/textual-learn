from textual.app import App, ComposeResult
from textual.widgets import Label, Button, Footer

class QuestionApp(App):
    CSS_PATH = 'tcss/question02.tcss'
    
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    def compose(self) -> ComposeResult:
        yield Footer()
        yield Label("Do you like pizza?", id="question")
        yield Button("Yes!", variant="primary", id="yes_button")
        yield Button("No!", variant="error", id="no_button")

    def on_button_pressed(self, event) -> None:
        if event.button.id == "yes_button":
            print("Yes")
        elif event.button.id == "no_button":
            print("No")
        self.exit(event.button.id)

    def on_toggle_dark(self) -> None:
        self.dark = not self.dark

if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(f"Exit code: {reply}")
