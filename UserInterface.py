#Local Imports
import Expenses
import OpenIntegrations as OI

#Other Imports
import PySimpleGUI as sg
import json

#Import user data
try:
    with open("User_Data.json", "r") as file:
        user_data = json.load(file)
    userExpenseDataFile = open("userExpenseData.txt", "r")
    expenseList = []
    for line in userExpenseDataFile:
        temp = line.split(",")
        expenseList.append(Expenses.Expense(str(temp[0]), str(temp[1]), float(temp[2]), str(temp[3])))
    expensesListed = ""
    for expense in expenseList:
        expensesListed = expensesListed + expense.To_String()
except FileNotFoundError:
    print("No User Data Files Found")

#AI integration and set up
initialContext = OI.Setup_Persistent_Context(user_data["firstName"], user_data["lastName"], user_data["location"], user_data["isEmployed"], user_data["hourlyWage"], user_data["weeklyHours"], expensesListed)
chatFunction = OI.Create_Chat_Function(initialContext, "Fin")
currentContext = OI.OpenAiConnection.create_new_context()
currentContext["history"] = ""

#Building the GUI
cprint = sg.cprint
sg.theme("DarkBlue14")
default_font = 'Roboto Mono'
openningGreeting = "Say hi to Fin, Your personal financial advisor"
layout = [
         [sg.Push(),sg.Text((f"{openningGreeting}"),font=("Roboto Mono", 16)),sg.Push()],
         [sg.Push(),sg.Multiline(size=(138,17), key= '-MULTI-', disabled=True, font=("Roboto Mono", 16)),sg.Push()],
         [sg.Push(),sg.Input(size=(130,400), key = '-IN-', do_not_clear=False, font=("Roboto Mono", 16)),sg.Push()],
         [sg.Push(),sg.Button('Enter', size=(27,10)), sg.Button('Exit', size=(27,10)),sg.Push()]
]
window = sg.Window("FINance GBT", layout, size= (500,700), resizable=True)
sg.cprint_set_output_destination(window, '-MULTI-')
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Enter":
       sg.cprint("User: " + str(values['-IN-']))
       currentContext["clientInput"] = values['-IN-']
       finResponse = chatFunction.invoke(context=currentContext)
       sg.cprint("Fin: " + str(finResponse))
       currentContext["history"] += f"\nClient: {currentContext['clientInput']}\nFin: {finResponse}\n"


window.close()