from Utils import CSVUtils as CsvU
from Models.Income import Income
from datetime import datetime

file_name = "Data/income.csv"


# --> print a date to string
# print(str(datetime.datetime(2008, 11, 22, 19, 53, 42).strftime('%Y-%m-%d')))
# --> get a date object out of a string
# print(datetime.strptime('2023-02-28', '%Y-%m-%d'))


def reade(transaction_id=None, account_no=None):
    list_of_results = CsvU.read_file(file_name)
    list_of_income_transactions = []

    for result in list_of_results:
        # we will skipp the id
        trans_id = result[0]
        acc_number = result[1]
        sign = result[2]
        value = result[3]
        date = result[4]
        categorie = result[5]
        comment = result[6]

        # if the account number or name are filled then filter the results by the filter
        if (transaction_id is not None and transaction_id == trans_id
                or account_no is not None and account_no == acc_number):
            income_transaction = Income(acc_number, value, date, categorie, comment)
            income_transaction.set_transaction_id(trans_id)
            list_of_income_transactions.append(income_transaction)
        if transaction_id is None and account_no is None:
            income_transaction = Income(acc_number, value, date, categorie, comment)
            income_transaction.set_transaction_id(trans_id)
            list_of_income_transactions.append(income_transaction)

    return list_of_income_transactions


def create(income):
    """data = [income.
            income.account_no,
            income.name, account.type, account.init_value, account.currency, account.color]
    CsvU.write_record(file_name, data)"""


def delete(account_no=None, transaction_id=None):
    """id_list = [account_no]
    CsvU.delete_records_by_ids(file_name, id_list)"""
