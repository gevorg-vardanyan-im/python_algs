"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""
from design_patterns.Behavioral.TemplateMethod.NewsPage import NewsPage
from design_patterns.Behavioral.TemplateMethod.WelcomePage import WelcomePage


def main():
    welcome_page = WelcomePage()
    news_page = NewsPage()

    welcome_page.show_page()
    print("=================================")
    news_page.show_page()


if __name__ == '__main__':
    main()
