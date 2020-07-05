"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Decorator.PythonDeveloper import PythonDeveloper
from design_patterns.Structural.Decorator.PythonSeniorDeveloper import \
    PythonSeniorDeveloper
from design_patterns.Structural.Decorator.PythonTeamLead import PythonTeamLead


def main():
    developer = PythonTeamLead(
        PythonSeniorDeveloper(
            PythonDeveloper()
        )
    )
    print(developer.make_job())


if __name__ == '__main__':
    main()
