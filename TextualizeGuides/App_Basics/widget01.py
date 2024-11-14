from textual.app import App
from textual.widgets import Welcome

class MyApp(App):
    def compose(self):
        yield Welcome("Welcome to Textual!")
        
    def on_button_pressed(self):
        self.exit()

if __name__ == "__main__":
    app = MyApp()
    app.run()
