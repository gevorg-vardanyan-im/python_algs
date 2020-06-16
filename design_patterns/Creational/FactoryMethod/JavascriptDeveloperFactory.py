from design_patterns.Creational.FactoryMethod.DeveloperFactory import \
    DeveloperFactory
from design_patterns.Creational.FactoryMethod.JavascriptDeveloper import \
    JavascriptDeveloper


class JavascriptDeveloperFactory(DeveloperFactory):

    def create_developer(self):
        return JavascriptDeveloper()
