#Local Imports
import Calculations
import OpenIntegrations as OI
import Expenses
import PySimpleGUI as sg

sg.theme("DarkBlue14")
default_font = 'Roboto Mono'
openningGreeting = "Hello"
layout = [
         [sg.Text(f"{openningGreeting}")],
         [sg.Output(size=(70,27), key= '-IN-')],
         [sg.Push(),sg.Button('Enter', size=(10,10)), sg.Button('Exit', size=(10,10)),sg.Push()]
]
window = sg.Window("FINance GBT", layout, size= (500,500), resizable=True)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Enter":
        print(*values)

window.close()