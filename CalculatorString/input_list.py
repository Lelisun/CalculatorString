import re

def UserInputSplit(userInput):
    return re.split(r'\s*([-+\*\/\^\(\)\=])\s*', userInput) 