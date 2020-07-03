"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""

from design_patterns.Creational.Builder.CMS import CMS
from design_patterns.Creational.Builder.WebsiteBuilder import WebsiteBuilder


class EnterpriseWebsiteBuilder(WebsiteBuilder):
    """Enterprise websites builder"""

    def build_name(self):
        self.website.set_name("Enterprise website")

    def build_cms(self):
        self.website.set_cms(CMS.ALIFRESCO.name)

    def build_price(self):
        self.website.set_price(10000)
