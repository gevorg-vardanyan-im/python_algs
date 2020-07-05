"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Flyweight.DeveloperFactory import \
    DeveloperFactory


def main():
    developer_factory = DeveloperFactory()
    developers = []
    # we hires 5 python developers
    for _ in range(5):
        developers.append(developer_factory.get_dev_by_specialty("python"))
    # we hires 3 c++ developers
    for _ in range(3):
        developers.append(developer_factory.get_dev_by_specialty("cpp"))

    for developer in developers:
        developer.write_code()


if __name__ == '__main__':
    main()
