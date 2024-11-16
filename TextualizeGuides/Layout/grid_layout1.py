from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer

class GridLayoutApp(App):
    
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
    Screen {
        layout: grid;
        grid-size: 3 2; # 3 cols x 2 rows
        # grid-size: 3; # if add more then 6 widgets
    }
    .box {
        height: 100%; # fr: fraction
        border: solid green;
        content-align: center middle;
    }
    """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("One", classes="box")
        yield Static("Two", classes="box")
        yield Static("Three", classes="box")
        yield Static("Four", classes="box")
        yield Static("Five", classes="box")
        yield Static("Six", classes="box")
        yield Static("Seven", classes="box")
    
    def on_toogle_dark(self):
        self.dark = not self.dark
        
    def on_quit(self):
        self.exit("User quit")

if __name__ == "__main__":
    app = GridLayoutApp()
    reply = app.run()
    print("User reply:", reply)
