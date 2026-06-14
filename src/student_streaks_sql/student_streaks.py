import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full", app_title="Student Streaks")

with app.setup:
    import os
    import marimo as mo
    import sqlalchemy
    import subprocess

    from pathlib import Path
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
    ### Calculations

    - A streak's duration increments each day the user remains active, and has not frozen the streak manually to preserve progress.
    - The length is not extended when there are no new daily interactions or when the streak is frozen.
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Dataset

    - This is provided by 365 Data Science as a MySQL script (`user_streaks_database.sql`), which has been modified for use with PostgreSQL.
    - It creates a database called `streaks` with a table called `user_streaks_sql`.

    #### Fields
    - `streak_id`: Unique identifier for each streak record.
    - `user_id`: Identifier for each user
    - `streak_active`: Whether the streak is currently active (`True`) or not (`False`).
    - `streak_frozen`: Whether the streak is currently frozen (`True`) or not (`False`).
    - `streak_platform`: The platform on which the streak was recorded.
    - `streak_created`: The date when the streak was started or updated.
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


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Create `streaks` database from SQL script using `psql`

    This approach is used to allow creation of a database separate from the default database in a single script.
    """)
    return


@app.function
def run_psql_script(sql_file: Path) -> subprocess.CompletedProcess:
    """
    Run SQL script using psql.

    Uses the default database and credentials from the environment.
    """
    username: str = os.environ.get("POSTGRES_USER")
    password: str = os.environ.get("POSTGRES_PASSWORD")
    database: str = os.environ.get("POSTGRES_DB")

    result: subprocess.CompletedProcess = subprocess.run(
        ["psql", "-h", "db", "-U", username, "-d", database, "-f", sql_file],
        env={**os.environ, "PGPASSWORD": password},
        check=True,
    )

    return result


if __name__ == "__main__":
    app.run()
