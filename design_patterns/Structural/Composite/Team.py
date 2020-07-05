"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Composite.Developer import Developer


class Team(object):
    """docstring for Team"""

    __developers = []

    def add_developer(self, developer:Developer):
        self.__developers.append(developer)

    def remove_developer(self, developer):
        self.__developers.remove(developer)

    def create_project(self):
        print("The team creates project ...")
        for developer in self.__developers:
            developer.write_code()