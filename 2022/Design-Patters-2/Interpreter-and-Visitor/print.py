class Print(object):

    def visit_sum(self, sum):
        print('(',  end=" ")
        sum.left_expression.accepts(self)
        print('+',  end=" ")
        sum.right_expression.accepts(self)
        print(')',  end=" ")

    def visit_subtraction(self, subtraction):
        print('(',  end=" ")
        subtraction.left_expression.accepts(self)
        print('-',  end=" ")
        subtraction.right_expression.accepts(self)

        print(')',  end=" ")

    def visit_number(self, number):

        print(number.evaluate(),  end=" ")
