class Discount_for_five_items(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calc(self, budget):

        if budget.num_items > 5:
            return budget.value * 0.1
        else:
            return self.__next_discount.calc(budget)


class Discount_for_more_than_five_hundred_dollars(object):

    def __init__(self, next_discount):
        self.__next_discount = next_discount

    def calc(self, budget):

        if budget.value > 500:
            return budget.value * 0.07
        else:
            return self.__next_discount.calc(budget)


class No_discount(object):

    def calc(self, budget):
        return 0
