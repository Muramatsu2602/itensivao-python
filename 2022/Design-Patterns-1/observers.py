def print_receipt(receipt):
    print('Printing receipt %s' % (receipt.cnpj))


def send_by_email(receipt):
    print('Sending the following receipt by email: %s' % (receipt.cnpj))


def save_on_database(receipt):
    print('Saving receipt on Database %s' % (receipt.cnpj))
