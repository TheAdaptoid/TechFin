#Imports
from os import system

#Local Imports
import Calculations
import OpenIntegrations as OI
import Expenses

def main():
    system("cls")
    print("|| FinanceGPT ||")

    #User Information Prompting
    '''
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
    '''
        
    if str(input("Are there any expenses you want to declare [Y/N]: ")).lower() == "y":
        expenseList = []
        while 1:
            tempExpenseName = str(input("Enter the expense name: "))
            print(f"Enter the expense category. Options: {list(Calculations.Expense_Category_Dictionary().keys())}")
            tempExpenseCat = Calculations.Input_Checking(Calculations.Expense_Category_Dictionary())
            tempEpenseAmount = float(input("Enter the amount of this expense: $"))
            print(f"Enter the expense frequency. Options: {list(Calculations.Expense_Frequency_Dictionary().keys())}")
            tempExpenseFreq =  Calculations.Input_Checking(Calculations.Expense_Frequency_Dictionary())

            tempExpenseObj = Expenses.Expense(tempExpenseName, tempExpenseCat, tempEpenseAmount, tempExpenseFreq)
            expenseList.append(tempExpenseObj)

            #Check for more expenses
            if str(input("Are there anymore expenses you want to list? [Y/N]: ")).lower() == "n":
                break
   
    #User Information Calculations
    '''
    grossWeeklyIncome = Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours)
    taxedAnnualIncome = Calculations.Calc_Anual_Income_After_Tax(grossWeeklyIncome)
    taxedWeeklyIncome = Calculations.Calc_Weekly_Income_After_Tax(taxedAnnualIncome)
    '''
    
    #send to gpt
    largestExpense = Calculations.Calc_Largest_Expense(expenseList)
    print(largestExpense)

main()