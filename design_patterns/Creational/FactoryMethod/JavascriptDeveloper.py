from design_patterns.Creational.FactoryMethod.Developer import Developer


class JavascriptDeveloper(Developer):
    def plan_work(self):
        print("Javascrip developer plans his working day.")

    def write_code(self):
        print("Javascrip developer writes js code.")

    def review_code(self):
        print("Javascrip developer reviews code.")

    def report_task(self):
        print("Javascrip developer reports about the work.")
