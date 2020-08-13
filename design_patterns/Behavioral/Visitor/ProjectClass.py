from design_patterns.Behavioral.Visitor.Developer import Developer
from design_patterns.Behavioral.Visitor.ProjectElement import ProjectElement


class ProjectClass(ProjectElement):
    """docstring for ProjectClass"""

    def be_written_by(self, developer: Developer):
        developer.create(self)
