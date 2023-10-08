#Local Imports
import OpenIntegrations as OI
import PySimpleGUI as sg
import keyboard

cprint = sg.cprint
sg.theme("DarkBlue14")
default_font = 'Roboto Mono'
openningGreeting = "Hello"
layout = [
         [sg.Text(f"{openningGreeting}")],
         [sg.Push(),sg.Multiline(size=(130,17), key= '-MULTI-', disabled=True, font=("Roboto Mono", 16)),sg.Push()],
         [sg.Push(),sg.Input(size=(130,400), key = '-IN-',font=('Roboto Mono', 16)),sg.Push()],
         [sg.Push(),sg.Button('Enter', size=(27,10)), sg.Button('Exit', size=(28,10)),sg.Push()]
]
window = sg.Window("FINance GBT", layout, size= (500,700), resizable=True)
sg.cprint_set_output_destination(window, '-MULTI-')
while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == "Enter":
       sg.cprint("User - " + values['-IN-'])


window.close()