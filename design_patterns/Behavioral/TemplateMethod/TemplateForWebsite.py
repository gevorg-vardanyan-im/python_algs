from abc import ABC, abstractmethod


class TemplateForWebsite(ABC):

    def show_page(self):
        print("\n<header>")
        self.show_page_content()
        print("\n<footer>")

    @abstractmethod
    def show_page_content(self): pass
