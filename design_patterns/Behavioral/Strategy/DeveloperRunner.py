"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.Strategy.Coding import Coding
from design_patterns.Behavioral.Strategy.Developer import Developer
from design_patterns.Behavioral.Strategy.Reading import Reading
from design_patterns.Behavioral.Strategy.Sleeping import Sleeping
from design_patterns.Behavioral.Strategy.Training import Training


def main():
    developer = Developer()
    developer.set_activity(Sleeping())
    developer.executeActivity()

    developer.set_activity(Training())
    developer.executeActivity()

    developer.set_activity(Sleeping())
    developer.executeActivity()

    developer.set_activity(Reading())
    developer.executeActivity()

    developer.set_activity(Coding())
    developer.executeActivity()

    developer.set_activity(Sleeping())
    developer.executeActivity()


if __name__ == '__main__':
    main()
