from abc import ABC, abstractmethod


class Developer(ABC):
    @abstractmethod
    def info(self): pass


class Svarog(ABC):
    @abstractmethod
    def pro(self): pass


class PythonDeveloper(Developer, Svarog):
    def pro(self):
        print("Svarog has created this world.")

    def info(self):
        print("\nPython developer writes python code.")


class GroovyDeveloper(Developer):
    def info(self):
        print("\nGroovy developer writes groovy code (lookalike java).")


py_dev = PythonDeveloper()
py_dev.info()
py_dev.pro()

groovy_dev = GroovyDeveloper()
groovy_dev.info()
