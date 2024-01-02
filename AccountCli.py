from Utils import OsUtils as Os
from Controlers import AccountController as AccCtrl
from Models.Account import Account as Acc


# if There are no registered accounts print there are no registed accounts yet
# if there are registered accounts print the list

# options:
#  1 - List by name or number (if no parameter list all)
#  2 - Create
#  3 - Update
#  4 - Delete


def main():
    go_back = False

    while not go_back:
        Os.clear()
        print("### ACCOUNT OPTIONS ###")
        print("1 - List accounts")
        print("2 - Create a new account")
        print("3 - Update an existing account")
        print("4 - Delete an account")
        print("5 - Go back")

        option = input("Select one option: ")

        match option:
            case "1":
                __list_account()
            case "2":
                __create_account()
            case "3":
                __update_account()
            case "4":
                __delete_account()
            case "5":
                go_back = True
                break
            case _:
                print("Please insert a valid option.")


def __list_account():
    print("### LIST ACCOUNTS ###")

    account_number = input("Filter by account number (press enter to skip): ")

    if not account_number == "":
        list_of_accounts = AccCtrl.reade(account_no=account_number)
    else:
        account_name = input("Filter by account name (press enter to skip): ")
        if not account_name == "":
            list_of_accounts = AccCtrl.reade(account_name=account_name)
        else:
            list_of_accounts = AccCtrl.reade()

    if len(list_of_accounts) == 0:
        print("There are no accounts for the applied filters.")
    else:
        print("The existing accounts are:")
        for account in list_of_accounts:
            print(account.to_string())

    input("(Press enter to continue)")


def __create_account():
    print("### CREATE ACCOUNT ###")
    while True:
        number = input("Please insert the account number: ")

        if not number.isdigit():
            print("The account number must be a number.")
        elif len(AccCtrl.reade(number)) > 0:
            print("There is an account registered with the same number, please insert a diferent value.")
        else:
            break

    name = input("Insert the account name: ")

    while True:
        option = input("Select one of the account type:\n"
                       "1 - BANK\n"
                       "2 - INVESTMENT\n"
                       "3 - FUND\n"
                       "4 - CRYPTO\n"
                       "5 - LENDING\n")

        if option == "1":
            acc_type = "BANK"
            break
        elif option == "2":
            acc_type = "INVESTMENT"
            break
        elif option == "3":
            acc_type = "FUND"
            break
        elif option == "4":
            acc_type = "CRYPTO"
            break
        elif option == "5":
            acc_type = "LENDING"
            break
        else:
            print("Invalid option.")

    while True:
        init_value = input("Type the initial value of the account: ")  # must be an integer
        if not init_value.isdigit():
            print("The account initial value must be a number.")
        else:
            break

    while True:
        option = input("Select one of the currencies:\n"
                       "1 - US Dollar\n"
                       "2 - Euro\n"
                       "3 - British Pound Sterling\n"
                       "4 - Swiss Franc\n"
                       "5 - Japanese Yen\n")

        if option == "1":
            currency = "USD"
            break
        elif option == "2":
            currency = "EUR"
            break
        elif option == "3":
            currency = "GBP"
            break
        elif option == "4":
            currency = "CHF"
            break
        elif option == "5":
            currency = "JPY"
            break
        else:
            print("Invalid option.")

    while True:
        option = input("Select one of possible colors:\n"
                       "1 - RED\n"
                       "2 - GREEN\n"
                       "3 - WHITE\n"
                       "4 - BLUE\n"
                       "5 - PINK\n"
                       "6 - ORANGE\n"
                       "7 - BLACK\n"
                       "8 - GRAY\n")

        if option == "1":
            color = "RED"
            break
        elif option == "2":
            color = "GREEN"
            break
        elif option == "3":
            color = "WHITE"
            break
        elif option == "4":
            color = "BLUE"
            break
        elif option == "5":
            color = "PINK"
            break
        elif option == "6":
            color = "ORANGE"
            break
        elif option == "7":
            color = "BLACK"
            break
        elif option == "8":
            color = "GRAY"
            break
        else:
            print("Invalid option.")

    account = Acc(number, name, acc_type, init_value, currency, color)

    print(f"You're about to register the following account:\n{account.list_attributes()}")
    proceed = input("Type Y and enter to save record: ")

    if proceed.lower() == "y":
        AccCtrl.create(account)
        print("SUCCESS: Account registred sucessfully!")
    else:
        print("WARNING: Account registration aborted!")

    input("(Press enter to continue)")


