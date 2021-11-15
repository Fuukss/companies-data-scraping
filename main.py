"""
Module for displaying the menu and selecting the defined options for the user.
"""
import time
from category import get_list_of_categories, \
    get_list_of_subcategories, \
    get_random_count_of_subcategories_objects, \
    category_list_of_objects, subcategory_list_of_objects
from db import take_one_company, get_count_of_random_companies
from scraping import DownloadData
from email_sender import send_email


def info_about_scrap_data(index: int, list_: list, len_: int) -> str:
    """
    Return the print about the current process
    """
    print(f'Progress:    {index + 1}/{len_}\n'
          f'Href:        {list_[0]}\n'
          f'Subcategory: {list_[1]}\n'
          f'Category:    {list_[2]}')


def scrap_data_with_random_count() -> str:
    """
    Sub-function of main() for 3rd option.
    """
    try:
        item_count = int(input(print("How many random item do you wanna scrap?\n")))
        category_random_data = get_random_count_of_subcategories_objects(item_count)
        len_ = len(category_random_data)

        for index, single_random_data in enumerate(category_random_data):
            info_about_scrap_data(index, single_random_data, len_)
            companies = DownloadData(single_random_data)
            companies.scrap_company_data()
    except IndexError:
        print('Probably categories or subcategories doesn"t exist.')
    except Exception as exception_name:
        print(exception_name)


def get_random_records() -> None:
    """
        Sub-function of main() for 5th option.
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


def send_random_count_of_emails() -> None:
    """
    Sub-function of main() for 5th option.
    """
    try:
        item_count = int(input(print("How many emails do you wanna send?\n")))
        company_random_data = get_count_of_random_companies(item_count)
        len_ = len(company_random_data)
        for index, single_random_data in enumerate(company_random_data, start=1):
            print(f"Email: {index}/{len_}: {single_random_data}")
            send_email(single_random_data['email_address'])
            print(f"Emial number: {index} to {single_random_data['email_address']} has been sent.")
            time.sleep(5)
    except IndexError:
        print('There are probably not that many records in the database.')
    except Exception as exception_name:
        print(exception_name)


def main():
    """
    Main function to display menu.
    ToDo: python 3.10 add match options
    """
    get_list_of_categories()
    get_list_of_subcategories()
    while True:
        option = input(print("Take one of the option:\n"
                             "1 - display categories\n"
                             "2 - display subcategories\n"
                             "3 - scrap the random category\n"
                             "4 - select random count of records\n"
                             "5 - send emails to potential clients\n"
                             "6 - exit\n"))
        if option == "1":
            for i in category_list_of_objects:
                print(i)
        if option == "2":
            for i in subcategory_list_of_objects:
                print(i)
        if option == '3':
            scrap_data_with_random_count()
        if option == '4':
            get_random_records()
        if option == '5':
            send_random_count_of_emails()
        if option == "6":
            break


if __name__ == "__main__":
    main()
