from design_patterns.Creational.Singleton.Logger.ProgramLogger\
    import ProgramLogger


def main():
    """
        In order to make sure that the further invocation of the ProgramLogger
        returns the same object, print the various instances of it.
        I.e.
            first_logger = ProgramLogger()
            second_logger = ProgramLogger()
            print(first_logger)
            print(second_logger)
            print(first_logger is second_logger)
    """

    # create several loggers
    first_logger = ProgramLogger()
    second_logger = ProgramLogger()

    # add logs in some order
    first_logger.add_log_info("Log from the first logger ...")
    second_logger.add_log_info("Log from the second logger ...")

    # view the logs and their order
    # and make sure that the instance does not matter
    first_logger.show_log_info()
    second_logger.show_log_info()


if __name__ == '__main__':
    main()
