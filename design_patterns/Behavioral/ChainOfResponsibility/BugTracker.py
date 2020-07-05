"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.ChainOfResponsibility.EmailNotifier import \
    EmailNotifier
from design_patterns.Behavioral.ChainOfResponsibility.Priority import Priority
from design_patterns.Behavioral.ChainOfResponsibility.SimpleReportNotifier \
    import SimpleReportNotifier
from design_patterns.Behavioral.ChainOfResponsibility.SmsNotifier import \
    SmsNotifier


def main():
    report_notifier = SimpleReportNotifier(Priority.ROUTINE.value)
    email_notifier = EmailNotifier(Priority.IMPORTANT.value)
    sms_notifier = SmsNotifier(Priority.ASAP.value)

    report_notifier.set_next_notifier(email_notifier)
    email_notifier.set_next_notifier(sms_notifier)

    report_notifier.notify_manager(Priority.ROUTINE.value,
                                   "Everything is good")
    report_notifier.notify_manager(Priority.IMPORTANT.value,
                                   "Something went wrong")
    report_notifier.notify_manager(Priority.ASAP.value,
                                   "We have an issue here!")


if __name__ == '__main__':
    main()
