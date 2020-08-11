from datetime import datetime


class Save:
    """docstring for Saver"""

    def __init__(self, version):
        self.__version = version
        self.__date = datetime.now()

    @property
    def version(self):
        return self.__version

    @property
    def date(self):
        return self.__date
