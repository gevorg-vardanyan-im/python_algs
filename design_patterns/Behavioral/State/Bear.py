from design_patterns.Behavioral.State.Activity import Activity


class Bear(Activity):
    """docstring for Bear"""

    def evolve(self):
        print("Evolving in the \'Bear\' state.")
