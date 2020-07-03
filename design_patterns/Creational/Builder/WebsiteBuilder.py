"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""

from abc import ABC, abstractmethod
from design_patterns.Creational.Builder.Website import Website


class WebsiteBuilder(ABC):
    website: Website

    def create_website(self):
        self.website = Website()

    @abstractmethod
    def build_name(self): pass

    @abstractmethod
    def build_cms(self): pass

    @abstractmethod
    def build_price(self): pass

    def get_website(self):
        return self.website
