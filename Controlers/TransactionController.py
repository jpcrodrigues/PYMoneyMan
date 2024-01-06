import Constants
from Utils import CSVUtils as CsvU
from Models.Income import Income
from Models.Expense import Expense

file_name = "Data/transaction.csv"


def reade(transaction_type, transaction_id=None, account_no=None):
    transaction = None
    list_of_results = CsvU.read_file(file_name)
    list_of_transactions = []

    for result in list_of_results:
        trans_id = result[0]
        acc_number = result[1]
        sign = result[2]
        value = result[3]
        date = result[4]
        category = result[5]
        comment = result[6]

        # if the account number or name are filled then filter the results by the filter
        if ((transaction_id is not None and transaction_id == trans_id
                or account_no is not None and account_no == acc_number)
                or transaction_id is None and account_no is None):

            if transaction_type == Constants.TRANSACTION_TYPE_INCOME and int(sign) == 1:
                transaction = Income(acc_number, value, date, category, comment)

            if transaction_type == Constants.TRANSACTION_TYPE_EXPENSE and int(sign) == -1:
                transaction = Expense(acc_number, value, date, category, comment)

            if transaction is not None:
                transaction.set_transaction_id(trans_id)
                list_of_transactions.append(transaction)

    return list_of_transactions


def create(transaction):
    data = [transaction.transaction_id,
            transaction.account_no,
            transaction.sign,
            transaction.value,
            transaction.date,
            transaction.category,
            transaction.comment]
    CsvU.write_record(file_name, data)


def delete(transaction_id=None, account_nos=None):
    """id_list = [account_no]
    CsvU.delete_records_by_ids(file_name, id_list)"""
