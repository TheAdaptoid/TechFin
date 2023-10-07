#Calculations

def Calc_Weekly_Income(hourlyRate:float, workingHours:int):
    weeklyIncome = hourlyRate * workingHours
    return weeklyIncome

def Calc_Weekly_Income_After_Tax(weeklyIncome:float, federalTaxRate:float):
    weeklyIncomeAfterTax = weeklyIncome - (weeklyIncome * federalTaxRate)
    return weeklyIncomeAfterTax