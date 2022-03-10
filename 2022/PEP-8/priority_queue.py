class PriorityQueue:
    code: int = 0
    queue = []
    served_customers = []
    current_password: str = ''

    def generate_current_password(self):
        