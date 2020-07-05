from abc import ABC, abstractmethod


class Notifier(ABC):
    priority = 0
    next_notifier = None

    def __init__(self, priority):
        self.priority = priority

    def set_next_notifier(self, next_notifier):
        self.next_notifier = next_notifier

    def notify_manager(self, level, message):
        if level >= self.priority:
            self.write(message)
        if self.next_notifier is not None:
            self.next_notifier.notify_manager(level, message)

    @abstractmethod
    def write(self, message): pass
