import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full", app_title="Student Streaks")

with app.setup:
    import marimo as mo


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
