import time


def generate_transaction_id():
    return int(hash(time.time()))


class Transaction(object):

    def __init__(self, account_no, sign, value, date, categorie, comment):
        self.transaction_id = generate_transaction_id()
        self.account_no = account_no
        self.sign = sign
        self.value = value
        self.date = date
        self.categories = categorie
        self.comment = comment

    def get_value(self):
        self.value = self.sign * self.value
        return self.value
