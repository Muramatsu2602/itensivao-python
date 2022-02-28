class Budget(object):

    def __init__(self, value):  # __ private
        self.__value = value

    def value(self):
        return self.__value


budget = Budget(500)
budget.value = 200