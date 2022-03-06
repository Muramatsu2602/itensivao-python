from abc import ABCMeta, abstractmethod


class Tax(object):

    def __init__(self, other_tax=None):
        self.__other_tax = other_tax

    def calc_other_tax(self, budget):
        if self.__other_tax is None:
            return 0
        else:
            return self.__other_tax.calc(budget)

    @abstractmethod
    def calc(self, budget):
        pass


class Conditional_tax_template(Tax):

    __metaclass__ = ABCMeta  # so-called 'magic attribute'

    def calc(self, budget):
        if self.must_use_taxation(budget):
            return self.max_taxation(budget) + self.calc_other_tax(budget)
        else:
            return self.min_taxation(budget) + self.calc_other_tax(budget)

    @abstractmethod
    def must_use_taxation(self, budget):
        pass

    @abstractmethod
    def max_taxation(self, budget):
        pass

    @abstractmethod
    def min_taxation(self, budget):
        pass


def IPVX(method_or_function):
    def wrapper(self, budget):
        return method_or_function(self, budget) + 50.0
    return wrapper


class ISS(Tax):

    @IPVX
    def calc(self, budget):
        return budget.value * 0.1 + + self.calc_other_tax(budget)


class ICMS(Tax):

    def calc(self, budget):
        return budget.value * 0.06 + self.calc_other_tax(budget)


class ICPP(Conditional_tax_template):

    def must_use_taxation(self, budget):
        return budget.value > 500

    def max_taxation(self, budget):
        return budget.value * 0.07

    def min_taxation(self, budget):
        return budget.value * 0.05


class IKCV(Conditional_tax_template):

    def must_use_taxation(self, budget):
        return budget.value > 500 and self.__has_item_bigger_than_100_dollars(budget)

    def max_taxation(self, budget):
        return budget.value * 0.1

    def min_taxation(self, budget):
        return budget.value * 0.06

    def __has_item_bigger_than_100_dollars(self, budget):
        for item in budget.get_items():
            return item.value > 100
