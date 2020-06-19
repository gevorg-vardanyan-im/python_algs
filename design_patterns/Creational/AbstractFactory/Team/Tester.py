from abc import ABC, abstractmethod


class Tester(ABC):

    @abstractmethod
    def test_code(self): pass
