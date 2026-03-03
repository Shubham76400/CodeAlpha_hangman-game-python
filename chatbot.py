import datetime

# Store conversation count
message_count = 0

# Predefined responses dictionary
responses = {
    "greeting": ["hello", "hi", "hey"],
    "how_are_you": ["how are you", "how are you doing"],
    "bye": ["bye", "goodbye", "see you"]
}


def get_time_based_greeting():
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        return "Good Morning!"
    elif current_hour < 18:
        return "Good Afternoon!"
    else:
        return "Good Evening!"


def get_response(user_input):
    user_input = user_input.lower()

    # Greeting
    for word in responses["greeting"]:
        if word in user_input:
            return f"{get_time_based_greeting()} Hi there!"

    # How are you
    for word in responses["how_are_you"]:
        if word in user_input:
            return "I am fine, thanks for asking!"

    # Exit
    for word in responses["bye"]:
        if word in user_input:
            return "Goodbye! Have a great day!"

    return "Sorry, I don't understand that. Can you rephrase?"


def save_chat(user, bot):
    with open("chat_log.txt", "a") as file:
        file.write(f"You: {user}\n")
        file.write(f"Bot: {bot}\n")


def chatbot():
    global message_count

    print("🤖 Chatbot Started (Type 'bye' to exit)")
    print("--------------------------------------")

    while True:
        user_input = input("You: ")
        message_count += 1

        response = get_response(user_input)
        print("Bot:", response)

        save_chat(user_input, response)

        if "bye" in user_input.lower():
            print(f"\nTotal messages exchanged: {message_count}")
            break


# Run chatbot
chatbot()