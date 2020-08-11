from abc import ABC, abstractmethod


class Activity(ABC):

    @abstractmethod
    def just_do_it(self): pass
