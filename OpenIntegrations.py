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
    inputPrompt = f"Congratulate {userName} for being under budget and saving ${round(weeklyIncome - weeklyExpense, 2)} this past week. Also suggest what {userName} could do to with money they saved."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

def Announce_Over_Budget(weeklyIncome:float, weeklyExpense:float, expenseCategory:str, expenseProportion:float, userName:str):
    inputPrompt = f"{contextClue} Inform {userName} that they have over budgeted by ${round(weeklyIncome - weeklyExpense, 2)} for the week. Also inform {userName} that their largest expense category is {expenseCategory} and that it makes up {round(expenseProportion*100,2)} of their total weekly expenses. Also suggest three ways they can reduce their expenditure in that category."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

def Direct_User_Input(pastContext:str, inputPrompt:str):
    result = OpenAiConnection.create_semantic_function(f"{contextClue} Past Context: {pastContext}. inputPrompt")
    return result()

def Ask_User_For_Prompt(pastContext:str, userName:str):
    inputPrompt = f"{contextClue} Past Context: {pastContext}. Ask {userName} if there is anything else you could help them with."
    result = OpenAiConnection.create_semantic_function(inputPrompt)
    return result()

#debuggin