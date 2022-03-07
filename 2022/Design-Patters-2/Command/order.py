from abc import ABCMeta, abstractclassmethod, abstractmethod
from datetime import date


class Order(object):

    def __init__(self, customer, value):
        self.__customer = customer
        self.__value = value
        self.__status = 'NEW'
        self.__completed_date = None

    def pay(self):
        self.__status = 'PAID'

    def complete(self):
        self.__completed_date = date.today()
        self.__status = 'DELIVERED'

    @property
    def customer(self):
        return self.__customer

    @property
    def status(self):
        return self.__status

    @property
    def completed_date(self):
        return self.__completed_date


class Command(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class Complete_order(Command):

    def __init__(self, order):
        self.__order = order

    def execute(self):
        self.__order.complete()


class Pay_order(Command):

    def __init__(self, order):
        self.__order = order

    def execute(self):
        self.__order.pay()


class Work_queue(object):

    def __init__(self):
        self.__commands = []

    def add(self, command):
        self.__commands.append(command)

    def process(self):
        for command in self.__commands:
            command.execute()


if __name__ == '__main__':

    order1 = Order('John', 200)
    order2 = Order('Marcus', 400)

    work_queue = Work_queue()
    work_queue.add(Complete_order(order1))
    work_queue.add(Pay_order(order1))
    work_queue.add(Complete_order(order2))

    work_queue.process()
