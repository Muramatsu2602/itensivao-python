
class NormalQueue:

    code: int = 0
    queue = []
    served_customers = []
    current_password: str = ''

    def generateCurrentPassword(self) -> None:
        self.current_password = f'NM{self.code}'

    def resetQueue(self):
        if self.code >= 100:
            self.code = 0
        else:
            self.code += 1

    def updateQueue(self):
        self.resetQueue()
        self.generateCurrentPassword()
        self.queue.append(self.current_password)
