import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full", app_title="Student Streaks")

with app.setup:
    import os
    import marimo as mo
    import sqlalchemy

    from sqlalchemy import Engine


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Student Streaks Analysis with SQL
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Description
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Aim

    Calculate the most extended streak length of students on an educational platform.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Background

    - Websites, especially educational and learning platforms, rely on user data to reveal engagement patterns.
    - This project analyses user streak data to identify the most engaged students. This can inform further actions like contacting them for testimonials, feedback, and to improve the product.
    - **Streak:** The number of consecutive interactions in days.
    - Streaks are a key metric and communicate insights about how users engage, and with what frequency.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Project Setup
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Setup default database engine
    """)
    return


@app.function
def create_engine(database: str | None = None) -> Engine:
    """
    Create database engine.
    Uses credentials from the environment unless database is supplied.
    """
    password: str = os.environ.get("POSTGRES_PASSWORD")
    username: str = os.environ.get("POSTGRES_USER")

    if database is None:
        database = os.environ.get("POSTGRES_DB")

    database_url: str = (
        f"postgresql+psycopg://{username}:{password}@db:5432/{database}"
    )
    engine: Engine = sqlalchemy.create_engine(database_url)

    return engine


@app.cell
def _():
    engine: Engine = create_engine(database="postgres")
    return


if __name__ == "__main__":
    app.run()
