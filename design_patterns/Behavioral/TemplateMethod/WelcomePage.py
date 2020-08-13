from design_patterns.Behavioral.TemplateMethod.TemplateForWebsite\
    import TemplateForWebsite


class WelcomePage(TemplateForWebsite):
    """docstring for WelcomePage"""

    def show_page_content(self):
        print("<welcome page content>")
