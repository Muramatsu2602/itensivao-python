from receipt import Receipt
from datetime import date


class Receipt_creator(object):

    def __init__(self):

        self.__company_name = None
        self.__cnpj = None
        self.__emission_date = None
        self.__items = None
        self.__details = None

    # HOW The builder will work:
    #     receipt = Receipt_creator().with_company_name('AHA').withCNPJ('42301321').build()

    def with_company_name(self, company_name):
        self.__company_name = company_name
        return self

    def with_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def with_emission_date(self, emission_date):
        self.__emission_date = emission_date
        return self

    def with_items(self, items):
        self.__items = items
        return self

    def with_details(self, details):
        self.__details = details
        return self

    def build(self):

        if self.__company_name is None:
            raise Exception('The Company Name field must not be blank')
        if self.__cnpj is None:
            raise Exception('The CNPJ field must not be blank')
        if self.__items is None:
            raise Exception('The Items field must not be blank')
        if self.__emission_date is None:
            self.__emission_date = date.today()
        if self.__details is None:
            self.__details = ''

        return Receipt(company_name=self.__company_name, cnpj=self.__cnpj, emission_date=self.__emission_date, items=self.__items, details=self.__details)
