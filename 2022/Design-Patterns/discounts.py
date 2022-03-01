class Discount_for_five_items(object):

    def calc(self, budget):

        if budget.num_items > 5:
            return budget.value * 0.1
        else:
            return 0


class Discount_for_more_than_five_hundred_dollars(object):

    def calc(self, budget):

        if budget.value > 500:
            return budget.value * 0.07
        else:
            return 0
