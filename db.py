"""

All the request to database. For simplicity context manager has been created.

"""

import sqlite3


def company_to_json(item):
    """
    Processing the result of sql query for display
    """
    return {
        "category_name": item[0],
        "subcategory_name": item[1],
        "company_name": item[2],
        "email_address": item[3],
        "web_address": item[4],
        "phone_number": item[5],
        "info_of_send": item[6]
    }


def company_to_json_for_email_sender(item):
    """
    Processing the result of sql query for email sender
    """
    return {
        "category_name": item[1],
        "subcategory_name": item[2],
        "company_name": item[3],
        "email_address": item[4],
        "web_address": item[5],
        "phone_number": item[6],
        "info_of_send": item[7]
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
    Query to select data to database form scraping.
    """
    try:
        with SQLite("application.db") as cur:
            # Execute the query
            cur.execute("INSERT INTO companies"
                        "(category_name, subcategory_name, company_name, "
                        "email_address, web_address, phone_number, info_of_send) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?)", dict_)
            return message_query_done()
    except Exception as exception_name:
        print(exception_name)
        return []


def update_data_in_database(email: str) -> None or str:
    """
    Query to update data in database after send email.
    """
    try:
        with SQLite("application.db") as cur:
            # Execute the query
            sqlite_update_query = """Update companies set info_of_send = "sent" where email_address = ?"""
            columnValues = email,
            cur.execute(sqlite_update_query, columnValues)
            return message_query_done()
    except Exception as exception_name:
        print(exception_name)
        return []


def get_count_of_random_companies(num: int):
    """
    Query to get random count item from database.
    """
    try:
        with SQLite("application.db") as cur:
            # Execute the query
            cur.execute('select * from companies order by RANDOM() LIMIT (?)', (num,))

            # Fetch the data and turn into a dict
            result = list(map(company_to_json_for_email_sender, cur.fetchall()))

            return result

    except Exception as exception_name:
        print(f'Return count of random companies: {exception_name}')
        return []


def get_count_of_random_companies_to_send(num: int):
    """
    Query to get random count item from database.
    """
    try:
        with SQLite("application.db") as cur:
            # Execute the query
            cur.execute('select * from companies where info_of_send like "to send" order by RANDOM() LIMIT (?)', (num,))

            # Fetch the data and turn into a dict
            result = list(map(company_to_json_for_email_sender, cur.fetchall()))

            return result

    except Exception as exception_name:
        print(f'Return count of random companies with to send info: {exception_name}')
        return []


def get_count_of_random_companies_sent(num: int):
    """
    Query to get random count item from database.
    """
    try:
        with SQLite("application.db") as cur:
            # Execute the query
            cur.execute('select * from companies where info_of_send like "sent" order by RANDOM() LIMIT (?)', (num,))

            # Fetch the data and turn into a dict
            result = list(map(company_to_json_for_email_sender, cur.fetchall()))

            return result

    except Exception as exception_name:
        print(f'Return count of random companies with sent info: {exception_name}')
        return []
