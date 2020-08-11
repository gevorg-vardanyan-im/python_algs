from design_patterns.Behavioral.Memento.Save import Save


class GitRepo(object):
    """docstring for GitRepo"""

    __save: Save

    @property
    def save(self):
        return self.__save

    @save.setter
    def save(self, save: Save):
        self.__save = save
