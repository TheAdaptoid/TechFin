import PySimpleGUI as sg
sg.set_options(font=('Roboto Mono', 16))
sg.theme("DarkBlue14")

def User_Name(firstName: str, lastName: str):
    user = firstName + " " + lastName[0] + "."
    print(f"{user}")
    return user
