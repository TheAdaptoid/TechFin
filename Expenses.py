class Expense:
    def __init__(self, expenseName:str, expenseCategory:str, expenseAmount:float, expenseFrequency:str):
        self.expenseName = expenseName
        self.expenseCategory = expenseCategory
        self.expenseAmount = expenseAmount
        self.expenseFrequency = expenseFrequency

    def Get_Name(self):
        return str(self.expenseName)

    def Get_Category(self):
        return str(self.expenseCategory).title()

    def Get_Amount(self):
        return float(self.expenseAmount)

    def Get_Frequency(self):
        return str(self.expenseFrequency).title()
    
    def To_String(self):
        return f"{self.expenseName},{self.expenseCategory},{self.expenseAmount},{self.expenseFrequency}"
