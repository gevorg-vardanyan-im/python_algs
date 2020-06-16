from abc import ABC, abstractmethod

class Developer(ABC):

    @abstractmethod
    def plan_work(self): pass

    @abstractmethod
    def write_code(self): pass

    @abstractmethod
    def review_code(self): pass

    @abstractmethod
    def report_task(self): pass
