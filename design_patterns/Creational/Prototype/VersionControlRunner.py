"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Creational.Prototype.Project import Project
from design_patterns.Creational.Prototype.ProjectFactory import ProjectFactory


def main():
    master = Project(1, "super_project", "source_code_location\n")
    print(master)

    factory = ProjectFactory(master)
    master_clone = factory.clone_project()
    print(master_clone)


if __name__ == '__main__':
    main()
