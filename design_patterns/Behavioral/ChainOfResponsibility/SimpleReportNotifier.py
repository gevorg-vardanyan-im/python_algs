"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.ChainOfResponsibility.Notifier import Notifier


class SimpleReportNotifier(Notifier):
    """docstring for SimpleReportNotifier"""

    def __init__(self, priority):
        super(SimpleReportNotifier, self).__init__(priority)

    def write(self, message):
        print("\nNotifying by using simple report:\n\t{}".format(message))
