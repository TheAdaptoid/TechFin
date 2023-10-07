#Imports
import semantic_kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

#Setting up AI connection
OpenAiConnection = semantic_kernel.Kernel()
apiKey = "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"
orgID = "org-QVpFdkKtFlEdqL6AMrDXFUfW"
OpenAiConnection.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", apiKey, orgID))

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

#debuggin
print(Trip_Plan_Suggestion("Cuba", '1000'))