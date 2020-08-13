from design_patterns.Behavioral.Visitor.Database import Database
from design_patterns.Behavioral.Visitor.Developer import Developer
from design_patterns.Behavioral.Visitor.ProjectClass import ProjectClass
from design_patterns.Behavioral.Visitor.ProjectElement import ProjectElement
from design_patterns.Behavioral.Visitor.Test import Test


class JuniorDeveloper(Developer):
    """docstring for JuniorDeveloper"""

    def create(self, element: ProjectElement):
        if isinstance(element, ProjectClass):
            print("Writing a poor code ...")
        elif isinstance(element, Database):
            print("Harming a data ...")
        elif isinstance(element, Test):
            print("Writing non-reliable test ...")
