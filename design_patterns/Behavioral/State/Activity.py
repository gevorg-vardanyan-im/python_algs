from abc import ABC, abstractmethod


class Activity(ABC):

    @abstractmethod
    def evolve(self): pass
