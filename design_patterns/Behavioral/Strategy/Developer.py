from design_patterns.Behavioral.Strategy.Activity import Activity


class Developer(object):
    """docstring for Developer"""

    activity: Activity

    def set_activity(self, activity: Activity):
        self.activity = activity

    def executeActivity(self):
        self.activity.just_do_it()
