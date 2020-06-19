from design_patterns.Creational.AbstractFactory.Team.ProjectManager import \
    ProjectManager


class ServicePM(ProjectManager):
    def manage_project(self):
        print("PM manages service project...")
