"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Composite.Developer import Developer


class CppDeveloper(Developer):
    """docstring for CppDeveloper"""

    def write_code(self):
        print("Cpp developer writes cpp code ...")
