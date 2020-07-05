"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Decorator.Developer import Developer


class PythonDeveloper(Developer):
    """docstring for PythonDeveloper"""

    def make_job(self):
        return "\tWrite python code."
