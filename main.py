"""
Module for displaying the menu and selecting the defined options for the user.
"""
import time
from category import CategoryScraper
from db import get_count_of_random_companies_to_send, get_count_of_random_companies
from scraping import DownloadData
from email_sender import Email
from create_db import create_database_with_table


class MenuFunctionality(CategoryScraper):
    def __init__(self):
        super().__init__()

    @staticmethod
    def info_about_scrap_data(index: int, list_: list, len_: int) -> None:
        """
        Return the print about the current process
        """
        print(f'Progress:    {index + 1}/{len_}\n'
              f'Href:        {list_[0]}\n'
              f'Subcategory: {list_[1]}\n'
              f'Category:    {list_[2]}')

    def scrap_data_with_random_count(self) -> None:
        """
        Sub-function of main() for 3rd option.
        """
        try:
            item_count = int(input(print("How many random item do you wanna scrap?\n")))
            category_random_data = self.get_random_count_of_subcategories_objects(item_count)
            len_ = len(category_random_data)

            for index, single_random_data in enumerate(category_random_data):
                self.info_about_scrap_data(index, single_random_data, len_)
                companies = DownloadData(single_random_data)
                companies.scrap_company_data()
        except IndexError:
            print("Probably categories or subcategories doesn't exist.")
        except Exception as exception_name:
            print(exception_name)

    @staticmethod
    def get_random_records() -> None:
        """
            Sub-function of main() for 4th option.
        """
        try:
            item_count = int(input(print("How many random item do you wanna see?\n")))
            company_random_data = get_count_of_random_companies(item_count)
            for index, single_random_data in enumerate(company_random_data, start=1):
                print(f"{index}: {single_random_data}")
        except IndexError:
            print('There are probably not that many records in the database.')
        except Exception as exception_name:
            print(exception_name)

    @staticmethod
    def send_random_count_of_emails() -> None:
        """
        Sub-function of main() for 5th option.
        """
        try:
            email = Email()
            item_count = int(input(print("How many emails do you wanna send?\n")))
            company_random_data = get_count_of_random_companies_to_send(item_count)
            if not company_random_data:
                return print("There are no records left in the database to be sent. Try scrap new.")
            len_ = len(company_random_data)
            for index, single_random_data in enumerate(company_random_data, start=1):
                print(f"Email: {index}/{len_}: {single_random_data}")
                email.send_email(single_random_data['email_address'])
                print(f"Emial number: {index} to {single_random_data['email_address']} has been sent.")
        except IndexError:
            print('There are probably not that many records in the database.')
        except Exception as exception_name:
            print(exception_name)

    @staticmethod
    def check_if_database_exist() -> None:
        """
        Check if database exist when program starting.
        If exist continue, else create database with base table.
        """
        try:
            with open('application.db'):
                return print("Database already exist")
        except IOError:
            create_database_with_table()
            print("Database has been created.")


def main():
    """
    Main function to display menu.
    ToDo: python 3.10 add match options
    """
    # Initial menu class
    menu = MenuFunctionality()
    menu.check_if_database_exist()
    menu.get_list_of_categories()
    menu.get_list_of_subcategories()
    while True:
        option = input(print("Take one of the option:\n"
                             "1 - display categories\n"
                             "2 - display subcategories\n"
                             "3 - scrap the random category\n"
                             "4 - display random count of records\n"
                             "5 - send emails to potential clients\n"
                             "6 - exit\n"))
        if option == "1":
            for i in menu.category_list_of_objects:
                print(i)
        if option == "2":
            for i in menu.subcategory_list_of_objects:
                print(i)
        if option == '3':
            menu.scrap_data_with_random_count()
        if option == '4':
            menu.get_random_records()
        if option == '5':
            menu.send_random_count_of_emails()
        if option == "6":
            break


if __name__ == "__main__":
    main()
