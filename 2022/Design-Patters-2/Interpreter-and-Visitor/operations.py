from ast import Sub


class Subtraction(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def evaluate(self):
        return self.__left_expression.evaluate() - self.__right_expression.evaluate()

    @property
    def left_expression(self):
        return self.__left_expression

    @property
    def right_expression(self):
        return self.__right_expression

    def accepts(self, visitor):
        visitor.visit_subtraction(self)


class Sum(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def evaluate(self):
        return self.__left_expression.evaluate() + self.__right_expression.evaluate()

    @property
    def left_expression(self):
        return self.__left_expression

    @property
    def right_expression(self):
        return self.__right_expression

    def accepts(self, visitor):
        visitor.visit_sum(self)


class TheNumber(object):

    def __init__(self, number):
        self.__number = number

    def evaluate(self):
        return self.__number

    def accepts(self, visitor):
        visitor.visit_number(self)


if __name__ == '__main__':

    from print import Print

    left_expression = Sum(TheNumber(10), TheNumber(20))
    right_expression = Sum(TheNumber(5), TheNumber(2))
    problem_expression = Sum(left_expression, right_expression)

    print = Print()
    problem_expression.accepts(print)
