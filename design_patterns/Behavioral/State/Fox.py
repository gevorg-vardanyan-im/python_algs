from design_patterns.Behavioral.State.Activity import Activity


class Fox(Activity):
    """docstring for Fox"""

    def evolve(self):
        print("Evolving in the \'Fox\' state.")
