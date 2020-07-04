"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Creational.Prototype.Project import Project


class ProjectFactory:
    """docstring for ProjectFactory"""
    project: Project = None

    def __init__(self, project):
        self.project = project

    def clone_project(self):
        return self.project.copy()