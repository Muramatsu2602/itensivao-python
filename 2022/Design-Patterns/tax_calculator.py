from taxes import ISS, ICMS, ICPP, IKCV


class Tax_calculator(object):

    def tax_calc(self, budget, tax):

        tax_sum = tax.calc(budget)

        print(tax_sum)


if __name__ == '__main__':

    from budget import Budget, Item

    calculator = Tax_calculator()

    budget = Budget()
    budget.add_item(Item('Item 1', 50))
    budget.add_item(Item('Item 2', 200))
    budget.add_item(Item('Item 3', 245))


    tax_list = [ISS, ICMS, ICPP, IKCV]

    for tax in tax_list:
        calculator.tax_calc(budget, tax)
