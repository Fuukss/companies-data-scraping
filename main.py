"""
Module for displaying the menu and selecting the defined options for the user.
"""
from category import get_list_of_categories, \
    get_list_of_subcategories, \
    get_random_count_of_subcategories_objects, \
    category_list_of_objects, subcategory_list_of_objects
from db import take_one_company
from scraping import DownloadData


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
    Sub-function of main() for 5th option.
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
                             "4 - select first rows of companies table\n"
                             "5 - exit"))
        if option == "1":
            for i in category_list_of_objects:
                print(i)
        if option == "2":
            for i in subcategory_list_of_objects:
                print(i)
        if option == '3':
            scrap_data_with_random_count()
        if option == '4':
            take_one_company()
        if option == "5":
            break


if __name__ == "__main__":
    main()
