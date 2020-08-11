from design_patterns.Behavioral.Observer.Observer import Observer


class Subscriber(Observer):
    """docstring for Subscriber"""

    def handle_event(self, vacancies):
        print("\nDear {0}, we have some changes in the vacancies.\n{1}"
              .format(self.name, vacancies))

    def __init__(self, name):
        self.name = name

