"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.Observer.DevelopersJobSite import \
    DevelopersJobSite
from design_patterns.Behavioral.Observer.Subscriber import Subscriber


def main():
    # vacancies
    JUNIOR = "junior"
    MID = "mid"
    SENIOR = "senior"
    JEDI = "jedi"

    # job site with some vacancies
    job_site = DevelopersJobSite()
    job_site.add_vacancy(JUNIOR)
    job_site.add_vacancy(MID)

    # subscribers
    first_subscriber = Subscriber("DY")
    second_subscriber = Subscriber("EC")
    third_subscriber = Subscriber("RT")

    # subscribe to job site
    job_site.add_observer(first_subscriber)
    job_site.add_observer(second_subscriber)
    job_site.add_observer(third_subscriber)

    print("\tAdded new vacancies....")
    print("===========================================")
    job_site.add_vacancy(SENIOR)
    job_site.add_vacancy(JEDI)

    print("\n\n\tRemoved a vacancy....")
    print("===========================================")
    job_site.remove_vacancy(JUNIOR)


if __name__ == '__main__':
    main()
