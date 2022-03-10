
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
