from design_patterns.Behavioral.State.Activity import Activity


class Finist(Activity):
    """docstring for Finist"""

    def evolve(self):
        print("Evolving in the \'Finist\' state.")
