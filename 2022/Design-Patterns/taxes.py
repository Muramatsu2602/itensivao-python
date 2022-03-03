from abc import ABCMeta, abstractmethod

__metaclass__ = ABCMeta  # so-called 'magic attribute'


class Conditional_tax_template(object):

    def calc(self, budget):

        if self.must_use_taxation(budget):
            return self.max_taxation(budget)
        else:
            return self.min_taxation(budget)

    @abstractmethod
    def must_use_taxation(budget):
        pass

    @abstractmethod
    def max_taxation(budget):
        pass

    @abstractmethod
    def min_taxation(budget):
        pass


class ISS(object):

    def calc(self, budget):

        return budget.value * 0.1


class ICMS(object):

    def calc(self, budget):

        return budget.value * 0.06


class ICPP(Conditional_tax_template):

    def calc(self, budget):

        if budget.value > 500:
            return budget.value * 0.07
        else:
            return budget.value * 0.05

    def must_use_taxation(budget):
        pass

    def max_taxation(budget):
        pass

    def min_taxation(budget):
        pass


class IKCV(Conditional_tax_template):

    def calc(self, budget):

        if budget.value > 500 and self.__has_item_bigger_than_100_dollars(budget):
            return budget.value * 0.1
        else:
            return budget.value * 0.06

    def must_use_taxation(budget):
        pass

    def max_taxation(budget):
        pass

    def min_taxation(budget):
        pass

    def __has_item_bigger_than_100_dollars(self, budget):

        for item in budget.get_items():
            if item.value > 100:
                return True

            return False
