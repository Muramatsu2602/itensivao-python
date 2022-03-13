import requests


class FindAddress:

    def __init__(self, cep):
        if self.cep_is_valid(str(cep)):
            self.cep = str(cep)
        else:
            raise ValueError("CEP is Invalid!")
