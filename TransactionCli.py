import datetime

import Constants
from Utils import OsUtils as Os
from Controlers import TransactionController as TrxController
from Controlers import AccountController as AccCtrl
from Models.Income import Income
from Models.Expense import Expense


def main(transaction_type):
    go_back = False

    while not go_back:
        Os.clear()
        print(f"### {transaction_type.upper()} OPTIONS ###")
        print(f"1 - List {transaction_type.lower()} record(s)")
        print(f"2 - Create an {transaction_type.lower()} record(s)")
        print(f"3 - Delete an {transaction_type.lower()} record(s)")
        print("4 - Go back")

        option = input("Select one option: ")

        match option:
            case "1":
                __list(transaction_type)
            case "2":
                __create(transaction_type)
            case "3":
                __delete(transaction_type)
            case "4":
                go_back = True
                break
            case _:
                print("Please insert a valid option.")


def __list(transaction_type):
    print(f"### LIST INCOME RECORD(s) ###")

    account_number = input("Filter income transactions by account number (press enter to skip): ")

    if not account_number == "":
        list_of_income = TrxController.reade(transaction_type, account_no=account_number)
    else:
        transaction_id = input("Filter income records by income transaction id (press enter to skip): ")
        if not transaction_id == "":
            list_of_income = TrxController.reade(transaction_type, transaction_id=transaction_id)
        else:
            list_of_income = TrxController.reade(transaction_type)

    if len(list_of_income) == 0:
        print("There are no income transactions for the applied filters.")
    else:
        print("The existing income records are:")
        for income in list_of_income:
            print(f"******************************************************")
            print(income.list_attributes())
        print(f"******************************************************\n")

    input("(Press enter to continue)")


def __create(transaction_type):
    print("### CREATE AN INCOME RECORD ###")

    option = input(f"Before creating an income record would you like to check all the existing acounts? "
                   f"(type y + enter to list or enter to skip)")

    if option.lower() == "y":
        list_of_accounts = AccCtrl.reade()
        for account in list_of_accounts:
            print(f"******************************************************")
            print(account.to_string())
        print(f"******************************************************")

    # ACCOUNT NUMBER
    while True:
        number = input("Please insert the account number: ")

        if not number.isdigit():
            print("The account number must be a number.")
        elif len(AccCtrl.reade(account_no=number)) == 0:
            print("The account number doesn't exist.")
        else:
            break

    # VALUE
    while True:
        try:
            value_float = float(input("Insert the income value: "))
            value = "{:.2f}".format(value_float)
            break
        except ValueError:
            print("The value must be a number")

    # DATE
    while True:
        try:
            date_str = input("Input the icome record date (format YYYY/MM/DD): ")
            date = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
            break
        except ValueError:
            print("The value must be in the right format YYYY/MM/DD")

    # CATEGORY
    category = input("Insert a category and press enter (or press enter to skip): ")

    # COMMENT
    comment = input("Insert comment and press enter (or press enter to skip): ")

    if transaction_type == Constants.TRANSACTION_TYPE_INCOME:
        transaction = Income(number, value, date, category, comment)

    if transaction_type == Constants.TRANSACTION_TYPE_EXPENSE:
        transaction = Expense(number, value, date, category, comment)

    print(f"You're about to register the icome record :\n{transaction.list_attributes()}")
    proceed = input("Type Y and enter to save record: ")

    if proceed.lower() == "y":
        TrxController.create(transaction)
        print("SUCCESS: Income record registred sucessfully!")
    else:
        print("WARNING: Account registration aborted!")

    input("(Press enter to continue)")


def __delete(transaction_type):
    TrxController.delete()