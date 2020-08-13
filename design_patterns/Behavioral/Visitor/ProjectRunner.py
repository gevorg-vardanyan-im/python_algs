"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.Visitor.JuniorDeveloper import JuniorDeveloper
from design_patterns.Behavioral.Visitor.Project import Project
from design_patterns.Behavioral.Visitor.SeniorDeveloper import SeniorDeveloper


def main():
    project = Project()
    junior_developer = JuniorDeveloper()
    senior_developer = SeniorDeveloper()

    print("\n\t========== Junior in action ==========")
    project.be_written_by(junior_developer)
    print("\n\t========== Senior in action ==========")
    project.be_written_by(senior_developer)


if __name__ == '__main__':
    main()
