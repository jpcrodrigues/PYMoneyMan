import Constants
from Utils import OsUtils as Os
import AccountCli as AccCli
import TransactionCli as TrxCli


def main():
    while True:
        Os.clear()
        print("""
          _______ ___ ___ ___ ___                         ___ ___             
         |   _   |   Y   |   Y   .-----.-----.-----.--.--|   Y   .---.-.-----.
         |.  1   |   1   |.      |  _  |     |  -__|  |  |.      |  _  |     |
         |.  ____|\_   _/|. \_/  |_____|__|__|_____|___  |. \_/  |___._|__|__|
         |:  |     |:  | |:  |   |                 |_____|:  |   |            
         |::.|     |::.| |::.|:. |                       |::.|:. |            
         `---'     `---' `--- ---'                       `--- ---'            
        """)
        print("Program options: ")
        print(" 1 - Manage Account(s)")
        print(" 2 - Manage Income(s)")
        print(" 3 - Manage Expense(s)")
        print(" 4 - Exit")
        option = input("Select one option: ")

        match option:
            case "1":
                __manage_account()
            case "2":
                __manage_income()
            case "3":
                __manage_expense()
            case "4":
                if __leavin():
                    exit()
            case _:
                print("Please insert select a valid option.")


def __manage_account():
    AccCli.main()


def __manage_income():
    TrxCli.main(Constants.TRANSACTION_TYPE_INCOME)


def __manage_expense():
    TrxCli.main(Constants.TRANSACTION_TYPE_EXPENSE)


def __leavin():
    option = input("Are you sure you want to leave? (Y + Enter for Yes): ")
    if option.lower() == "y":
        return True
    else:
        return False


if __name__ == '__main__':
    main()
