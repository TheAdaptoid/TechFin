#Imports
import semantic_kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

#Setting up AI connection
OpenAiConnection = semantic_kernel.Kernel()
apiKey = "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"
orgID = "org-QVpFdkKtFlEdqL6AMrDXFUfW"
OpenAiConnection.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", apiKey, orgID))
contextClue = "You are friendly, digital personal financial advisor. Try to keep your resposes short but informative."


#Definitions
def Location_Suggestions_For_Food(location:str, foodType:str, budget:float):
    inputPrompt = f"Suggest 3 resturants that serve {foodType} style food in the {location} area on a budget of ${budget}."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

def Expense_Reduction_Suggestion(expenseCategory:str):
    inputPrompt = f"Suggest ways a person can spendless money on {expenseCategory}."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

def Trip_Plan_Suggestion(location:str, budget:float):
    inputPrompt = f"Suggest how a person could plan for a trip to {location} on a budget of ${budget}."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

def Announce_Under_Budget(weeklyIncome:float, weeklyExpense:float, userName:str):
    inputPrompt = f"{contextClue} Congratulate {userName} for being under budget and saving ${round(weeklyIncome - weeklyExpense, 2)} this past week. Also suggest what {userName} could do to with money they saved."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

def Announce_Over_Budget(weeklyIncome:float, weeklyExpense:float, expenseCategory:str, expenseProportion:float, userName:str):
    inputPrompt = f"{contextClue} Inform {userName} that they have over budgeted by ${round(weeklyIncome - weeklyExpense, 2)} for the week. Also inform {userName} that their largest expense category is {expenseCategory} and that it makes up {round(expenseProportion*100,2)} of their total weekly expenses. Also suggest three ways they can reduce their expenditure in that category."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

#persistent context
def Create_Chat_Function(setupPrompt:str, chatName:str):
    chatFunction = OpenAiConnection.create_semantic_function(setupPrompt, chatName, max_tokens=2000, temperature=0.7, top_p=0.5)
    return chatFunction

def Setup_Persistent_Context(firstName:str, lastName:str, location:str, isEmployed:bool,
                            hourlyRate:float, weeklyHours:int, expensesListed:list):
    setupPrompt = f"""
You are a friendly, digital personal financial advisor named Fin. Your goal is to help your client optimize their finances.
Try to keep your resposes short but informative. And after every response, ask the client if they have any more questions.
Your client is {firstName}.

Here is some background information about your client:
First Name: {firstName}
Last Name: {lastName}
City of Residence: {location}
Employed: {isEmployed}
Hourly Pay Rate: ${hourlyRate}
Hours worked per week: {weeklyHours}

Here is a list of their expenses with each expense in the format of the name of expense, expense Category, expense Amount, payment Frequency):
{expensesListed}"""

    setupPrompt += """
{{$history}}
Client: {{$clientInput}}
Fin: """

    return setupPrompt

"""
print("Conducting Analysis...")
    initialContext = OI.Setup_Persistent_Context(firstName, lastName, location, isEmployed, hourlyRate, weeklyHours, expensesListed)
    chatFunction = OI.Create_Chat_Function(initialContext, "Fin")

    currentContext = OI.OpenAiConnection.create_new_context()
    currentContext["history"] = ""

    while 0:
        currentContext["clientInput"] = str(input(""))
        finResponse = chatFunction.invoke(context=currentContext)
        print(finResponse)
        currentContext["history"] += f"\nClient: {currentContext['clientInput']}\nFin: {finResponse}\n"
"""