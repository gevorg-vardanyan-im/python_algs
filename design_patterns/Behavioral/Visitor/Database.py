from design_patterns.Behavioral.Visitor.Developer import Developer
from design_patterns.Behavioral.Visitor.ProjectElement import ProjectElement


class Database(ProjectElement):
    """docstring for Database"""

    def be_written_by(self, developer: Developer):
        developer.create(self)

