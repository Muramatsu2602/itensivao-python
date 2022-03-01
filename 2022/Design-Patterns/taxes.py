from matplotlib.pyplot import cla
from sqlalchemy import false


class Conditional_tax_template(object):

    def calc(self, budget):

        if self.must_use_taxation(budget):
            return self.max_taxation(budget)
        else:
            return self.min_taxation(budget)


class ISS(object):

    def calc(self, budget):

        return budget.value * 0.1


class ICMS(object):

    def calc(self, budget):

        return budget.value * 0.06


class ICPP(object):

    def calc(self, budget):

        if budget.value > 500:
            return budget.value * 0.07
        else:
            return budget.value * 0.05


class IKCV(object):

    def calc(self, budget):

        if budget.value > 500 and self.__has_item_bigger_than_100_dollars(budget):
            return budget.value * 0.1
        else:
            return budget.value * 0.06

    def __has_item_bigger_than_100_dollars(self, budget):

        for item in budget.get_items():
            if item.value > 100:
                return True

            return False
