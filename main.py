#Local Imports
import Calculations

def main():
    print ("Hello World")

    #Initializing User Information
    hourlyRate = float(input("What is your hourly pay rate: "))
    weeklyHours = int(input("How many hours do you work per week: "))

    grossWeeklyIncome = Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours)
    taxedWeeklyIncome = Calculations.Calc_Weekly_Income_After_Tax(Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours))
    
    #send to gpt
    print(f"You make ${grossWeeklyIncome} per week.")
    print(f"You make ${taxedWeeklyIncome} per week after tax.")
    print(f"${Calculations.Calc_Weekly_Income_After_Tax(grossWeeklyIncome)}")
main()