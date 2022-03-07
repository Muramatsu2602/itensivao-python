
class NormalQueue:

    code: int = 0
    queue = []
    served_customers = []
    current_password: str = ''

    def generateCurrentPassword(self) -> None:
        self.current_password = f'NM{self.code}'
