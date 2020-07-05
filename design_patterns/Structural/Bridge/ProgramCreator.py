"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Bridge.HeadSystem import HeadSystem
from design_patterns.Structural.Bridge.JavaDeveloper import JavaDeveloper
from design_patterns.Structural.Bridge.PythonDeveloper import PythonDeveloper
from design_patterns.Structural.Bridge.StockExchange import StockExchange


def main():
    programs = [
        HeadSystem(PythonDeveloper()),
        StockExchange(JavaDeveloper())
    ]
    for program in programs:
        program.develop_program()


if __name__ == '__main__':
    main()
