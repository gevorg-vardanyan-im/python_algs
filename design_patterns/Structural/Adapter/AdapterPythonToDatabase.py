from design_patterns.Structural.Adapter.Database import Database
from design_patterns.Structural.Adapter.PythonApplication\
    import PythonApplication


class AdapterPythonToDatabase(PythonApplication, Database):
    def insert(self):
        self.saveObject()

    def update(self):
        self.updateObject()

    def select(self):
        self.loadObject()

    def remove(self):
        self.deleteObject()
