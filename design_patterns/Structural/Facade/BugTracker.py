"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""


class BugTracker(object):
    """docstring for BugTracker"""
    __active_sprint = False

    def is_sprint_active(self):
        return self.__active_sprint

    def start_sprint(self):
        print("Sprint is active.")
        self.__active_sprint = True

    def finish_sprint(self):
        print("Sprint is over.")
        self.__active_sprint = False
