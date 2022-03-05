from abc import ABCMeta, abstractmethod

__metaclass__ = ABCMeta  # so-called 'magic attribute'


class Conditional_tax_template(object):

    def calc(self, budget):
        if self.must_use_taxation(budget):
            return self.max_taxation(budget)
        else:
            return self.min_taxation(budget)

    @abstractmethod
    def must_use_taxation(self, budget):
        pass

    @abstractmethod
    def max_taxation(self, budget):
        pass

    @abstractmethod
    def min_taxation(self, budget):
        pass


class ISS(object):

    def calc(self, budget):
        return budget.value * 0.1


class ICMS(object):

    def calc(self, budget):
        return budget.value * 0.06


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
