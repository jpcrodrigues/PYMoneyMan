from Models import Transaction


class Expense(Transaction.Transaction):

    def __init__(self, account_no, sign, value, date, categorie, comment):
        super().__init__(account_no, sign, value, date, categorie, comment)
