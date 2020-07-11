"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.Command.Database import Database
from design_patterns.Behavioral.Command.DeleteCommand import DeleteCommand
from design_patterns.Behavioral.Command.Developer import Developer
from design_patterns.Behavioral.Command.InsertCommand import InsertCommand
from design_patterns.Behavioral.Command.SelectCommand import SelectCommand
from design_patterns.Behavioral.Command.UpdateCommand import UpdateCommand


def main():
    database = Database()
    developer = Developer(
        InsertCommand(database),
        UpdateCommand(database),
        SelectCommand(database),
        DeleteCommand(database)
    )

    developer.insert_record()
    developer.update_record()
    developer.select_record()
    developer.delete_record()


if __name__ == '__main__':
    main()
