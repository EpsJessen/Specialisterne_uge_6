"""
Get paths to files
"""

from os.path import join


def online_creds_path() -> str:
    """
    OS specific path to communications/credentials
    """
    return join("Data", "communication.json")


def my_creds_path() -> str:
    """
    OS specific path to communications/my_db
    """
    return join("Data", "my_db.json")


def csv_path(table: str) -> str:
    """
    OS specific path to csv table
    """
    return join("Data CSV", f"{table}.csv")


def api_path(table: str) -> str:
    """
    OS specific path to API csv tables
    """
    return join("Data API", "data", f"{table}.csv")


def db_path(table: str) -> str:
    """
    OS specific path to DB csv tables
    """
    return join("Data DB", f"{table}.csv")


def main():
    pass


if __name__ == "__main__":
    main()
