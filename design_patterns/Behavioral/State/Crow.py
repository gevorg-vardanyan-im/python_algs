from design_patterns.Behavioral.State.Activity import Activity


class Crow(Activity):
    """docstring for Crow"""

    def evolve(self):
        print("Evolving in the \'Crow\' state.")
