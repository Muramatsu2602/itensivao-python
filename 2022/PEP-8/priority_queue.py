import statistics

from pandas import array


class PriorityQueue:
    code: int = 0
    queue = []
    served_customers = []
    current_password: str = ''

    def generate_current_password(self) -> None:
        self.current_password = f'NM{self.code}'

    def reset_queue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def update_queue(self) -> None:
        self.reset_queue()
        self.generate_current_password()
        self.queue.append(self.current_password)

    def call_customer(self, counter: int) -> str:
        current_costumer = self.queue.pop()
        self.served_customers.append(current_costumer)

        return(f'Current costumer: {current_costumer}, please go to {counter}')

    def statistics(self, day: str, agency: int, flag: str) -> str or array:

        if flag != 'detail':
            statistics = {f'{agency}-{day}': len(self.served_customers)}
        else:
            # creating a dictionary
            statistics = {}
            statistics['day'] = day
            statistics['agency'] = agency
            statistics['served_costumers'] = self.served_customers
            statistics['num_served_costumers'] = len(self.served_customers)

        return statistics
