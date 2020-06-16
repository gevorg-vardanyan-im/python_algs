from design_patterns.Creational.FactoryMethod.JavaDeveloperFactory import \
    JavaDeveloperFactory
from design_patterns.Creational.FactoryMethod.JavascriptDeveloperFactory import \
    JavascriptDeveloperFactory
from design_patterns.Creational.FactoryMethod.PythonDeveloperFactory import \
    PythonDeveloperFactory


def create_dev_by_specialty(specialty):
    specialty = str(specialty).lower()
    if specialty == "python" or specialty == "py":
        return PythonDeveloperFactory()
    elif specialty == "javascript" or specialty == "js":
        return JavascriptDeveloperFactory()
    elif specialty == "java":
        return JavaDeveloperFactory()
    else:
        raise ValueError("{} speciality is unknown.".format(specialty.title()))


def main():
    developer_factory = create_dev_by_specialty("py")
    developer = developer_factory.create_developer()
    developer.plan_work()

    developer_factory = create_dev_by_specialty("java")
    developer = developer_factory.create_developer()
    developer.write_code()

    developer_factory = create_dev_by_specialty("js")
    developer = developer_factory.create_developer()
    developer.review_code()


if __name__ == '__main__':
    main()
