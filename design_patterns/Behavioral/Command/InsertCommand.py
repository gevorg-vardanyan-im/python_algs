from design_patterns.Behavioral.Command.Database import Database
from design_patterns.Behavioral.Command.Command import Command


class InsertCommand(Command):
    """docstring for InsertCommand"""

    database: Database

    def execute(self):
        self.database.insert()

    def __init__(self, database):
        self.database = database
