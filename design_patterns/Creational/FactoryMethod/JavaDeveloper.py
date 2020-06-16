from design_patterns.Creational.FactoryMethod.Developer import Developer


class JavaDeveloper(Developer):
    def plan_work(self):
        print("Java developer plans his working day.")

    def write_code(self):
        print("Java developer writes java code.")

    def review_code(self):
        print("Java developer reviews code.")

    def report_task(self):
        print("Java developer reports about the work.")
