"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Decorator.DeveloperDecorator import \
    DeveloperDecorator


class PythonSeniorDeveloper(DeveloperDecorator):
    """docstring for SeniorPythonDeveloper"""

    def __init__(self, developer):
        super(PythonSeniorDeveloper, self).__init__(developer)

    def make_job(self):
        return super().make_job() + self.make_code_review()

    def make_code_review(self):
        return "\tMake code review."
