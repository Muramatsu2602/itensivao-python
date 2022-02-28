from taxes import ISS, ICMS


class Tax_calculator(object):

    def tax_calc(self, budget, tax):

        tax_sum = tax.calc(budget)

        print(tax_sum)


if __name__ == '__main__':

    from budget import Budget

    calculator = Tax_calculator()

    budget = Budget(500)

    calculator.tax_calc(budget, ISS)
    calculator.tax_calc(budget, ICMS)
