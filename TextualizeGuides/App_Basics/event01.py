from typing import Coroutine, Any
from textual.app import App
from textual import events

class EventApp(App):
    
    COLORS = [
        "white",
        "maroon",
        "red",
        "purple",
        "fuchsia",
        "olive",
        "yellow",
        "navy",
        "teal",
        "aqua",
    ]
    
    i = 0
    
    def on_mount(self):
        self.screen.styles.background = self.COLORS[self.i]
    
    def on_key(self, event: events.Key) -> Coroutine[Any, Any, None]:
        if event.key.isdecimal():
            self.screen.styles.background = self.COLORS[int(event.key) - 1]
        
    def _on_app_focus(self, event: events.AppFocus) -> Coroutine[Any, Any, None]:
        self.i += 1
        self.screen.styles.background = self.COLORS[self.i % len(self.COLORS)]

    def _on_app_blur(self, event: events.AppBlur) -> Coroutine[Any, Any, None]:
        self.screen.styles.background = "lightgray"
        

if __name__ == "__main__":
    app = EventApp()
    app.run()
