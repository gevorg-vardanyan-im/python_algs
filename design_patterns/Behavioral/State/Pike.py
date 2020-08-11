from design_patterns.Behavioral.State.Activity import Activity


class Pike(Activity):
    """docstring for Pike"""

    def evolve(self):
        print("Evolving in the \'Pike\' state.")
