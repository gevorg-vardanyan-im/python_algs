from design_patterns.Behavioral.Visitor.Database import Database
from design_patterns.Behavioral.Visitor.Developer import Developer
from design_patterns.Behavioral.Visitor.ProjectClass import ProjectClass
from design_patterns.Behavioral.Visitor.ProjectElement import ProjectElement
from design_patterns.Behavioral.Visitor.Test import Test


class Project(ProjectElement):
    """docstring for Project"""

    def __init__(self):
        self.project_elements = [ProjectClass(),
                                 Database(),
                                 Test()]

    def be_written_by(self, developer: Developer):
        for element in self.project_elements:
            element.be_written_by(developer)
