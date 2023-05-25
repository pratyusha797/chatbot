import random

def greet():
    responses = ["Hello!", "Hi!", "Hey there!", "Greetings!"]
    return random.choice(responses)

def get_response(user_input):
    user_input = user_input.lower()
    
    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        return greet()
    elif "how are you" in user_input:
        return "I'm good, thank you! How about you?"
    elif "your name" in user_input:
        return "I am ChatBot. Nice to meet you!"
    elif "bye" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

print("ChatBot: " + greet())

while True:
    user_input = input("User: ")
    response = get_response(user_input)
    print("ChatBot: " + response)

    if "bye" in user_input:
        break
