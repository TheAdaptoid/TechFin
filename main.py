#Local Imports
import Calculations
import OpenIntegrations as OI
import Expenses
def main():
    print("|| FinanceGPT ||")

    #User Information Prompting
    firstName = str(input("First Name: "))
    lastName = str(input("Last Name: "))
    location = str(input("City of residence: "))

    isEmployed = False
    hourlyRate = 0
    weeklyHours = 0
    
    if str(input("Are you employed? [Y/N]: ")).lower() == "y":
        isEmployed = True
        hourlyRate = float(input("Hourly pay rate: $"))
        weeklyHours = int(input("Hours worked per week: "))

    
    if str(input("Are there any expenses you want to declare [Y/N]: ")).lower() == "y":
        expenseList = []
        while 1:
            tempExpenseName = str(input("Enter the expense name: "))
            tempExpenseCat = str(input("Enter the expense category [Bills & Utilities, Subscriptions, Transportation, Dining, Groceries]: "))
            tempEpenseAmount = float(input("Enter the amount of this expense: $"))
            tempExpenseFreq =  str(input("How frequent is this expense [Weekly, Monthly, Yearly]: "))
            tempExpenseObj = Expenses.Expense(expenseName= tempExpenseName, expenseCategory= tempExpenseCat, expenseAmount= tempEpenseAmount, expenseFrequency= tempExpenseFreq)
            expenseList.append(tempExpenseObj)
            if str(input("Are there anymore expenses you want to list? [Y/N]: ")).lower() == "n":
                break
   
    #User Information Calculations
    grossWeeklyIncome = Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours)
    taxedAnualIncome = Calculations.Calc_Anual_Income_After_Tax(grossWeeklyIncome)
    taxedWeeklyIncome = Calculations.Calc_Weekly_Income_After_Tax(taxedAnualIncome)
    
    #send to gpt
    print(f"You make ${grossWeeklyIncome} per week.")
    print(f"You make ${round(taxedWeeklyIncome,2)} per week after tax.")
    print(f"${taxedAnualIncome}")
main()