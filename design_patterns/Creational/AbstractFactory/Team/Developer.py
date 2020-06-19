from abc import ABC, abstractmethod


class Developer(ABC):

    @abstractmethod
    def write_code(self): pass
