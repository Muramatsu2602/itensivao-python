from ast import Sub


class Subtraction(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def evaluate(self):
        return self.__left_expression.evaluate() - self.__right_expression.evaluate()


class Sum(object):

    def __init__(self, left_expression, right_expression):
        self.__left_expression = left_expression
        self.__right_expression = right_expression

    def evaluate(self):
        return self.__left_expression.evaluate() + self.__right_expression.evaluate()


class TheNumber(object):

    def __init__(self, number):
        self.__number = number

    def evaluate(self):
        return self.__number


if __name__ == '__main__':

    left_expression = Sum(TheNumber(10), TheNumber(20))
    right_expression = Sum(TheNumber(5), TheNumber(2))
    problem_expression = Sum(left_expression, right_expression)

    print(problem_expression.evaluate())

    problem_expression_2 = Subtraction(TheNumber(100), TheNumber(40))

    print(problem_expression_2.evaluate())
