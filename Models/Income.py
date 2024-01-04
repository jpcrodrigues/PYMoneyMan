from Models import Transaction


class Income(Transaction.Transaction):

    def __init__(self, account_no, value, date, categorie, comment):
        super().__init__(account_no, 1, value, date, categorie, comment)

    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    def list_attributes(self):
        return (f"****** Transaction Id: {self.transaction_id} ******\n"
                f"     * Account: {self.account_no} * Value: {self.value}   * Date: {self.date}\n"
                f"     * Comment: {self.comment}")
