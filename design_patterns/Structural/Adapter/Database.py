from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def insert(self): pass

    @abstractmethod
    def update(self): pass

    @abstractmethod
    def select(self): pass

    @abstractmethod
    def remove(self): pass
