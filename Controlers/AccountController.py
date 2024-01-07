import Constants
from Utils import CSVUtils as CsvU
from Models.Account import Account
from Controlers import TransactionController as TrxCtrl

file_name = "Data/accounts.csv"


def system_has_records():
    list_of_accounts = read()
    if len(list_of_accounts) > 0:
        return True
    else:
        return False


def read(account_no=None, account_name=None):
    list_of_results = CsvU.read_file(file_name)
    list_of_accounts = []

    for result in list_of_results:
        number = result[0]
        name = result[1]
        type = result[2]
        init_value = result[3]
        currency = result[4]
        color = result[5]

        # if the account number or name are filled then filter the results by the filter
        if ((account_no is not None and account_no == number or account_name is not None and account_name == name)
                or account_no is None and account_name is None):
            account = Account(number, name, type, init_value, currency, color)
            # fill the expenses and incomes to update the account balance
            account.set_incomes(TrxCtrl.read(Constants.TRANSACTION_TYPE_INCOME, account_no=number))
            account.set_expenses(TrxCtrl.read(Constants.TRANSACTION_TYPE_EXPENSE, account_no=number))
            list_of_accounts.append(account)

    return list_of_accounts


def create(account):
    data = [account.number, account.name, account.type, account.init_value, account.currency, account.color]
    CsvU.write_record(file_name, data)


def update(account):
    data = [account.number, account.name, account.type, account.init_value, account.currency, account.color]
    CsvU.update_record(file_name, data)


def delete(account_no):
    id_list = [account_no]
    CsvU.delete_records_by_ids(file_name, id_list)
