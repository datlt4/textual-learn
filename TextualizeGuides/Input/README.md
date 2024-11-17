# Input

## Keyboard input

- The most fundamental way to receive input is via `Key` events which are sent to your app when the user presses a key. Let's write an app to show key events as you type.

- `key.py`

    ```python
    from textual import events
    from textual.app import App, ComposeResult
    from textual.widgets import RichLog


    class InputApp(App):
        """App to display key events."""

        def compose(self) -> ComposeResult:
            yield RichLog()

        def on_key(self, event: events.Key) -> None:
            if event.key == "ctrl+p":
                self.query_one(RichLog).write("ctrl + P")
            else:
                self.query_one(RichLog).write(event)


    if __name__ == "__main__":
        app = InputApp()
        app.run()
    ```

## Bindings

- Keys may be associated with actions for a given widget. This association is known as a `key binding`.

- To create bindings, add a `BINDINGS` class variable to your app or widget. This should be a list of tuples of three strings. The first value is the key, the second is the action, the third value is a short human readable description.

- `binding01.py`

    ```python
    from textual.app import App, ComposeResult
    from textual.color import Color
    from textual.widgets import Footer, Static


    class Bar(Static):
        pass


    class BindingApp(App):
        CSS_PATH = "binding01.tcss"
        BINDINGS = [
            ("r", "add_bar('red')", "Add Red"),
            ("g", "add_bar('green')", "Add Green"),
            ("b", "add_bar('blue')", "Add Blue"),
        ]

        def compose(self) -> ComposeResult:
            yield Footer()

        def action_add_bar(self, color: str) -> None:
            bar = Bar(color)
            bar.styles.background = Color.parse(color).with_alpha(0.5)
            self.mount(bar)
            self.call_after_refresh(self.screen.scroll_end, animate=False)


    if __name__ == "__main__":
        app = BindingApp()
        app.run()
    ```

- `binding01.tcss`

    ```css
    Bar {
        height: 5;
        content-align: center middle;
        text-style: bold;
        margin: 1 2;
        color: $text;
    }
    ```

### Priority bindings

- Individual bindings may be marked as a `priority`, which means they will be checked prior to the bindings of the focused widget. This feature is often used to create hot-keys on the app or screen. Such bindings can not be disabled by binding the same key on a widget.

- You can create priority key bindings by setting `priority=True` on the `Binding` object. Textual uses this feature to add a default binding for `Ctrl+C` so there is always a way to exit the app. Here's the bindings from the App base class. Note the first binding is set as a priority:

    ```python
    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=False, priority=True),
        Binding("tab", "focus_next", "Focus Next", show=False),
        Binding("shift+tab", "focus_previous", "Focus Previous", show=False),
    ]
    ```

## Mouse Input

- Textual will send events in response to mouse movement and mouse clicks. These events contain the coordinates of the mouse cursor relative to the terminal or widget.

- Terminal coordinates are given by a pair values named `x` and `y`. The X coordinate is an offset in characters, extending from the left to the right of the screen. The Y coordinate is an offset in lines, extending from the top of the screen to the bottom.

- Coordinates may be relative to the screen, so (0, 0) would be the top left of the screen. Coordinates may also be relative to a widget, where (0, 0) would be the top left of the widget itself.

### Mouse movements

- When you move the mouse cursor over a widget it will receive MouseMove events which contain the coordinate of the mouse and information about what modifier keys (Ctrl, Shift etc) are held down.

- `mouse01.py`

    ```python
    from textual import events
    from textual.app import App, ComposeResult
    from textual.widgets import RichLog, Static


    class Ball(Static):
        pass


    class MouseApp(App):
        CSS_PATH = "mouse01.tcss"

        def compose(self) -> ComposeResult:
            yield RichLog()
            yield Ball("Textual")

        def on_mouse_move(self, event: events.MouseMove) -> None:
            self.screen.query_one(RichLog).write(event)
            self.query_one(Ball).offset = event.screen_offset - (8, 2)


    if __name__ == "__main__":
        app = MouseApp()
        app.run()
    ```

- `mouse01.tcss`

    ```css
    Screen {
        layers: log ball;
    }

    RichLog {
        layer: log;
    }

    Ball {
        layer: ball;
        width: auto;
        height: 1;
        background: $secondary;
        border: tall $secondary;
        color: $background;
        box-sizing: content-box;
        text-style: bold;
        padding: 0 4;
    }
    ```

### Mouse capture

### Enter and Leave events

### Click events

### Scroll events
