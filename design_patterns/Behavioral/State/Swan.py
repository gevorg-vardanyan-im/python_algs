from design_patterns.Behavioral.State.Activity import Activity


class Swan(Activity):
    """docstring for Swan"""

    def evolve(self):
        print("Evolving in the \'Swan\' state.")
