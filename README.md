# textual-learn

## Devtools

### Run

- The run sub-command runs Textual apps.

- This is equivalent to running python my_app.py from the command prompt.

    ```bash
    textual run my_app.py
    ```

### Serve

- The devtools can also serve your application in a browser.

- Effectively turning your terminal app in to a web application!

    ```bash
    textual serve my_app.py
    ```

### Live editing

- If you combine the run command with the --dev switch your app will run in development mode.

- One of the features of dev mode is live editing of CSS files: any changes to your CSS will be reflected in the terminal a few milliseconds later.

    ```bash
    textual run --dev my_app.py
    ```

### Console

- You can use the option --port to specify a custom port to run the console on, which comes in handy if you have other software running on the port that Textual uses by default:

    ```bash
    textual console --port 7342
    textual run --dev --port 7342 my_app.py
    ```

### Theme Reference

- Here's a list of the colors defined in the default light and dark themes.

    ```bash
    textual color
    ```