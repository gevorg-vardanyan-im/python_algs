from design_patterns.Creational.AbstractFactory.Service.ServiceTeamFactory import \
    ServiceTeamFactory


def main():
    project_team_factory = ServiceTeamFactory()
    developer = project_team_factory.get_developer()
    tester = project_team_factory.get_tester()
    pm = project_team_factory.get_manager()

    print("Creating the system ...")
    developer.write_code()
    tester.test_code()
    pm.manage_project()


if __name__ == '__main__':
    main()