from design_patterns.Behavioral.Command.Database import Database
from design_patterns.Behavioral.Command.Command import Command


class UpdateCommand(Command):
    """docstring for UpdateCommand"""

    database: Database

    def execute(self):
        self.database.update()

    def __init__(self, database):
        self.database = database
