"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Structural.Proxy.ProxyProject import ProxyProject


def main():
    project_url = "https://github.com/gevorg-vardanyan-im/python_algs"
    project = ProxyProject(project_url)
    project.run()


if __name__ == '__main__':
    main()
