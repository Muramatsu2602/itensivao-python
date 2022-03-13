from validate_docbr import CPF, CNPJ

class Document:
    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocCPF(document)
            