from abc import ABC, abstractmethod

from design_patterns.Behavioral.Mediator.User import User


class Chat(ABC):

    @abstractmethod
    def send_message(self, name, user: User): pass
