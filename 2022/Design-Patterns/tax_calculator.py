from taxes import ISS_calc, ICMS_calc


class Tax_calculator(object):

    def tax_calc(self, budget, tax):

        if tax == 'ISS':
            tax_sum = ISS_calc(budget)

        elif tax == 'ICMS':
            tax_sum = ICMS_calc(budget)

        print(tax_sum)


if __name__ == '__main__':

    from budget import Budget

    calculator = Tax_calculator()

    budget = Budget(500)

    calculator.tax_calc(budget, 'ISS')
    calculator.tax_calc(budget, 'ICMS')
