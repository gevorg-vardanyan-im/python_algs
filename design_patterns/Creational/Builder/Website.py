"""
    @author: "Gevorg Vardanyan"
    @email: "gevorg6493@gmail.com"
    @project: "python_algs"
"""


class Website:
    name = ""
    cms = ""
    price = 0

    def set_name(self, name):
        self.name = name

    def set_cms(self, cms):
        self.cms = cms

    def set_price(self, price):
        self.price = price

    def set_lastname(self, price):
        self.price = price

    def __str__(self):
        details = ("Website details:"
                   "\n\tname: {0}"
                   "\n\tcms: {1}"
                   "\n\tprice: {2}$")
        return details.format(self.name, self.cms, self.price)
