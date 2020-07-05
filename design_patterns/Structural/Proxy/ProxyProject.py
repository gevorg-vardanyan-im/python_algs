"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Proxy.Project import Project
from design_patterns.Structural.Proxy.RealProject import RealProject


class ProxyProject(Project):
    """docstring for ProxyProject"""

    def __init__(self, url):
        self.url = url
        self.real_project = None

    def run(self):
        if not self.real_project:
            self.real_project = RealProject(self.url)
        self.real_project.run()
