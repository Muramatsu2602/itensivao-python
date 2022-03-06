from datetime import date


class Item(object):

    def __init__(self, description, value):
        self.__description = description
        self.__value = value

    @property
    def description(self):
        return self.__description

    @property
    def value(self):
        return self.__value


class Receipt(object):

    def __init__(self, company_name, cnpj, items, emission_date=date.today(), details=''):
        self.__company_name = company_name
        self.__cnpj = cnpj
        self.__emission_date = emission_date
        if len(details) > 20:
            raise Exception('Receipt details may not exceed 20 characters')
        self.__details = details
        self.__items = items

    @property
    def company_name(self):
        return self.__company_name

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def emission_date(self):
        return self.__emission_date

    @property
    def details(self):
        return self.__details


if __name__ == '__main__':

    items = [
        Item(
            'ITEM A',
            100
        ),
        Item(
            'ITEM B',
            200
        )

    ]

    from receipt_creator import Receipt_creator



    # REMEMBER = optional parameters go LAST
    receipt = Receipt(cnpj='0123183102381',
                      company_name='My Company Ltd',
                      items=items,
                      emission_date=date.today(),
                      details=''
                      )

    receipt_created_with_builder = Receipt_creator()