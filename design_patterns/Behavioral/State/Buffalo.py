from design_patterns.Behavioral.State.Activity import Activity


class Buffalo(Activity):
    """docstring for Buffalo"""

    def evolve(self):
        print("Evolving in the \'Buffalo\' state.")
