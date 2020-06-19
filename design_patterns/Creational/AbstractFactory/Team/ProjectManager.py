from abc import ABC, abstractmethod


class ProjectManager(ABC):

    @abstractmethod
    def manage_project(self): pass
