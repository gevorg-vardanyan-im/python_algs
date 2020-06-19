from design_patterns.Creational.AbstractFactory.Website.WebsiteTeamFactory import \
    WebsiteTeamFactory


def main():
    project_team_factory = WebsiteTeamFactory()
    developer = project_team_factory.get_developer()
    tester = project_team_factory.get_tester()
    pm = project_team_factory.get_manager()

    print("Creating auction website ...")
    developer.write_code()
    tester.test_code()
    pm.manage_project()


if __name__ == '__main__':
    main()