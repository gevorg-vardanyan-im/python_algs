"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Flyweight.CppDeveloper import CppDeveloper
from design_patterns.Structural.Flyweight.PythonDeveloper import PythonDeveloper


class DeveloperFactory(object):
    """docstring for DeveloperFactory"""

    def __init__(self):
        self.developers = dict()

    def get_dev_by_specialty(self, specialty):
        developer = self.developers.get(specialty)
        if not developer:
            if str(specialty).lower() == "python":
                print("Hiring a python developer ...")
                developer = PythonDeveloper()
            else:
                print("Hiring a c++ developer ...")
                developer = CppDeveloper()
            self.developers[specialty] = developer
        return developer
