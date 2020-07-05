"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Proxy.Project import Project


class RealProject(Project):
    """docstring for RealProject"""

    def __init__(self, url):
        self.url = url
        self.load()

    def load(self):
        print("Loading a project from {} ...".format(self.url))

    def run(self):
        print("Running the project - url is '{}'.".format(self.url))
