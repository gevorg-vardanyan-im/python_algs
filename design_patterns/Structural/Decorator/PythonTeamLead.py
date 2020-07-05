"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Decorator.DeveloperDecorator import \
    DeveloperDecorator


class PythonTeamLead(DeveloperDecorator):
    """docstring for PythonTeamLead"""

    def __init__(self, developer):
        super(PythonTeamLead, self).__init__(developer)

    def make_job(self):
        return super().make_job() + self.send_weekly_report()

    def send_weekly_report(self):
        return "\tSend weekly report to customer."
