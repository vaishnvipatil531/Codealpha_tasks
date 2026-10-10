def chatbot():

    print("===== BASIC CHATBOT =====")
    print("Type 'hello', 'how are you', 'what is your name' or 'bye'.")

    while True:

        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is CodeAlpha Bot.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
