"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Bridge.Program import Program


class StockExchange(Program):
    """docstring for StockExchange"""

    def __init__(self, developer):
        super(StockExchange, self).__init__(developer)

    def develop_program(self):
        print("Stock exchange development is on progress...")
        self._developer.write_code()
