"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from time import sleep

from design_patterns.Behavioral.Memento.GitRepo import GitRepo
from design_patterns.Behavioral.Memento.Project import Project


def main():
    project = Project()
    git = GitRepo()
    print("Creating new project [1.0.0].")
    project.set_version_and_date("1.0.0")
    print(project)

    print("\nSaving the current version into the github.")
    git.save = project.save()

    sleep(3)
    print("\n\nUpdating project version [1.0.1] ... (with a poor code)")
    project.set_version_and_date("1.0.1")
    print(project)
    print("\nBut something went wrong with new codes.")

    sleep(3)
    print("\n\nRolling back to the previous version.")
    project.load(git.save)
    print(project)


if __name__ == '__main__':
    main()
