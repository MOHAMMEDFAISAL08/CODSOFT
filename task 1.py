def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but thanks for asking! How can I assist you?"
    elif "joke" in user_input:
        return "Why don't programmers like nature? It has too many bugs!"
    elif "weather" in user_input:
        return "I'm not connected to live weather data, but it looks like a good day to code!"
    elif "your favorite programming language" in user_input:
        return "I love Python! It's simple, versatile, and perfect for beginners."
    elif "motivate me" in user_input or "motivation" in user_input:
        return "Here's a motivational quote: 'The only way to do great work is to love what you do.' - Steve Jobs"
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    elif "learning resources" in user_input:
        return "Check out free platforms like Codecademy, FreeCodeCamp, and W3Schools to start learning programming!"
    elif "fun fact" in user_input:
        return "Did you know? The first computer programmer was Ada Lovelace, who worked on Charles Babbage's early mechanical computer!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you ask something else?"

# Main loop
print("Chatbot: Hello! I am your chatbot. Ask me anything or type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
