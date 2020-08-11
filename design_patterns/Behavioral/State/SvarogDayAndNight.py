"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.State.Practitioner import Practitioner
from design_patterns.Behavioral.State.Virgo import Virgo


def main():
    starting_position = Virgo()
    practitioner = Practitioner()
    practitioner.set_activity(starting_position)

    for i in range(15):  # remained 15 states
        practitioner.move()
        practitioner.change_activity()


if __name__ == '__main__':
    main()
