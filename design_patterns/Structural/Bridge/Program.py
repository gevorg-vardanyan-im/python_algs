from abc import ABC, abstractmethod

from design_patterns.Structural.Bridge.Developer import Developer


class Program(ABC):
    # _developer: Developer

    def __init__(self, developer):
        self._developer: Developer = developer

    @abstractmethod
    def develop_program(self): pass
