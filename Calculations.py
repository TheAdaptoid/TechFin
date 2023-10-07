#Calculations

def Calc_Weekly_Income(hourlyRate:float, workingHours:int):
    weeklyIncome = hourlyRate * workingHours
    return weeklyIncome

def Calc_Anual_Income_After_Tax(weeklyIncome:float):
    grossAnualIncome = weeklyIncome * 52
    taxedAnualIncome = 0
    if(grossAnualIncome >= 578126):
        amountTaxed = grossAnualIncome - 578126
        taxedAnualIncome = (amountTaxed * .37)
        grossAnualIncome - amountTaxed
    if(grossAnualIncome >= 231251):
        amountTaxed = grossAnualIncome - 231251
        taxedAnualIncome = taxedAnualIncome + (amountTaxed * .35)
        grossAnualIncome - amountTaxed
    if(grossAnualIncome >= 182101):
        amountTaxed = grossAnualIncome - 182101
        taxedAnualIncome = taxedAnualIncome + (amountTaxed * .32)
        grossAnualIncome - amountTaxed
    if(grossAnualIncome >= 95376):
        amountTaxed = grossAnualIncome - 95376
        taxedAnualIncome = taxedAnualIncome + (amountTaxed * .24)
        grossAnualIncome - amountTaxed
    if(grossAnualIncome >= 44726):
        amountTaxed = grossAnualIncome - 44726
        taxedAnualIncome = taxedAnualIncome + (amountTaxed * .22)
        grossAnualIncome - amountTaxed 
    if(grossAnualIncome >= 11001):
        amountTaxed = grossAnualIncome - 11001
        taxedAnualIncome = taxedAnualIncome + (amountTaxed * .12)
        grossAnualIncome - amountTaxed
    if(grossAnualIncome >= 0):
        amountTaxed = grossAnualIncome
        taxedAnualIncome = taxedAnualIncome + (amountTaxed * .1)
        taxedAnualIncome = grossAnualIncome - taxedAnualIncome
    return taxedAnualIncome

def Calc_Weekly_Income_After_Tax(anualIncome:float):
    weeklyTaxedIncome = Calc_Anual_Income_After_Tax(anualIncome)
    weeklyTaxedIncome /= 52
    return weeklyTaxedIncome

print(f"{Calc_Anual_Income_After_Tax(100.0)}")