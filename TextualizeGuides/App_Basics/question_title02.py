from textual.app import App, ComposeResult
from textual.events import Key
from textual.widgets import Label, Button, Footer, Header

class QuestionApp(App):
    TITLE = "A Question Application"
    SUB_TITLE = "The most popular Question"
    
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
        Screen {
            layout: grid;
            grid-size: 2;
            grid-gutter: 2;
            padding: 0;
        }
        
        #question {
            width: 100%;
            height: 100%;
            column-span: 2;
            content-align: center bottom;
            text-style: bold;
        }
        
        Button {
            width: 100%;
        }
        """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Label("Do you like pizza?", id="question")
        yield Button("Yes!", variant="primary", id="yes_button")
        yield Button("No!", variant="error", id="no_button")
        
    def on_toggle_dark(self):
        self.dark = not self.dark
        
    def on_button_pressed(self, event):
        self.exit(event.button.id)

    def on_key(self, event: Key):
        self.title = event.key
        self.sub_title = f"You just pressed: {event.key}"
        
    def on_quit(self):
        self.exit("User quit")

if __name__ == "__main__":
    app = QuestionApp()
    reply = app.run()
    print("User reply:", reply)
