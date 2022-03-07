from datetime import date

from matplotlib.pyplot import hist


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

    def advance(self):
        if self.__type == 'NEW':
            self.__type = 'IN PROGRESS'
        elif self.__type == 'IN PROGRESS':
            self.__type = 'DEAL'
        elif self.__type == 'DEAL':
            self.__type = 'DONE'

    def save_state(self):
        return State(Contract(date=self.__date, customer=self.__customer, contract_type=self.__type))

    def restore_state(self, state):
        self.__customer = state.contract.customer
        self.__date = state.contract.date
        self.__type = state.contract.contract_type


class State(object):

    def __init__(self, contract):
        self.__contract = contract

    @property
    def contract(self):
        return self.__contract


class History(object):

    def __init__(self):
        self.__saved_states = []

    def get_state(self, index):
        return self.__saved_states[index]

    def add_state(self, state):
        self.__saved_states.append(state)


if __name__ == '__main__':

    history = History()

    contract = Contract(date=date.today(),
                        customer='Pedro Muramatsu', contract_type='NEW')

    contract.advance()

    history.add_state(contract.save_state())

    contract.advance()

    contract.customer = 'Muramatsu Pedro'

    history.add_state(contract.save_state())

    contract.advance()

    history.add_state(contract.save_state())

    contract.advance()

    history.add_state(contract.save_state())

    print(contract.contract_type)

    contract.restore_state(history.get_state(1))

    print(contract.contract_type)
    print(contract.customer)
