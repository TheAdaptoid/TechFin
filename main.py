#Imports
from os import system

#Local Imports
import Calculations
import OpenIntegrations as OI
import Expenses

def main():
    system("cls")
    print("|| FinanceGPT ||")

    try:
        #Load User Data from Files
        userDataFile = open("userData.txt", "r")
        userExpenseDataFile = open("userExpenseData.txt", "r")

        firstName = userDataFile.readline()
        lastName = userDataFile.readline()
        location = userDataFile.readline()
        isEmployed = bool(userDataFile.readline())
        hourlyRate = float(userDataFile.readline())
        weeklyHours = int(userDataFile.readline())

        expenseList = []
        for line in userExpenseDataFile:
            temp = line.split(",")
            expenseList.append(Expenses.Expense(str(temp[0]), str(temp[1]), float(temp[2]), str(temp[3])))

    except FileNotFoundError:
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

        #Send User Information to Persistent File
        userDataFile = open("userData.txt", "w")
        userDataFile.write(f"{firstName}\n")
        userDataFile.write(f"{lastName}\n")
        userDataFile.write(f"{location}\n")
        userDataFile.write(f"{isEmployed}\n")
        userDataFile.write(f"{hourlyRate}\n")
        userDataFile.write(f"{weeklyHours}\n")
        userDataFile.close()

        userExpenseDataFile = open("userExpenseData.txt", "w")
        for expense in expenseList:
            userExpenseDataFile.write(f"{expense.Get_Name()},{expense.Get_Category()},{expense.Get_Amount()},{expense.Get_Frequency()}\n")
        userExpenseDataFile.close()

    #User Information Calculations
    grossWeeklyIncome = Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours)
    taxedAnnualIncome = Calculations.Calc_Anual_Income_After_Tax(grossWeeklyIncome)
    taxedWeeklyIncome = Calculations.Calc_Weekly_Income_After_Tax(taxedAnnualIncome)
    totalWeeklyExpense = Calculations.Calc_Total_Weekly_Expense(expenseList)
    largestExpense = Calculations.Calc_Largest_Expense(expenseList)
    expensesListed = ""
    for expense in expenseList:
        expensesListed = expensesListed + expense.To_String()

    #Initial Analysis ||KEEP||
    print("Conducting Analysis...")
    initialContext = OI.Setup_Persistent_Context(firstName, lastName, location, isEmployed, hourlyRate, weeklyHours, expensesListed)
    chatFunction = OI.Create_Chat_Function(initialContext, "Fin")

    currentContext = OI.OpenAiConnection.create_new_context()
    currentContext["history"] = ""

    while 0:
        currentContext["clientInput"] = str(input(""))
        finResponse = chatFunction.invoke(context=currentContext)
        print(finResponse)
        currentContext["history"] += f"\nClient: {currentContext['clientInput']}\nFin: {finResponse}\n"
        
main()