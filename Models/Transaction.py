import time


def generate_transaction_id():
    return str(hash(time.time()))[0:16]


class Transaction(object):

    def __init__(self, account_no, sign, value, date, category, comment):
        self.transaction_id = generate_transaction_id()
        self.account_no = account_no
        self.sign = sign
        self.value = value
        self.date = date
        self.category = category
        self.comment = comment

    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    def get_value(self):
        self.value = self.sign * self.value
        return self.value
