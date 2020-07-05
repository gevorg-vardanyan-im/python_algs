"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.ChainOfResponsibility.Notifier import Notifier


class EmailNotifier(Notifier):
    """docstring for EmailNotifier"""

    def __init__(self, priority):
        super(EmailNotifier, self).__init__(priority)

    def write(self, message):
        print("Sending email:\n\t{}".format(message))
