

class Discount_calculator:

    def calc(self, budget):

        if budget.num_items > 5:
            return budget.value * 0.1

        elif budget.value > 500:
            return budget.value * 0.07


if __name__ == '__main__':

    from budget import Budget, Item

    budget = Budget()
    budget.add_item(Item('ITEM - 1', 100))
    budget.add_item(Item('ITEM - 2', 50))
    budget.add_item(Item('ITEM - 2', 400))

    discount_calc = Discount_calculator()
    discount = discount_calc.calc(budget)

    print('Calculated discount: %.4s' % (discount))