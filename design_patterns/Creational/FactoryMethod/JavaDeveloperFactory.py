from design_patterns.Creational.FactoryMethod.DeveloperFactory import \
    DeveloperFactory
from design_patterns.Creational.FactoryMethod.JavaDeveloper import JavaDeveloper


class JavaDeveloperFactory(DeveloperFactory):

    def create_developer(self):
        return JavaDeveloper()
