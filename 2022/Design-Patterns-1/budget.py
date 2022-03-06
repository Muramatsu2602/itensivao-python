from abc import ABCMeta, abstractmethod


class Budget_of_a_state(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def apply_extra_discount(self, budget):
        pass

    @abstractmethod
    def approve(self, budget):
        pass

    @abstractmethod
    def deny(self, budget):
        pass

    @abstractmethod
    def end(self, budget):
        pass


class In_approval(Budget_of_a_state):

    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.value * 0.02)

    def approve(self, budget):
        budget.current_state = Approval()

    def deny(self, budget):
        budget.current_state = Denied()

    def end(self, budget):
        raise Exception('A budget under approval cannot go to ended')


class Approval(Budget_of_a_state):

    def apply_extra_discount(self, budget):
        budget.add_extra_discount(budget.value * 0.05)

    def approve(self, budget):
        raise Exception('Budget has been already approved')

    def deny(self, budget):
        raise Exception('Approved Budgets cannot be denied')

    def end(self, budget):
        budget.current_state = Ended()


class Denied(Budget_of_a_state):

    def apply_extra_discount(self, budget):
        raise Exception(
            "Denied budgets shall not receive any additional discounts")

    def approve(self, budget):
        raise Exception('Denied Budget cannot be approved')

    def deny(self, budget):
        raise Exception('Denied Budget cannot be denied twice')

    def end(self, budget):
        budget.current_state = Ended()


class Ended(Budget_of_a_state):

    def apply_extra_discount(self, budget):
        raise Exception(
            "Ended budgets shall not receive any additional discounts")

    def approve(self, budget):
        raise Exception('Ended Budgets cannot be approved')

    def deny(self, budget):
        raise Exception('Ended Budgets cannot be denied')

    def end(self, budget):
        raise Exception('Ended Budgets cannot be ended twice')


class Budget(object):

    IN_APPROVAL = 1
    APPROVED = 2
    DENIED = 3
    ENDED = 4

    def __init__(self):  # __ private
        self.__items = []
        self.current_state = In_approval()
        self.__extra_discount = 0

    @property
    def num_items(self):
        return len(self.__items)

    @property
    def value(self):
        total = 0.0
        for item in self.__items:
            total += item.value

        return total - self.__extra_discount

    def approve(self):
        self.current_state.approve(budget)

    def deny(self):
        self.current_state.deny(budget)

    def end(self):
        self.current_state.end(budget)

    def apply_extra_discount(self):
        self.current_state.apply_extra_discount(self)

    def add_extra_discount(self, discount):
        self.__extra_discount += discount

    def get_items(self):
        return tuple(self.__items)

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

    if __name__ == "__main__":
        from budget import Item

        budget = Budget()
        budget.add_item(Item('Item 1', 50))
        budget.add_item(Item('Item 2', 200))
        budget.add_item(Item('Item 3', 245))

        print(budget.value)

        budget.apply_extra_discount()

        print(budget.value)
