from design_patterns.Creational.AbstractFactory.Team.Developer import Developer


class JavaDeveloper(Developer):
    def write_code(self):
        print("Java developer writes java code...")
