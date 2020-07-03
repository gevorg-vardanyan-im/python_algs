"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""

from design_patterns.Creational.Builder.CMS import CMS
from design_patterns.Creational.Builder.WebsiteBuilder import WebsiteBuilder


class VisitCardWebsiteBuilder(WebsiteBuilder):
    """Visit-card websites builder"""

    def build_name(self):
        self.website.set_name("Visit card")

    def build_cms(self):
        self.website.set_cms(CMS.WORDPRESS.name)

    def build_price(self):
        self.website.set_price(500)
