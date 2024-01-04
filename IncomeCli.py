from Utils import OsUtils as Os
from Controlers import IncomeController as IncCtrl


def main():
    go_back = False

    while not go_back:
        Os.clear()
        print("### INCOME OPTIONS ###")
        print("1 - List income records")
        print("2 - Register a new income record")
        print("3 - Delete one income record")
        print("4 - Go back")

        option = input("Select one option: ")

        match option:
            case "1":
                __list_income()
            case "2":
                __create_income()
            case "3":
                __delete_income()
            case "4":
                go_back = True
                break
            case _:
                print("Please insert a valid option.")


def __list_income():
    print("### LIST INCOME ###")

    account_number = input("Filter income transactions by account number (press enter to skip): ")

    if not account_number == "":
        list_of_income = IncCtrl.reade(account_no=account_number)
    else:
        transaction_id = input("Filter income records by income transaction id (press enter to skip): ")
        if not transaction_id == "":
            list_of_income = IncCtrl.reade(transaction_id=transaction_id)
        else:
            list_of_income = IncCtrl.reade()

    if len(list_of_income) == 0:
        print("There are no income transactions for the applied filters.")
    else:
        print("The existing income records are:")
        for income in list_of_income:
            print(f"******************************************************")
            print(income.list_attributes())
        print(f"******************************************************\n")

    input("(Press enter to continue)")


def __create_income():
    IncCtrl.create()


def __delete_income():
    IncCtrl.delete()
