from communicate_db import Connector
import polars as pl
from mysql.connector import errors


class Sql_user:

    def __init__(self, user: str, password: str, schema: str = "bikes"):
        self._connector = Connector(
            user=user, password=password, host="localhost", dbname=schema, exists=True
        )

    def make_change(self, query: str) -> str:
        try:
            self._connector.executeCUD(query)
            return True

        except errors.ProgrammingError:
            return False

    def get_info(self, query: str):
        try:
            res = self._connector.executeR(query)
            return True, res
        except:
            return False, pl.DataFrame("Empty", None)


def main():
    nr1 = Sql_user("1", "PASS")
    print(nr1.get_info("call customer_info_self();")[1])
    print(nr1.make_change("call customer_change_first_name('John');"))
    print(nr1.get_info("call customer_info_self();")[1])


if __name__ == "__main__":
    main()
