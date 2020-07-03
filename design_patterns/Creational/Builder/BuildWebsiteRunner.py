"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""

from design_patterns.Creational.Builder.Director import Director
from design_patterns.Creational.Builder.EnterpriseWebsiteBuilder import \
    EnterpriseWebsiteBuilder
from design_patterns.Creational.Builder.VisitCardWebsiteBuilder import \
    VisitCardWebsiteBuilder


def main():
    """
    we can create a website per our need by using corresponding website builder
    """
    director = Director()
    director.set_builder(EnterpriseWebsiteBuilder())
    # director.set_builder(VisitCardWebsiteBuilder())
    website = director.build_website()
    print(website)


if __name__ == '__main__':
    main()