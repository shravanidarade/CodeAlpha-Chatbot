# ==========================================
# Task 4: Basic Rule-Based Chatbot
# Goal: Build a simple rule-based chatbot
# Key Concepts: if-elif, functions, loops, input/output
# ==========================================

def get_bot_response(user_input):
    """
    Takes the user's input, normalizes it to lowercase,
    and returns a predefined response based on if-elif-else rules.
    """
    # Clean and normalize input (remove extra whitespace and convert to lowercase)
    clean_input = user_input.strip().lower()

    # Rule 1: Greeting
    if clean_input in ["hello", "hi", "hey", "greetings"]:
        return "Hi there! Friendly virtual greetings to you! 👋"
    
    # Rule 2: Inquiring about state
    elif clean_input in ["how are you", "how are you doing", "how's it going"]:
        return "I'm just a simple script, but I'm functioning perfectly! Thanks for asking! 💻"
    
    # Rule 3: Leaving/Goodbye
    elif clean_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a fantastic day ahead! 🚀"
    
    # Rule 4: Asking for help / capabilities
    elif "help" in clean_input or "can you do" in clean_input:
        return "I can answer basic greetings! Try saying 'hello', 'how are you', or 'bye'."
    
    # Rule 5: User entered nothing
    elif clean_input == "":
        return "I'm listening! Please type something so we can chat."
    
    # Rule 6: Fallback for unmatched inputs
    else:
        return "Hmm, I don't quite understand that. Try saying 'hello' or ask for 'help'!"


def run_chat_session():
    """
    The main function that controls the chatbot flow,
    running a loop to process continuous inputs until the user exits.
    """
    print("==================================================")
    print("🤖 Welcome to PythonBot, your friendly assistant! 🤖")
    print("Directions: Type your message below and press Enter.")
    print("Type 'bye' or 'exit' whenever you want to close the chat.")
    print("==================================================")

    # Infinite loop to keep the conversation going
    while True:
        # Prompt user for input
        user_message = input("\nYou: ")

        # Fetch corresponding bot response
        response = get_bot_response(user_message)

        # Output response
        print(f"Bot: {response}")

        # Check termination condition using normalized input
        normalized_message = user_message.strip().lower()
        if normalized_message in ["bye", "goodbye", "exit", "quit"]:
            print("\n[Chat Session Closed]")
            break


# The entry point of our script
if __name__ == "__main__":
    run_chat_session()