#Local Imports
import Calculations

def main():
    print ("Hello World")

    #Initializing User Information
    hourlyRate = float(input("What is your hourly pay rate: "))
    weeklyHours = int(input("How many hours do you work per week: "))

    #send to gpt
    print(f"You make ${Calculations.Calc_Weekly_Income(hourlyRate, weeklyHours)} per week.")

main()