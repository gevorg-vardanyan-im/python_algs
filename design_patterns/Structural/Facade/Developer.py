"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Facade.BugTracker import BugTracker


class Developer(object):
    """docstring for Developer"""

    @staticmethod
    def do_job_before_deadline(bug_tracker: BugTracker):
        if bug_tracker.is_sprint_active():
            print("Developer is solving problems ...")
        else:
            print("Developer is learning development stuff ...")
