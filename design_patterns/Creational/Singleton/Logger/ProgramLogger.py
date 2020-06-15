class ProgramLogger():
    __logger = None
    __log_file = ""

    def __new__(cls):
        if not cls.__logger:
            cls.__logger = super(ProgramLogger, cls).__new__(cls)
            cls.__log_file = "This is log file.\n"
        return cls.__logger

    def add_log_info(self, log):
        self.__log_file += log + "\n"

    def show_log_info(self):
        print(self.__log_file)
