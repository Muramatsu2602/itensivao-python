from datetime import date


class Contract(object):

    def __init__(self, date, customer, contract_type):
        self.__date = date
        self.__customer = customer
        self.__type = contract_type

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer):
        self.__customer = customer

    @property
    def contract_type(self):
        return self.__type

    @contract_type.setter
    def contract_type(self, contract_type):
        self.__type = contract_type

    