class Print(object):

    def visit_sum(self, sum):
        print('(',  end=" ")
        # visits left expression
        print('+',  end=" ")
        # visits right expression
        print(')',  end=" ")

    def visit_subtraction(self, subtraction):
        print('(',  end=" ")
        # visits left expression
        print('-',  end=" ")
        # visits right expression
        print(')',  end=" ")

    def visit_number(self, number):

        print(number.evaluate(),  end=" ")
