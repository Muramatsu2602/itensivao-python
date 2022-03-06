class Budget(object):

    IN_APPROVAL = 1
    APPROVED = 2
    DENIED = 3
    ENDED = 4

    def __init__(self):  # __ private
        self.__items = []
        self.current_state = Budget.IN_APPROVAL
        self.__extra_discount = 0

    def apply_extra_discount(self):
        if self.current_state == Budget.IN_APPROVAL:
            self.__extra_discount += self.value * 0.02
        
        elif self.current_state == Budget.APPROVED:
            self.__extra_discount += self.value * 0.05
        
        elif self.__extra_discount == Budget.DENIED:
            raise Exception("Denied budgets shall not receive any additional discounts")
        
        elif self.__extra_discount == Budget.ENDED:
            raise Exception("Ended budgets shall not receive any additional discounts")

    @property
    def value(self):
        total = 0.0
        for item in self.__items:
            total += item.value

        return total

    def get_items(self):

        return tuple(self.__items)

    @property
    def num_items(self):
        return len(self.__items)

    def add_item(self, item):
        self.__items.append(item)


class Item(object):

    def __init__(self, name, value):
        self.__name = name
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name
