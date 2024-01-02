class __Transaction(object):

    def __init__(self, sign, value, date, categories, tag, comment):
        self.sign = sign
        self.value = value
        self.date = date
        self.categories = categories
        self.tag = tag
        self.comment = comment

    def get_value(self):
        self.value = self.sign * self.value
        return self.value
