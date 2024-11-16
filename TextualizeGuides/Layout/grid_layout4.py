from textual.app import App, ComposeResult
from textual.widgets import Static, Header, Footer

class GridLayoutApp(App):
    
    BINDINGS = [("q", "quit", "Quit application"),
                ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
    Screen {
        layout: grid;
        grid-size: 3; # 3 cols
        # grid-size: 3; # if add more then 6 widgets
        grid-columns: auto 1fr 1fr
    }
    .box {
        height: 100%; # fr: fraction
        border: solid green;
        content-align: center middle;
    }
    #two {
        column-span: 2;
        row-span: 2;
        background: lightblue;
        border: solid blue;
        content-align: center middle;
    }
    """
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("One", classes="box")
        yield Static("Two (column-span: 2, row-span: 2)", classes="box", id="two")
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
    app.dark = False
    reply = app.run()
    print("User reply:", reply)
