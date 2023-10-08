#Local Imports
import OpenIntegrations as OI
import PySimpleGUI as sg

#AI integration
initialContext = OI.Setup_Persistent_Context("John", "Foster", "Orlando", True, 35.0, 40, None)
chatFunction = OI.Create_Chat_Function(initialContext, "Fin")
currentContext = OI.OpenAiConnection.create_new_context()
currentContext["history"] = ""

cprint = sg.cprint
sg.theme("DarkBlue14")
default_font = 'Roboto Mono'
openningGreeting = "Say Hi to Fin, Your personal AI financial assistant"
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