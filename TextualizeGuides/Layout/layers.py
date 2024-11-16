from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class LayersApp(App):
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
        Screen {
            align: center middle;
            layers: below above;
        }

        Static {
            width: 28;
            height: 8;
            color: auto;
            content-align: center middle;
        }

        #box1 {
            layer: above;
            background: darkcyan;
        }

        #box2 {
            layer: below;
            background: orange;
            offset: 32 6;
        }

        #box3 {
            layer: below;
            background: $error-darken-1;
            offset: 18 3;
        }
        """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("box1 (layer = above)", id="box1")
        yield Static("box2 (layer = below)", id="box2")
        yield Static("box3 (layer = below)", id="box3")
        yield Footer()
        
    
    def on_toggle_dark(self):
        self.dark = not self.dark
        
    def on_quit(self):
        self.exit("User quit")

if __name__ == "__main__":
    app = LayersApp()
    reply = app.run()
    print("User reply:", reply)