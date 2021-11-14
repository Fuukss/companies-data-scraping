"""

Functionality for get the category from panorama web site and then scrap subcategories data.

"""
import random
from bs4 import BeautifulSoup
from requests import get
from objects import MainCategory, SubCategory


URL_PANORAMA: str = 'https://panoramafirm.pl/budownictwo,b/branze.html'
URL_PANORAMA_MAIN: str = 'https://panoramafirm.pl'

industry_page = get(f'{URL_PANORAMA}')
bs_panorama_web_site = BeautifulSoup(industry_page.content, 'html.parser')

subcategory_list_of_objects = []
category_list_of_objects = []


def get_list_of_categories() -> list:
    """
    Return list of instance of an objects - categories
    :return: category_object_list: href(), __str__()
    """
    class_ = 'card-header bg-transparent border-0 py-1 cursor-pointer'
    for categories in bs_panorama_web_site.find_all('div', class_):
        category = categories.find('a', href=True)
        category = category['href']
        category_object = MainCategory(category)
        category_list_of_objects.append(category_object)
    return category_list_of_objects


def bs_subcategories_site_parse_html(categories: list) -> BeautifulSoup:
    page_subcategory = get(f'{URL_PANORAMA_MAIN}{categories.href()}')
    bs_panorama_sub = BeautifulSoup(page_subcategory.content, 'html.parser')
    return bs_panorama_sub


def get_list_of_subcategories() -> list:
    """
    Return list of instance of an objects - subcategories
    :return: subcategory_object_list: href(), __str__()
    """
    for categories in category_list_of_objects:
        for subcategory in bs_subcategories_site_parse_html(categories)('li', class_='py-1'):
            subcategory = subcategory.find('a', href=True)
            subcategory = subcategory['href']
            subcategory_object = SubCategory(categories, subcategory)
            subcategory_list_of_objects.append(subcategory_object)
    return subcategory_list_of_objects


def get_random_count_of_subcategories_objects(item_count: int) -> list:
    random_list_of_objects = random.choices(subcategory_list_of_objects, k=item_count)
    random_list_of_elements = [[x.href(), str(x), str(x.return_category_name())]
                               for x in random_list_of_objects]
    return random_list_of_elements
