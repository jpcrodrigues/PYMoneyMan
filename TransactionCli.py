import datetime

import Constants
from Utils import OsUtils as Os
from Controlers import TransactionController as TrxCtrl
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
    print(f"### LIST {transaction_type.upper()} RECORD(s) ###")

    account_number = input(f"Filter {transaction_type.lower()} records by account number (press enter to skip): ")

    if not account_number == "":
        list_of_transactions = TrxCtrl.read(transaction_type, account_no=account_number)
    else:
        transaction_id = input(f"Filter {transaction_type.lower()} records by id "
                               f"(press enter to skip): ")
        if not transaction_id == "":
            list_of_transactions = TrxCtrl.read(transaction_type, transaction_id=transaction_id)
        else:
            list_of_transactions = TrxCtrl.read(transaction_type)

    if len(list_of_transactions) == 0:
        print(f"There are no {transaction_type.lower()} records for the applied filters.")
    else:
        print(f"The existing {transaction_type.lower()} records are:")
        for transaction in list_of_transactions:
            print(f"******************************************************")
            print(transaction.list_attributes())
        print(f"******************************************************\n")

    input("(Press enter to continue)")


def __create(transaction_type):
    print(f"### CREATE AN {transaction_type.upper()} RECORD ###")

    option = input(f"Before creating an {transaction_type.lower()} record would you like "
                   f"to check all the existing acounts (type y + enter to list or enter to skip)?")

    if option.lower() == "y":
        list_of_accounts = AccCtrl.read()
        for account in list_of_accounts:
            print(f"******************************************************")
            print(account.to_string())
        print(f"******************************************************")

    # ACCOUNT NUMBER
    while True:
        number = input("Please insert the account number: ")

        if not number.isdigit():
            print("The account number must be a number.")
        elif len(AccCtrl.read(account_no=number)) == 0:
            print("The account number doesn't exist.")
        else:
            break

    # VALUE
    while True:
        try:
            value_float = float(input(f"Insert the {transaction_type.lower()} value: "))
            value = "{:.2f}".format(value_float)
            break
        except ValueError:
            print("The value must be a number")

    # DATE
    while True:
        try:
            date_str = input(f"Input the {transaction_type.lower()} record date (format YYYY/MM/DD): ")
            date = datetime.datetime.strptime(date_str, '%Y/%m/%d').date()
            break
        except ValueError:
            print("The value must be in the right format YYYY/MM/DD")

    # CATEGORY
    category = input("Insert a category and press enter (or press enter to skip): ")

    # COMMENT
    comment = input("Insert comment and press enter (or press enter to skip): ")

    transaction = None

    if transaction_type == Constants.TRANSACTION_TYPE_INCOME:
        transaction = Income(number, value, date, category, comment)

    if transaction_type == Constants.TRANSACTION_TYPE_EXPENSE:
        transaction = Expense(number, value, date, category, comment)

    print(f"You're about to register an {transaction_type.lower()} record :\n{transaction.list_attributes()}")
    proceed = input("Type Y and enter to save record: ")

    if proceed.lower() == "y":
        TrxCtrl.create(transaction)
        print(f"SUCCESS: {transaction_type.upper()} record registred sucessfully!")
    else:
        print(f"WARNING: {transaction_type.upper()} registration aborted!")

    input("(Press enter to continue)")


def __delete(transaction_type):
    print(f"### DELETE {transaction_type.upper()} RECORD ###")

    list_of_transactions = TrxCtrl.read(transaction_type)

    if len(list_of_transactions) == 0:
        print(f"There are no {transaction_type.lower()} records registered. Please register one {transaction_type.lower()} record first.")
        input("Press entrer to continue")
    else:
        print(f"\nWARNING: You're about to delete an {transaction_type.lower()} record.\n"
              "Are you sure you want to proceed?")

        option = input("(Type Y + enter to continue): ")

        if option.lower() == "y":
            while True:
                option = input(f"Delete {transaction_type.lower()} record by:\n"
                               "\t1 - Account Number;\n"
                               "or\n"
                               "\t2 - Transaction Id\n"
                               "\n"
                               "Select on option from above (1 or 2):")

                # DELETE THE TRANSACTION BY ACCOUNT NUMBER
                if option.lower() == "1":
                    option = input("Would you like to list the existing accounts before proceeding "
                                   "(press y + enter to list or enter only to skip)?")

                    if option.lower() == "y":
                        list_of_accounts = AccCtrl.read()
                        for account in list_of_accounts:
                            print(f"******************************************************\n")
                            print(account.to_string())
                        print(f"******************************************************")

                    while True:
                        account_no = input(f"Input the account number from above "
                                           f"to delete all the {transaction_type.lower()} records: ")
                        if not account_no.isdigit():
                            print("The account number must be a digit.")
                        else:
                            if len(AccCtrl.read(account_no=account_no)) > 0:
                                TrxCtrl.delete(transaction_type, account_no=account_no)
                                print(f"SUCCESS: All {transaction_type.lower()} records were deleted successfuly.")
                                input("(Press enter to continue)")
                                break
                            else:
                                print(f"There are no {transaction_type.lower()} records with that number.")
                                input("(Press enter to continue)")
                                break

                    break
                # DELETE THE TRANSACTION BY TRANSACTION ID
                elif option == "2":
                    option = input(f"Would you like to list the existing {transaction_type.lower()} records before "
                                   f"proceeding (press y + enter to list or enter only to skip)?")

                    if option.lower() == "y":
                        list_of_transactions = TrxCtrl.read(transaction_type)
                        for transaction in list_of_transactions:
                            print(f"******************************************************\n")
                            print(transaction.list_attributes())
                        print(f"******************************************************")

                    while True:
                        transaction_id = input(f"Input the {transaction_type.lower()} record id from above to delete: ")
                        if not transaction_id.isdigit():
                            print(f"The {transaction_type.lowe()} record id must be a digit.")
                        else:
                            if len(TrxCtrl.read(transaction_type, transaction_id=transaction_id)) > 0:
                                TrxCtrl.delete(transaction_type, transaction_id=transaction_id)
                                print(f"SUCCESS: The {transaction_type.lower()} record was deleted successfuly.")
                                input("(Press enter to continue)")
                                break
                            else:
                                print("There are no accounts with that number.")
                                input("(Press enter to continue)")
                                break
                    break
                else:
                    print("Please select one valid option.")
                    input("(Press entrer to continue)")
        else:
            print("WARNING: Delete operation canceled!")
            input("(Press enter to continue)")