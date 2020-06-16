from abc import ABC, abstractmethod


class DeveloperFactory(ABC):

    @abstractmethod
    def create_developer(self): pass
