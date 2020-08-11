from design_patterns.Behavioral.State.Activity import Activity


class Snake(Activity):
    """docstring for Snake"""

    def evolve(self):
        print("Evolving in the \'Snake\' state.")
