"""

All the request to database. For simplicity context manager has been created.

"""

import sqlite3


def company_to_json(item):
    """
    Processing the result of sql query
    """
    return {
        "category_name": item[0],
        "subcategory_name": item[1],
        "company_name": item[2],
        "email_address": item[3],
        "web_address": item[4],
        "phone_number": item[5]
    }


class SQLite:
    """
    Context manager for SQlite.
    """

    def __init__(self, file="application.db"):
        self.file = file
        self.con: str

    def __enter__(self):
        self.con = sqlite3.connect(self.file)
        return self.con.cursor()

    def __exit__(self, type_, value, traceback):
        self.con.commit()
        self.con.close()


def take_one_company():
    """
    Query to get one record from database
    """
    try:
        with SQLite("application.db") as cur:
            # Execute the query
            cur.execute('SELECT * from companies')

            # Fetch the data and turn into a dict
            result = list(map(company_to_json, cur.fetchall()))

            return print(result[1])

    except Exception as exception_name:
        print(exception_name)
        return []


def message_query_done():
    """
    Info after query
    """
    return "Query done"


def save_data_to_database(dict_: dict) -> None or str:
    """
    Query to select data to database form scraping
    """
    try:
        with SQLite("application.db") as cur:
            # Execute the query
            cur.execute("INSERT INTO companies"
                        "(category_name, subcategory_name, company_name, "
                        "email_address, web_address, phone_number) "
                        "VALUES (?, ?, ?, ?, ?, ?)", dict_)
            return message_query_done()
    except Exception as exception_name:
        print(exception_name)
        return []
