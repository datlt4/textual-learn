from textual.app import App
from textual.widgets import Static

class SimpleApp(App):
    async def on_mount(self):
        await self.mount(Static("Hello, Textual!"))

if __name__ == "__main__":
    app = SimpleApp()
    app.run()

# python3 tui_app.py
