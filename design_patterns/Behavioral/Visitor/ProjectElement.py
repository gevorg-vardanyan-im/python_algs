from abc import ABC, abstractmethod

from design_patterns.Behavioral.Visitor.Developer import Developer


class ProjectElement(ABC):

    # @abstractmethod
    def be_written_by(self, developer: Developer): pass
