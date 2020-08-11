from datetime import datetime

from design_patterns.Behavioral.Memento.Save import Save


class Project:
    """docstring for Project"""

    version: str
    date: datetime

    def set_version_and_date(self, version):
        self.version = version
        self.date = datetime.now()

    def save(self):
        return Save(self.version)

    def load(self, save: Save):
        self.version = save.version
        self.date = save.date

    def __str__(self):
        return ("Project:"
                "\n\tversion: {version}"
                "\n\tdate: {date}")\
            .format(version=self.version, date=self.date)
