"""

Process scraping data by class: DownloadData.
Main functionality: scrap_company_data()

"""

import math
import json
from bs4 import BeautifulSoup
from requests import get
from db import save_data_to_database
from dataclasses import dataclass


@dataclass
class PanoramaSiteData:
    """
    Data needed to future URL's creation.
    """
    PANORAMA_MAIN: str = 'https://panoramafirm.pl'
    TEST_LIST: str = ('/amortyzatory_samochodowe')
    END_PANORAMA_MAIN: str = '/firmy,1.html'
    END_PANORAMA_MAIN_ST: str = '/firmy,'
    END_PANORAMA_MAIN_SEC: str = '.html'

    def __init__(self, category: list) -> None:
        self.category = category


class DownloadData(PanoramaSiteData):
    """
    Main function to scrap data from site.
    """

    @staticmethod
    def success_message() -> str:
        return 'Process has been finished with success!'

    def parse_top_lv_category_site(self) -> BeautifulSoup:
        page_main = get(f'{self.PANORAMA_MAIN}{self.category[0]}{self.END_PANORAMA_MAIN}')
        bs_panorama = BeautifulSoup(page_main.content, 'html.parser')
        return bs_panorama

    def count_number_of_pages(self) -> int:
        page_processing = self.parse_top_lv_category_site().find('div', id="listing-search-filters",
                                                                 class_="card container py-2 text-dark")
        page_processing = page_processing.find('h1').get_text().strip()
        page_processing = ''.join([n for n in page_processing if n.isdigit()])
        number_of_pages = int(page_processing)
        number_of_pages = math.ceil(number_of_pages / 26)
        number_of_pages = math.ceil(.5 * number_of_pages)
        return number_of_pages

    def info_about_process(self, page, pages):
        print(
            f'Working {page}/{pages} page. '
            f'Category: {self.category[1]}. Subcategory: {self.category[2]}')

    def parse_specific_category_page(self, page: int) -> BeautifulSoup:
        page_category = get(
            f'{self.PANORAMA_MAIN}'
            f'{self.category[0]}'
            f'{self.END_PANORAMA_MAIN_ST}'
            f'{page}'
            f'{self.END_PANORAMA_MAIN_SEC}')
        bs_category = BeautifulSoup(page_category.content, 'html.parser')
        return bs_category

    def scrap_company_data(self):
        pages = self.count_number_of_pages()
        for page in range(1, pages + 1):
            bs_category = self.parse_specific_category_page(page)
            self.info_about_process(page, pages)
            self.save_data(bs_category)
        self.success_message()

    @staticmethod
    def extract_correct_data(bs_category: BeautifulSoup) -> str:
        # Find all json types in HTML and extract correct data
        companies_json_html = bs_category.find_all('script', {'type': 'application/ld+json'})
        return companies_json_html[:-1]

    @staticmethod
    def extract_company_json(company_data: object) -> json:
        company_json = str(company_data)[35:-9]
        return json.loads(company_json)

    def json_company_data_into_dict(self, json_load) -> dict:
        if 'email' in json_load:
            company_name = json_load['name']
            email = json_load['email']

            if 'sameAs' not in json_load:
                web = None
            else:
                web = json_load['sameAs']

            if 'telephone' not in json_load:
                phone = None
            else:
                phone = json_load['telephone']
            json_ = {
                "category_name": self.category[1],
                "subcategory_name": self.category[2],
                "company_name": company_name,
                "email_address": email,
                "web_address": web,
                "phone_number": phone,
                "info_of_send": 'to send'
            }
            print(json_)
            return json_

    def save_data(self, bs_category: BeautifulSoup):
        insert_data: list

        for company in self.extract_correct_data(bs_category):
            json_load = self.extract_company_json(company)
            data_dict = self.json_company_data_into_dict(json_load)
            try:
                insert_data = [x for x in data_dict.values() if data_dict is not None]
            except AttributeError as exception_name:
                print(exception_name)
            except UnboundLocalError as exception_name:
                print(exception_name)
            else:
                save_data_to_database(insert_data)
            finally:
                pass
