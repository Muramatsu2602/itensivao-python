
class NormalQueue:

    code: int = 0
    queue = []
    served_customers = []
    current_password: str = ''

    def generateCurrentPassword(self) -> None:
        self.current_password = f'NM{self.code}'

    def resetQueue(self) -> None:
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def updateQueue(self) -> None:
        self.resetQueue()
        self.generateCurrentPassword()
        self.queue.append(self.current_password)

    def callCustomer(self, counter: int) -> str:
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
