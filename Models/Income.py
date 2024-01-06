from Models import Transaction


class Income(Transaction.Transaction):

    def __init__(self, account_no, value, date, category, comment):
        super().__init__(account_no, 1, value, date, category, comment)

    def list_attributes(self):
        return (f"****** Transaction Id: {self.transaction_id} ******\n"
                f"     * Account: {self.account_no} * Value: {self.value}   * Date: {self.date}\n"
                f"     * Comment: {self.comment}")
