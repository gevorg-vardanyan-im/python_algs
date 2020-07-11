from design_patterns.Behavioral.Command.Database import Database
from design_patterns.Behavioral.Command.Command import Command


class DeleteCommand(Command):
    """docstring for DeleteCommand"""

    database: Database

    def execute(self):
        self.database.delete()

    def __init__(self, database):
        self.database = database
