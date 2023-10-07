#Local Imports
import Expenses

def Yes_No_Dictionary():
    yesNoDict = {
        "Yes" : 1,
        "No" : 0,
    }

    return yesNoDict

def Expense_Category_Dictionary():
    expenseCategoryDict = {
        "Bills & Utilities" : 0,
        "Transportation" : 0,
        "Groceries" : 0,
        "Dining Out" : 0,
        "Subscriptions" : 0,
    }

    return expenseCategoryDict

def Expense_Frequency_Dictionary():
    expenseFrequencyDict = {
        "Weekly" : 0,
        "Monthly" : 0,
        "Yearly" : 0,
    }

    return expenseFrequencyDict

def Input_Checking(optionDict:dict):
    option = str(input(""))
    while True:
        if option.title() in optionDict.keys():
            return option
        else:
            print(f"Please enter a valid keyword. Options: {list(optionDict.keys())}")
            option = str(input("Keyword: "))

def Calc_Weekly_Income(hourlyRate:float, workingHours:int):
    weeklyIncome = hourlyRate * workingHours
    return weeklyIncome

def Calc_Anual_Income_After_Tax(weeklyIncome:float):
    grossAnnualIncome = weeklyIncome * 52
    taxedAnnualIncome = 0
    if(grossAnnualIncome >= 578126):
        amountTaxed = grossAnnualIncome - 578126
        taxedAnnualIncome = (amountTaxed * .37)
        grossAnnualIncome - amountTaxed
    if(grossAnnualIncome >= 231251):
        amountTaxed = grossAnnualIncome - 231251
        taxedAnnualIncome = taxedAnnualIncome + (amountTaxed * .35)
        grossAnnualIncome - amountTaxed
    if(grossAnnualIncome >= 182101):
        amountTaxed = grossAnnualIncome - 182101
        taxedAnnualIncome = taxedAnnualIncome + (amountTaxed * .32)
        grossAnnualIncome - amountTaxed
    if(grossAnnualIncome >= 95376):
        amountTaxed = grossAnnualIncome - 95376
        taxedAnnualIncome = taxedAnnualIncome + (amountTaxed * .24)
        grossAnnualIncome - amountTaxed
    if(grossAnnualIncome >= 44726):
        amountTaxed = grossAnnualIncome - 44726
        taxedAnnualIncome = taxedAnnualIncome + (amountTaxed * .22)
        grossAnnualIncome - amountTaxed 
    if(grossAnnualIncome >= 11001):
        amountTaxed = grossAnnualIncome - 11001
        taxedAnnualIncome = taxedAnnualIncome + (amountTaxed * .12)
        grossAnnualIncome - amountTaxed
    if(grossAnnualIncome >= 0):
        amountTaxed = grossAnnualIncome
        taxedAnnualIncome = taxedAnnualIncome + (amountTaxed * .1)
        taxedAnnualIncome = grossAnnualIncome - taxedAnnualIncome
    return taxedAnnualIncome

def Calc_Weekly_Income_After_Tax(annualIncome:float):
    weeklyTaxedIncome = annualIncome
    weeklyTaxedIncome /= 52
    return weeklyTaxedIncome

def Calc_Expense_Breakdown(expenseList:list):
    localExpenseDict = Expense_Category_Dictionary()
    for expense in expenseList:
        localExpenseDict[expense.Get_Category()] =  localExpenseDict[expense.Get_Category()] + expense.Get_Amount()
    return localExpenseDict

def Calc_Expense_Proportion(expenseDict:dict, category:str):
    return expenseDict[category] / sum(expenseDict.values())

def Calc_Expense_Breakdowns(expenseList:list):
    for category in Expense_Category_Dictionary():
        print(f"{category}: {round((Calc_Expense_Proportion(Calc_Expense_Breakdown(expenseList)), category)) * 100, 2}%")

def Calc_Largest_Expense(expenseList:list):
    expenseDict = Calc_Expense_Breakdown(expenseList)
    return max(expenseDict, key=expenseDict.get)