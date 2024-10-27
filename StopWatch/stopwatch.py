import os
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from time import monotonic


class TimeDisplayWidget(Static):
    """A widget that displays elapsed time."""
    time = reactive(0.0)

    def on_mount(self) -> None:
        """Event handler called when widget is added to the app."""
        self.start_time = monotonic()
        self.update_timer = self.set_interval(1/60, self.update_time)
        self.update_timer.pause()
        self.total_time = 0.0

    def update_time(self) -> None:
        """Update the elapsed time."""
        self.time = self.total_time + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        """Called when the time attribute changes.
        Define a method starting with watch_ followed by the name of a reactive attribute."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self):
        """Start the stopwatch."""
        self.total_time = 0.0
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self):
        """Stop the stopwatch."""
        self.update_timer.pause()
        self.total_time = self.total_time + (monotonic() - self.start_time)

    def resume(self):
        """Resume the stopwatch."""
        self.start_time = monotonic()
        self.update_timer.resume()

    def reset(self):
        """Reset the stopwatch."""
        self.update_timer.pause()
        self.time = 0.0 # Change value of time attribute, it will trigger self.watch_time
        self.start_time = monotonic()


class StopwatchWidget(Static):
    """A widget that control the stopwatch time."""
    
    def compose(self) -> ComposeResult:
        yield Button("Start", id="start", variant="success")
        yield Button("Resume", id="resume", variant="primary")
        yield Button("Stop", id="stop", variant="warning")
        yield TimeDisplayWidget("00:00:00.00", id="stopwatch")
        yield Button("Reset", id="reset", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when the button is pressed."""
        print(event.button.id)
        time_display = self.query_one(TimeDisplayWidget)
        reset_button = self.query_one("#reset")
        if event.button.id == "start":
            self.add_class("started")
            self.remove_class("stopped")
            reset_button.disabled = True
            time_display.start()
        elif event.button.id == "stop":
            self.remove_class("started")
            self.add_class("stopped")
            time_display.stop()
            reset_button.disabled = False
        elif event.button.id == "resume":
            self.add_class("started")
            self.remove_class("stopped")
            reset_button.disabled = True
            time_display.resume()
        elif event.button.id == "reset":
            self.remove_class("started")
            self.remove_class("stopped")
            time_display.reset()
            reset_button.disabled = True


class StopwatchApp(App):
    """A simple stopwatch"""
    
    """Bind keys to actions in your app"""
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
                ("a", "add_new", "Add new stopwatch"),
                ("r", "rm_last", "Remove last stopwatch"),
                ("q", "quit", "Quit"),]
    
    CSS_PATH = os.path.join("tcss", "stopwatch.css")

    def compose(self) -> ComposeResult:
        """Create child widgets for the application
        Where we construct a user interface with widgets."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(StopwatchWidget(), StopwatchWidget(), StopwatchWidget(), id="timers")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode"""
        self.dark = not self.dark
        
    def action_add_new(self) -> None:
        """An action to add a new stopwatch"""
        new_stopwatch = StopwatchWidget()
        self.query_one("#timers").mount(new_stopwatch)
        new_stopwatch.scroll_visible()
    
    def action_rm_last(self) -> None:
        """An action to remove the last stopwatch"""
        timers = self.query(StopwatchWidget)
        if timers:
            timers.last().remove()
    
    def action_quit(self) -> None:
        """An action to quit the application"""
        self.exit()


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()

# python3 stopwatch.py
