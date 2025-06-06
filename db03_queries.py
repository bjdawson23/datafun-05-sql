"""
Use Python to execute queries from the sql_queries folder.
"""

# Imports from Python Standard Library
import sqlite3
import os
import pathlib
import pandas as pd
import matplotlib.pyplot as plt

# Import local modules
from utils_logger import logger


def execute_sql_file(connection, file_path) -> None:
    """
    Executes a SQL file using the provided SQLite connection.

    Args:
        connection (sqlite3.Connection): SQLite connection object.
        file_path (str): Path to the SQL file to be executed.
    """
    try:
        with open(file_path, 'r') as file:
            sql_script: str = file.read()
        with connection:
            connection.executescript(sql_script)
            logger.info(f"Executed: {file_path}")
    except Exception as e:
        logger.error(f"Failed to execute {file_path}: {e}")
        raise


def summarize_and_plot_books_by_author(connection):
    """
    Reads the SQL count query from the sql_queries folder, executes it,
    prints a summary table, and displays a bar chart.
    """
    # Path to the count books by author SQL file
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_QUERIES_FOLDER = ROOT_DIR.joinpath("sql_queries")
    count_sql_path = SQL_QUERIES_FOLDER.joinpath("01_count_books_by_author.sql")

    # Read the SQL query from file
    with open(count_sql_path, "r") as f:
        sql_query = f.read()

    # Execute the query and load results into a DataFrame
    df = pd.read_sql_query(sql_query, connection)

    # Print summary table
    print("\nNumber of Books by Author:")
    print(df)

    # Plot bar chart
    plt.figure(figsize=(8, 5))
    plt.bar(df['author_name'], df['book_count'], color='skyblue')
    plt.xlabel('Author')
    plt.ylabel('Number of Books')
    plt.title('Number of Books by Author')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def summarize_and_plot_sql_file(connection, sql_file_path):
    """
    Reads a SQL query from the given file, executes it,
    prints a summary table, and displays a bar chart if possible.
    """
    # Read the SQL query from file
    with open(sql_file_path, "r") as f:
        sql_query = f.read()

    # Execute the query and load results into a DataFrame
    try:
        df = pd.read_sql_query(sql_query, connection)
    except Exception as e:
        logger.error(f"Failed to execute query in {sql_file_path}: {e}")
        return

    # Print summary table
    print(f"\nResults for {os.path.basename(sql_file_path)}:")
    print(df)

    # Try to plot if the result is suitable (at least 2 columns, one numeric)
    if df.shape[1] >= 2:
        # Find the first numeric column (excluding the first column)
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            x_col = df.columns[0]
            y_col = numeric_cols[0]
            plt.figure(figsize=(8, 5))
            plt.bar(df[x_col].astype(str), df[y_col], color='skyblue')
            plt.xlabel(x_col.replace('_', ' ').title())
            plt.ylabel(y_col.replace('_', ' ').title())
            plt.title(f"{y_col.replace('_', ' ').title()} by {x_col.replace('_', ' ').title()}")
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
        else:
            logger.info(f"No numeric columns to plot in {sql_file_path}.")
    else:
        logger.info(f"Not enough columns to plot for {sql_file_path}.")


def main() -> None:

    # Log start of queries execution
    logger.info("Starting queries execution...")

    # Define path variables
    ROOT_DIR = pathlib.Path(__file__).parent.resolve()
    SQL_QUERIES_FOLDER = ROOT_DIR.joinpath("sql_queries")
    DATA_FOLDER = ROOT_DIR.joinpath("data")
    DB_PATH = DATA_FOLDER.joinpath('db.sqlite')

    # Ensure the database file exists before attempting to connect
    if not DB_PATH.exists():
        logger.error(f"Database file not found at {DB_PATH}. Ensure the database is created first.")
        return

    # Connect to SQLite database
    try:
        connection = sqlite3.connect(DB_PATH)
        logger.info(f"Connected to database: {DB_PATH}")

        # Execute all SQL files in the sql_queries folder
        for sql_file in sorted(SQL_QUERIES_FOLDER.glob("*.sql")):
            execute_sql_file(connection, sql_file)

        # Summarize and plot results for each SQL file
        for sql_file in sorted(SQL_QUERIES_FOLDER.glob("*.sql")):
            summarize_and_plot_sql_file(connection, sql_file)

        logger.info("Queries execution completed successfully.")
    except Exception as e:
        logger.error(f"Error during queries execution: {e}")
    finally:
        connection.close()
        logger.info("Database connection closed.")


if __name__ == '__main__':
    main()

