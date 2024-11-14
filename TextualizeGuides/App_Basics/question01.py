from textual.app import App
from textual.widgets import Label, Button

class QuestionApp(App):
    def compose(self):
        yield Label("Do you like pizza?")
        yield Button("Yes!", variant="success", id="yes_button")
        yield Button("No!", variant="default", id="no_button")

    def on_button_pressed(self, event):
        exit(event.button.id)

if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print(f"User chose: {reply}")
