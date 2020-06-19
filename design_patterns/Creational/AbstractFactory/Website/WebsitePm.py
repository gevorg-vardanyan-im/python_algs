from design_patterns.Creational.AbstractFactory.Team.ProjectManager import \
    ProjectManager


class WebsitePm(ProjectManager):
    def manage_project(self):
        print("Website pm manages website project ...")
