"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Facade.BugTracker import BugTracker
from design_patterns.Structural.Facade.Developer import Developer
from design_patterns.Structural.Facade.Job import Job


class Workflow(object):
    """docstring for Workflow"""

    def __init__(self):
        self.developer = Developer()
        self.job = Job()
        self.bug_tracker = BugTracker()

    def solve_problems(self):
        self.job.do_job()
        self.bug_tracker.start_sprint()
        self.developer.do_job_before_deadline(self.bug_tracker)
