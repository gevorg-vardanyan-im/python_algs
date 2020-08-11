from design_patterns.Behavioral.Observer.Observed import Observed
from design_patterns.Behavioral.Observer.Observer import Observer


class DevelopersJobSite(Observed):
    """docstring for DevelopersJobSite"""

    def __init__(self):
        self.vacancies = []
        self.subscibers = []

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)
        self.notify_observers()

    def remove_vacancy(self, vacancy):
        try:
            self.vacancies.remove(vacancy)
        except ValueError as e:
            print("{} vacancy was not found in the vacancies list."
                  .format(vacancy))
        finally:
            self.notify_observers()

    def add_observer(self, observer: Observer):
        self.subscibers.append(observer)

    def remove_observer(self, observer: Observer):
        try:
            self.subscibers.remove(observer)
        except ValueError as e:
            print("{} observer was not found in the subscribers list"
                  .format(observer))

    def notify_observers(self):
        for sub in self.subscibers:
            sub.handle_event(self.vacancies)
        print("\n")
