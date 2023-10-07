#Imports
import os

#Local Imports
import Calculations
import OpenIntegrations as OI

def main():
    os.system('cls')
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
        hourlyRate = float(input("Hourly pay rate: "))
        weeklyHours = int(input("Hours worked per week: "))

    #User Information Calculations
    grossWeeklyIncome = Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours)
    taxedAnualIncome =Calculations.Calc_Anual_Income_After_Tax(grossWeeklyIncome)
    taxedWeeklyIncome = Calculations.Calc_Weekly_Income_After_Tax(taxedAnualIncome)
    
    #send to gpt
    print(f"You make ${grossWeeklyIncome} per week.")
    print(f"You make ${round(taxedWeeklyIncome,2)} per week after tax.")
    print(f"${taxedAnualIncome}")

main()