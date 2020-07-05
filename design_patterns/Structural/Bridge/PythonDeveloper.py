"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Bridge.Developer import Developer


class PythonDeveloper(Developer):
    """docstring for PythonDeveloper"""

    def write_code(self):
        print("Python developer writes python code.")
