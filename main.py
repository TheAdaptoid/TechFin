#Local Imports
import Calculations

def main():
    print ("Hello World")

    #Initializing User Information
    hourlyRate = float(input("What is your hourly pay rate: "))
    weeklyHours = int(input("How many hours do you work per week: "))

    grossWeeklyIncome = Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours)
    taxedAnualIncome =Calculations.Calc_Anual_Income_After_Tax(grossWeeklyIncome)
    taxedWeeklyIncome = Calculations.Calc_Weekly_Income_After_Tax(taxedAnualIncome)
    #send to gpt
    print(f"You make ${grossWeeklyIncome} per week.")
    print(f"You make ${round(taxedWeeklyIncome,2)} per week after tax.")
    print(f"${taxedAnualIncome}")
main()