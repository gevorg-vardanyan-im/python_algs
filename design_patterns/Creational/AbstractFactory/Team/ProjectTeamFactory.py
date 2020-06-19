from abc import ABC, abstractmethod


class ProjectTeamFactory(ABC):

    @abstractmethod
    def get_developer(self): pass

    @abstractmethod
    def get_tester(self): pass

    @abstractmethod
    def get_manager(self): pass
