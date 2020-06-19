from design_patterns.Creational.AbstractFactory.Service.JavaDeveloper import \
    JavaDeveloper
from design_patterns.Creational.AbstractFactory.Service.QATester import QATester
from design_patterns.Creational.AbstractFactory.Service.ServicePM import \
    ServicePM
from design_patterns.Creational.AbstractFactory.Team.ProjectTeamFactory import \
    ProjectTeamFactory


class ServiceTeamFactory(ProjectTeamFactory):
    def get_developer(self):
        return JavaDeveloper()

    def get_tester(self):
        return QATester()

    def get_manager(self):
        return ServicePM()
