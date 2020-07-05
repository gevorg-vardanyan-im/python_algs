"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.ChainOfResponsibility.Notifier import Notifier


class SmsNotifier(Notifier):
    """docstring for SmsNotifier"""

    def __init__(self, priority):
        super(SmsNotifier, self).__init__(priority)

    def write(self, message):
        print("Sending sms:\n\t{}".format(message))
