"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Bridge.Program import Program


class HeadSystem(Program):
    """docstring for HeadSystem"""

    def __init__(self, developer):
        super(HeadSystem, self).__init__(developer)

    def develop_program(self):
        print("Head system development is in progress...")
        self._developer.write_code()
