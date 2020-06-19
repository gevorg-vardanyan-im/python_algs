from design_patterns.Creational.AbstractFactory.Team.ProjectTeamFactory import \
    ProjectTeamFactory
from design_patterns.Creational.AbstractFactory.Website.ManualTester import \
    ManualTester
from design_patterns.Creational.AbstractFactory.Website.PhpDeveloper import \
    PhpDeveloper
from design_patterns.Creational.AbstractFactory.Website.WebsitePm import \
    WebsitePm


class WebsiteTeamFactory(ProjectTeamFactory):
    def get_developer(self):
        return PhpDeveloper()

    def get_tester(self):
        return ManualTester()

    def get_manager(self):
        return WebsitePm()
