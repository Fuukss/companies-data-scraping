"""

Functionality for get the category from panorama web site and then scrap subcategories data.

"""
import random
from bs4 import BeautifulSoup
from requests import get
from objects import MainCategory, SubCategory
from dataclasses import dataclass


@dataclass
class CategoryScraper:
    URL_PANORAMA: str = 'https://panoramafirm.pl/budownictwo,b/branze.html'
    URL_PANORAMA_MAIN: str = 'https://panoramafirm.pl'
    subcategory_list_of_objects = []
    category_list_of_objects = []

    def __init__(self):
        self.industry_page = get(f'{self.URL_PANORAMA}')
        self.bs_panorama_web_site = BeautifulSoup(self.industry_page.content, 'html.parser')

    def get_list_of_categories(self) -> list:
        """
        Return list of instance of an objects - categories
        :return: category_object_list: href(), __str__()
        """
        _class = 'card-header bg-transparent border-0 py-1 cursor-pointer'
        for categories in self.bs_panorama_web_site.find_all('div', _class):
            category = (categories.find('a', href=True))['href']
            category_object = MainCategory(category)
            self.category_list_of_objects.append(category_object)
        return self.category_list_of_objects

    def bs_subcategories_site_parse_html(self, categories: list) -> BeautifulSoup:
        page_subcategory = get(f'{self.URL_PANORAMA_MAIN}{categories.href()}')
        bs_panorama_sub = BeautifulSoup(page_subcategory.content, 'html.parser')
        return bs_panorama_sub

    def get_list_of_subcategories(self) -> list:
        """
        Return list of instance of an objects - subcategories
        :return: subcategory_object_list: href(), __str__()
        """
        for categories in self.category_list_of_objects:
            for subcategory in self.bs_subcategories_site_parse_html(categories)('li', class_='py-1'):
                subcategory = (subcategory.find('a', href=True))['href']
                subcategory_object = SubCategory(categories, subcategory)
                self.subcategory_list_of_objects.append(subcategory_object)
        return self.subcategory_list_of_objects

    def get_random_count_of_subcategories_objects(self, item_count: int) -> list:
        random_list_of_objects = random.choices(self.subcategory_list_of_objects, k=item_count)
        random_list_of_elements = [[x.href(), str(x), str(x.return_category_name())]
                                   for x in random_list_of_objects]
        return random_list_of_elements
