from design_patterns.Behavioral.State.Activity import Activity


class Horse(Activity):
    """docstring for Horse"""

    def evolve(self):
        print("Evolving in the \'Horse\' state.")
