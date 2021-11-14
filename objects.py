"""

Representation objects as class of categories and subcategories.

"""
import re


class MainCategory:
    """
    Main category object represented as category_name field.
    """

    def __init__(self, category_name):
        self.category_name = category_name

    def href(self):
        """
        Return category name as formatted text to create the URL.
        """
        return self.category_name

    def __str__(self):
        category_name = re.search('/(.*),', self.category_name)
        category_name = category_name.group(1).replace('_', ' ')
        return category_name

    def return_category_name(self):
        """
        Return category name for child class.
        """
        return self.category_name


class SubCategory(MainCategory):
    """
    Subcategory represented as main category (parent) field and subcategory_name.
    """

    def __init__(self, category_name, subcategory_name):
        super().__init__(category_name)
        self.subcategory_name = subcategory_name

    def __str__(self):
        subcategory_name = re.search('/(.*)', self.subcategory_name)
        subcategory_name = subcategory_name.group(1).replace('_', ' ')
        return subcategory_name

    def href(self):
        return self.subcategory_name

    def return_category_name(self):
        returned_category_name = super().return_category_name()
        return returned_category_name
