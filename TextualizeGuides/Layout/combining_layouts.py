from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll
from textual.widgets import Header, Footer, Static


class CombiningLayoutsExample(App):
    BINDINGS = [("q", "quit", "Quit application"),
            ("d", "toggle_dark", "Toggle dark mode"),]
    
    CSS = """
        #app-grid {
            layout: grid;
            grid-size: 2;  /* two columns */
            grid-columns: 1fr;
            grid-rows: 1fr;
        }

        #left-pane > Static {
            background: $boost;
            color: auto;
            margin-bottom: 1;
            padding: 1;
        }

        #left-pane {
            width: 100%;
            height: 100%;
            row-span: 2;
            background: $panel;
            border: dodgerblue;
        }

        #top-right {
            height: 100%;
            background: $panel;
            border: mediumvioletred;
        }

        #top-right > Static {
            width: auto;
            height: 100%;
            margin-right: 1;
            background: $boost;
        }

        #bottom-right {
            height: 100%;
            layout: grid;
            grid-size: 3;
            grid-columns: 1fr;
            grid-rows: 1fr;
            grid-gutter: 1;
            background: $panel;
            border: greenyellow;
        }

        #bottom-right-final {
            column-span: 2;
        }

        #bottom-right > Static {
            height: 100%;
            background: $boost;
        }
        """

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(id="app-grid"):
            with VerticalScroll(id="left-pane"):
                for number in range(15):
                    yield Static(f"Vertical layout, child {number}")
            with Horizontal(id="top-right"):
                yield Static("Horizontally")
                yield Static("Positioned")
                yield Static("Children")
                yield Static("Here")
            with Container(id="bottom-right"):
                yield Static("This")
                yield Static("panel")
                yield Static("is")
                yield Static("using")
                yield Static("grid layout!", id="bottom-right-final")
        yield Footer()
    
    def on_toggle_dark(self):
        self.dark = not self.dark
        
    def on_quit(self):
        self.exit("User quit")
 

if __name__ == "__main__":
    app = CombiningLayoutsExample()
    app.run()
