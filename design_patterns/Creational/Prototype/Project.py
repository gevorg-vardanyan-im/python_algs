"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""

from design_patterns.Creational.Prototype.Copyable import Copyable


class Project(Copyable):
    """docstring for Project"""

    def __init__(self, id, project_name, source):
        self.id = id
        self.project_name = project_name
        self.source = source

    def __str__(self):
        details = ("Project details:"
                   "\n\tid: {0}"
                   "\n\tproject_name: {1}"
                   "\n\tsource: {2}")
        return details.format(self.id, self.project_name, self.source)

    def copy(self):
        return Project(self.id, self.project_name, self.source)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        self._project_name = project_name

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._source = source
