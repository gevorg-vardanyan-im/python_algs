"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Facade.Workflow import Workflow


def main():
    workflow = Workflow()
    workflow.solve_problems()
    workflow.take_rest()


if __name__ == '__main__':
    main()
