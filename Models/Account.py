class Account:

    def __init__(self, number, name, type, init_value, currency, color):
        self.number = number
        self.name = name
        self.type = type
        self.init_value = init_value
        self.currency = currency
        self.color = color
        self.expenses = 0
        self.income = 0

    def to_string(self):
        return (f"****** Account Name: {self.name} ******\n"
                f"     * Account Number: {self.number} * Type: {self.type}\n"
                f"     * Balance: {str(self.get_balance())} {self.currency}")

    def list_attributes(self):
        return (f"* Account Number: {self.number}\n"
                f"* Account Name: {self.name}\n"
                f"* Type: {self.type}\n"
                f"* Initial Value: {self.init_value}\n"
                f"* Currency: {self.currency}\n"
                f"* Color: {self.color}")

    def get_balance(self):
        return int(self.init_value) + int(self.income) - int(self.expenses)
