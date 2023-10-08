#Imports
import json
import semantic_kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

#Setting up AI connection
with open("Open_AI_Keys.json"):
    keys = json.load(open("Open_AI_Keys.json"))
    apiKey = keys["API_KEY"]
    orgID = keys["Group_ID"]

OpenAiConnection = semantic_kernel.Kernel()
OpenAiConnection.add_chat_service("chat-gpt", OpenAIChatCompletion("gpt-3.5-turbo", apiKey, orgID))

#Definitions
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