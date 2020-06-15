from design_patterns.Structural.Adapter.AdapterPythonToDatabase import AdapterPythonToDatabase

class DatabaseRunner():
    def run(self):
        database = AdapterPythonToDatabase()
        database.insert()
        database.update()
        database.select()
        database.remove()


if __name__ == '__main__':
    runner = DatabaseRunner()
    runner.run()
