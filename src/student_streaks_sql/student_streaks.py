import marimo

__generated_with = "0.23.9"
app = marimo.App(width="full", app_title="Student Streaks")

with app.setup:
    import os

    import marimo as mo
    import sqlalchemy
    from sqlalchemy import Engine


@app.function
def create_engine(database: str = None) -> Engine:
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
