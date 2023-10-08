#Local Imports
import Calculations
import OpenIntegrations as OI
import Expenses
import GUI
import PySimpleGUI as sg

sg.set_options(font=('Roboto Mono', 16))
sg.theme("DarkBlue14")

#User Information Prompting
instructions = sg.Text("Please answer all the questions and then press ok.")
q1 = [sg.Text("Enter Name: "), sg.Input("", key='-name-')]
q2 = [sg.Text("City of residence: "), sg.Input(key='-a21-')]
q3 = [sg.Text("Are you employed? [Y/N]: "), sg.Input(key='-a22-')]
q4 = [sg.Text("Hourly pay rate: $"), sg.Input(key='-a23-')]
q5 = [sg.Text("Hours worked per week: "), sg.Input(key='-a24-')]
q6 = [sg.Text("Are there any expenses you want to declare [Y/N]: "), sg.Input(key='-a25-')]
q7 = [sg.Text("Enter the expense name: "), sg.Input(key='-a26-')]
q8 = [sg.Text("Enter the expense category [Bills & Utilities, Subscriptions, Transportation, Dining, Groceries]: "), sg.Input(key='-a27-')]
q9 = [sg.Text("Enter the amount of this expense: $"), sg.Input(key='-a28-')]
q10 = [sg.Text("How frequent is this expense [Weekly, Monthly, Yearly]: "), sg.Input(key='-a29-')]
q11 = [sg.Text("Are there anymore expenses you want to list? [Y/N]: "), sg.Input(key='-a30-')]

col1 = [[q1],[q2],[q3],[q4],[q5],[q6],[q7],[q8],[q9],[q10],[q11]]

layout = [[instructions],
          [sg.Text("Enter Name:  "), sg.Input("", key='-name-')],
[sg.Text("City of residence: "), sg.Input(key='-a21-')],
[sg.Text("Are you employed? [Y/N]: "), sg.Input(key='-a22-')],
[sg.Text("Hourly pay rate: $"), sg.Input(key='-a23-')],
[sg.Text("Hours worked per week: "), sg.Input(key='-a24-')],
[sg.Text("Are there any expenses you want to declare [Y/N]: "), sg.Input(key='-a25-')],
[sg.Text("Enter the expense name: "), sg.Input(key='-a26-')],
[sg.Text("Enter the expense category [Bills & Utilities-")],
[sg.Text("-Subscriptions Transportation, Dining, Groceries]: "), sg.Input(key='-a27-')],
[sg.Text("Enter the amount of this expense: $"), sg.Input(key='-a28-')],
[sg.Text("How frequent is this expense [Weekly, Monthly, Yearly]: "), sg.Input(key='-a29-')],
[sg.Text("Are there anymore expenses you want to list? [Y/N]: "), sg.Input(key='-a30-')]
]

window = sg.Window('Fin virtual Assistant', layout,location=(0,0), size=(800,600))


while True:
   event, values = window.read()
   print (event, values)
   if event in (sg.WIN_CLOSED, 'Exit'):
      break
window.close()