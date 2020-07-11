from design_patterns.Behavioral.Command.Command import Command


class Developer:
    """docstring for Developer"""

    insert: Command
    update: Command
    select: Command
    delete: Command

    def __init__(self, insert, update, select, delete):
        self.insert = insert
        self.update = update
        self.select = select
        self.delete = delete

    def insert_record(self):
        self.insert.execute()

    def update_record(self):
        self.update.execute()

    def select_record(self):
        self.select.execute()

    def delete_record(self):
        self.delete.execute()
