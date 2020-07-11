from design_patterns.Behavioral.Command.Database import Database
from design_patterns.Behavioral.Command.Command import Command


class SelectCommand(Command):
    """docstring for SelectCommand"""

    database: Database

    def execute(self):
        self.database.select()

    def __init__(self, database):
        self.database = database
