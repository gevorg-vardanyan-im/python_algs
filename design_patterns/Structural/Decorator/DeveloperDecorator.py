"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Decorator.Developer import Developer


class DeveloperDecorator(Developer):
    """docstring for DeveloperDecorator"""

    def __init__(self, developer: Developer):
        self.developer = developer

    def make_job(self):
        return self.developer.make_job()
