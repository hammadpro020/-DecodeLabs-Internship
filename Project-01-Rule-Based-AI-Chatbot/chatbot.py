# ----------------------------------------
# Project : Rule-Based AI Chatbot
# Author  : Hammad Ahmed
# Language: Python
# ----------------------------------------

print("=" * 40)
print("      RULE-BASED AI CHATBOT")
print("=" * 40)
print("Available Commands:")
print("1. hello")
print("2. hi")
print("3. how are you")
print("4. what is your name")
print("5. who created you")
print("6. help")
print("7. bye")
print("=" * 40)

while True:

    user = input("\nYou: ")
    user = user.lower().strip()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created by Hammad Ahmed.")

    elif user == "help":
        print("\nAvailable Commands:")
        print("hello")
        print("hi")
        print("how are you")
        print("what is your name")
        print("who created you")
        print("bye")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that command.")