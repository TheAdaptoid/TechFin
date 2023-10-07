#Imports
import semantic_kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

#Setting up AI connection
OpenAiConnection = semantic_kernel.Kernel()
apiKey = "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"
orgID = "org-QVpFdkKtFlEdqL6AMrDXFUfW"
OpenAiConnection.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", apiKey, orgID))

def Location_Suggestions_For_Food(location:str, foodType:str, budget:float):
    promptInput = f"Suggest 3 resturants that serve {foodType} style food in the {location} area on a budget of ${budget}."
    result = OpenAiConnection.create_semantic_function(promptInput)
    return result()