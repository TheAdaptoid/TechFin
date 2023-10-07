<<<<<<< HEAD
def Expense(self, expenseName:str, enpenseCategory:str, expenseAmount:str, expenseFrequency:str):
    self.expenseName
    self.expenseCategory
    self.expenseAmount
    self.expenseFrequency
=======
class Expense:
    def __init__(self, expenseName:str, expenseCategory:str, expenseAmount:float, expenseFrequency:str):
        self.expenseName = expenseName
        self.expenseCategory = expenseCategory
        self.expenseAmount = expenseAmount
        self.expenseFrequency = expenseFrequency

    def Get_Name(self):
        return str(self.expenseName)

    def Get_Category(self):
        return str(self.expenseCategory)

    def Get_Amount(self):
        return float(self.expenseAmount)

    def Get_Frequency(self):
        return str(self.expenseFrequency)
>>>>>>> abbba8009b27a617f2287f0049672f36a255b0dd
