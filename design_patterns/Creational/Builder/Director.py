"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""

from design_patterns.Creational.Builder.WebsiteBuilder import WebsiteBuilder


class Director(object):
    """Director decides what implementation of website builder we are using."""

    builder: WebsiteBuilder

    def set_builder(self, builder):
        self.builder = builder

    def build_website(self):
        self.builder.create_website()
        self.builder.build_name()
        self.builder.build_cms()
        self.builder.build_price()
        return self.builder.get_website()
