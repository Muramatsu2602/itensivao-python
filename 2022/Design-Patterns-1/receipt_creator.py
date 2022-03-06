class Receipt_creator(object):

    def __init__(self):

        self.__company_name = None
        self.__cnpj = None
        self.__emission_date = None
        self.__items = None
        self.__details = None

    def with_company_name(self, company_name):
        