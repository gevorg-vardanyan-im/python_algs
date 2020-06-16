from design_patterns.Creational.FactoryMethod.Developer import Developer


class PythonDeveloper(Developer):
    def plan_work(self):
        print("Python developer plans his working day.")

    def write_code(self):
        print("Python developer writes python code.")

    def review_code(self):
        print("Python developer reviews code.")

    def report_task(self):
        print("Python developer reports about the work.")