def __update_account():
    print("### UPDATE ACCOUNT ###")

    list_of_accounts = AccCtrl.reade()
    if len(list_of_accounts) == 0:
        print("There are no accounts registered at the moment, please create an account first.")
    else:
        print("The existing accounts are:")
        for account in list_of_accounts:
            print(account.to_string())

        while True:
            account_no = input("Input the account number from the list above: ")
            if not account_no.isdigit():
                print("The account number must be a digit.")
            else:
                list_of_accounts = AccCtrl.reade(account_no=account_no)
                if len(list_of_accounts) > 0:
                    existing_account = list_of_accounts[0]

                    # ACCOUNT NAME
                    option = input(f"The account name is '{existing_account.name}',"
                                   f" replace the current value? (press Y + enter)")

                    if option.lower() == "y":
                        name = input("Input the new account name: ")
                    else:
                        name = existing_account.name

                    # ACCOUNT TYPE
                    option = input(f"The account type is '{existing_account.type}',"
                                   f" replace the current value? (press Y + enter)")

                    if option.lower() == "y":
                        while True:
                            option = input("Select the new account type:\n"
                                           "1 - BANK\n"
                                           "2 - INVESTMENT\n"
                                           "3 - FUND\n"
                                           "4 - CRYPTO\n"
                                           "5 - LENDING\n")

                            if option == "1":
                                acc_type = "BANK"
                                break
                            elif option == "2":
                                acc_type = "INVESTMENT"
                                break
                            elif option == "3":
                                acc_type = "FUND"
                                break
                            elif option == "4":
                                acc_type = "CRYPTO"
                                break
                            elif option == "5":
                                acc_type = "LENDING"
                                break
                            else:
                                print("Invalid option.")
                    else:
                        acc_type = existing_account.type

                    # INITIAL VALUE
                    option = input(f"The current account initial value is '{existing_account.init_value}',"
                                   f" replace the current value? (press Y + enter)")

                    if option.lower() == "y":
                        while True:
                            init_value = input("Type the new initial value of the account: ")  # must be an integer
                            if not init_value.isdigit():
                                print("The account initial value must be a number.")
                            else:
                                break
                    else:
                        init_value = existing_account.init_value

                    # CURRENCY
                    option = input(f"The current accout currency is '{existing_account.currency}',"
                                   f" replace the current value? (press Y + enter)")

                    if option.lower() == "y":
                        while True:
                            option = input("Select the new currency for the account:\n"
                                           "1 - US Dollar\n"
                                           "2 - Euro\n"
                                           "3 - British Pound Sterling\n"
                                           "4 - Swiss Franc\n"
                                           "5 - Japanese Yen\n")

                            if option == "1":
                                currency = "USD"
                                break
                            elif option == "2":
                                currency = "EUR"
                                break
                            elif option == "3":
                                currency = "GBP"
                                break
                            elif option == "4":
                                currency = "CHF"
                                break
                            elif option == "5":
                                currency = "JPY"
                                break
                            else:
                                print("Invalid option.")
                    else:
                        currency = existing_account.currency

                    # COLOR
                    option = input(f"The current accout color is '{existing_account.color}',"
                                   f" replace the current value? (press Y + enter)")

                    if option.lower() == "y":
                        while True:
                            option = input("Select one of possible colors:\n"
                                           "1 - RED\n"
                                           "2 - GREEN\n"
                                           "3 - WHITE\n"
                                           "4 - BLUE\n"
                                           "5 - PINK\n"
                                           "6 - ORANGE\n"
                                           "7 - BLACK\n"
                                           "8 - GRAY\n")

                            if option == "1":
                                color = "RED"
                                break
                            elif option == "2":
                                color = "GREEN"
                                break
                            elif option == "3":
                                color = "WHITE"
                                break
                            elif option == "4":
                                color = "BLUE"
                                break
                            elif option == "5":
                                color = "PINK"
                                break
                            elif option == "6":
                                color = "ORANGE"
                                break
                            elif option == "7":
                                color = "BLACK"
                                break
                            elif option == "8":
                                color = "GRAY"
                                break
                            else:
                                print("Invalid option.")
                    else:
                        color = existing_account.color

                    account = Acc(existing_account.number,
                                  name,
                                  acc_type,
                                  init_value,
                                  currency,
                                  color)

                    option = input(f"WARNING: The new account will have the following values:\n{account.list_attributes()}"
                                   f"\n\n(Type Y + enter to continue): ")

                    if option.lower() == "y":
                        AccCtrl.update(account)
                        print("SUCCESS: Account updated successfuly.")
                    else:
                        print("WARNING: Account update aborted!")

                    input("(Press entre to continue)")
                    break
                else:
                    print("There are no accounts with that number.")
                    input("(Press entre to continue)")
                    break


def __delete_account():
    print("### DELETE ACCOUNT ###")

    print("\nWARNING: Deleting an account will also delete all income and expenses records.\n"
          "Are you sure you want to proceed?")

    option = input("(Type Y + enter to continue): ")

    if option.lower() == "y":
        list_of_accounts = AccCtrl.reade()
        if len(list_of_accounts) == 0:
            print("There are no accounts registered at the moment, please create an account first.")
        else:
            print("The existing accounts are:")
            for account in list_of_accounts:
                print(account.to_string())

            while True:
                account_no = input("Input the account number from the list above: ")
                if not account_no.isdigit():
                    print("The account number must be a digit.")
                else:
                    if len(AccCtrl.reade(account_no=account_no)) > 0:
                        # TODO detele the existing records from the CSV file
                        AccCtrl.delete(account_no)
                        print("SUCCESS: Account deleted successfuly.")
                        input("(Press entre to continue)")
                        break
                    else:
                        print("There are no accounts with that number.")
                        input("(Press entre to continue)")
                        break

    else:
        print("WARNING: Delete operation canceled!")
        input("(Press enter to continue)")