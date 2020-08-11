from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def handle_event(self, vacancies): pass
