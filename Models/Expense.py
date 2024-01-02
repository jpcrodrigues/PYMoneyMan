import Transaction


class Income(Transaction):

    def __init__(self, value, date, categories, tag, comment):
        super().__init__(-1, value, date, categories, tag, comment)