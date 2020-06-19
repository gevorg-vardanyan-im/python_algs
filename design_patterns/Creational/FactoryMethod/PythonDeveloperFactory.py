from design_patterns.Creational.FactoryMethod.DeveloperFactory import \
    DeveloperFactory
from design_patterns.Creational.FactoryMethod.PythonDeveloper import \
    PythonDeveloper


class PythonDeveloperFactory(DeveloperFactory):

    def create_developer(self):
        return PythonDeveloper()
