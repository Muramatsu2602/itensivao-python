from discounts import Discount_for_five_items, Discount_for_more_than_five_hundred_dollars, No_discount


class Discount_calculator:

    def calc(self, budget):
        discount = Discount_for_five_items(
            Discount_for_more_than_five_hundred_dollars(No_discount())).calc(budget)

        return discount


if __name__ == '__main__':

    from budget import Budget, Item

    budget = Budget()
    budget.add_item(Item('ITEM - 1', 100))
    budget.add_item(Item('ITEM - 2', 50))
    budget.add_item(Item('ITEM - 2', 400))

    discount_calc = Discount_calculator()
    discount = discount_calc.calc(budget)

    print('Calculated discount: %.4s' % (discount))
