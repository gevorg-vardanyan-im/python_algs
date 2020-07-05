"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Composite.CppDeveloper import CppDeveloper
from design_patterns.Structural.Composite.PythonDeveloper import PythonDeveloper
from design_patterns.Structural.Composite.Team import Team


def main():
    team = Team()
    first_py_dev = PythonDeveloper()
    second_py_dev = PythonDeveloper()
    cpp_dev = CppDeveloper()

    team.add_developer(first_py_dev)
    team.add_developer(second_py_dev)
    team.add_developer(cpp_dev)

    team.create_project()


if __name__ == '__main__':
    main()
