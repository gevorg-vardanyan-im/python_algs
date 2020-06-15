class PythonApplication():

    def saveObject(self):
        print("Saving an object.")

    def updateObject(self):
        print("Updating an object.")

    def loadObject(self):
        print("Loading an object.")

    def deleteObject(self):
        print("Deleting an object.")


if __name__ == '__main__':
    py_app = PythonApplication()
    py_app.saveObject()
    py_app.updateObject()
    py_app.loadObject()
    py_app.deleteObject()