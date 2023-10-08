#Local Imports
import OpenIntegrations as OI
import PySimpleGUI as sg
import keyboard

#AI integration
initialContext = OI.Setup_Persistent_Context("John", "Foster", "Orlando", True, 35.0, 40, None)
chatFunction = OI.Create_Chat_Function(initialContext, "Fin")
currentContext = OI.OpenAiConnection.create_new_context()
currentContext["history"] = ""

cprint = sg.cprint
sg.theme("DarkBlue14")
default_font = 'Roboto Mono'
openningGreeting = "Hello"
layout = [
         [sg.Text(f"{openningGreeting}")],
         [sg.Push(),sg.Multiline(size=(130,27), key= '-MULTI-', disabled=True),sg.Push()],
         [sg.Push(),sg.Input(size=(130,400), key = '-IN-', do_not_clear=False),sg.Push()],
         [sg.Button('Enter', size=(30,10)),sg.Push(), sg.Button('Exit', size=(30,10))]
]
window = sg.Window("FINance GBT", layout, size= (500,500), resizable=True)
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