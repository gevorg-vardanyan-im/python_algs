from design_patterns.Behavioral.TemplateMethod.TemplateForWebsite \
    import TemplateForWebsite


class NewsPage(TemplateForWebsite):
    """docstring for NewsPage"""

    def show_page_content(self):
        print("<news page content>")
