# Simple Rule-Based Chatbot

print("🤖 ChatBot: Hi there! I'm your friendly chatbot.")
print("Type 'bye' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("🤖 ChatBot: Hello! How can I help you today?")
    
    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm just a bunch of code, but I'm doing great! How about you?")
    
    elif "your name" in user_input:
        print("🤖 ChatBot: I'm ChatBot 1.0 — your virtual assistant.")
    
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"🤖 ChatBot: The current time is {current_time}.")
    
    elif "date" in user_input:
        from datetime import date
        today = date.today()
        print(f"🤖 ChatBot: Today's date is {today}.")
    
    elif "weather" in user_input:
        print("🤖 ChatBot: I can’t fetch live data yet, but I hope the weather’s nice where you are!")
    
    elif "bye" in user_input or "exit" in user_input:
        print("🤖 ChatBot: Goodbye! Have a great day! 👋")
        break
    
    else:
        print("🤖 ChatBot: Sorry, I didn’t understand that. Try asking something else!")
