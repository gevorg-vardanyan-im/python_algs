"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Bridge.Developer import Developer


class JavaDeveloper(Developer):
    """docstring for JavaDeveloper"""

    def write_code(self):
        print("Java developer writes java code.")
