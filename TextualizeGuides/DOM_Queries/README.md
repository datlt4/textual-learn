# DOM Queries

## Query one

- The query_one method is used to retrieve a single widget that matches a selector or a type.

    ```python
    send_button = self.query_one("#send")
    send_button = self.query_one("#send", Button)
    ```

## Making queries

- Apps and widgets also have a query method which finds (or queries) widgets. This method returns a DOMQuery object which is a list-like container of widgets.

### Query selectors

- Apps and widgets also have a query method which finds (or queries) widgets. This method returns a DOMQuery object which is a list-like container of widgets.

    ```python
    for widget in self.query():
        print(widget)

    for button in self.query("Button"):
        print(button)
    ```

### Results

- Query objects have a `results` method which is an alternative way of iterating over widgets. If you supply a type (i.e. a Widget class) then this method will generate only objects of that type.

    ```python
    for button in self.query(".disabled").results(Button):
        print(button)
    ```

## Query objects

- We've seen that the query method returns a DOMQuery object you can iterate over in a for loop. Query objects behave like Python lists and support all of the same operations (such as `query[0]`, `len(query)` ,`reverse(query)` etc). They also have a number of other methods to simplify retrieving and modifying widgets.

## First and last

- The `first` and `last` methods return the first or last matching widget from the selector, respectively.

    ```python
    first_button = self.query("Button").first()
    last_button = self.query("Button").last()

    disabled_button = self.query(".disabled").last(Button)
    ```

## Filter

- Query objects have a `filter` method which further refines a query. This method will return a new query object with widgets that match both the original query and the new selector.

    ```python
    # Get all the Buttons
    buttons_query = self.query("Button")
    # Buttons with 'disabled' CSS class
    disabled_buttons = buttons_query.filter(".disabled")
    ```

## Exclude

- Query objects have an exclude method which is the logical opposite of filter. The exclude method removes any widgets from the query object which match a selector.

    ```python
    # Get all the Buttons
    buttons_query = self.query("Button")
    # Remove all the Buttons with the 'disabled' CSS class
    enabled_buttons = buttons_query.exclude(".disabled")
    ```

## Loop-free operations

- Once you have a query object, you can loop over it to call methods on the matched widgets. Query objects also support a number of methods which make an update to every matched widget without an explicit loop.

    ```python
    self.query("Button").add_class("disabled")

    # # Equivalent to the following:
    # for widget in self.query("Button"):
    #     widget.add_class("disabled")
    ```

- Here are the other loop-free methods on query objects:

    - `add_class` Adds a CSS class (or classes) to matched widgets.

    - `remove_class` Removes a CSS class (or classes) from matched widgets.

    - `blur` Blurs (removes focus) from matching widgets.

    - `focus` Focuses the first matching widgets.

    - `refresh` Refreshes matched widgets.

    - `remove` Removes matched widgets from the DOM.

    - `set_class` Sets a CSS class (or classes) on matched widgets.

    - `set` Sets common attributes on a widget.

    - `toggle_class` Sets a CSS class (or classes) if it is not set, or removes the class (or classes) if they are set on the matched widgets.
    