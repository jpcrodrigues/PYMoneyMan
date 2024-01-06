from Utils import CSVUtils as CsvU
from Models.Account import Account

file_name = "Data/accounts.csv"


def reade(account_no=None, account_name=None):
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
        if  account_no is not None and account_no == number or account_name is not None and account_name == name:
            account = Account(number, name, type, init_value, currency, color)
            list_of_accounts.append(account)
        if account_no is None and account_name is None:
            account = Account(number, name, type, init_value, currency, color)
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
