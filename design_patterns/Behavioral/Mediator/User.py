from abc import ABC, abstractmethod


class User(ABC):

    @abstractmethod
    def send_message(self, message): pass

    @abstractmethod
    def get_message(self, message): pass
