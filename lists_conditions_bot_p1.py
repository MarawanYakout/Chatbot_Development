# Learning how to create chatbots - Part 1
# Created on 23rd Nov 2025
# Created by Marawan Yakout
# Use freely for education just give credit, spread love not hate.



# The Knowledge Base
# Index:      0        1       2       3         4         5
precepts = ["hello", "tea", "cafe", "no", "thank you", "goodbye"]

responses = [
    "Hello! How can I assist you today?",                # Index 0
    "Sure, where would you like to sit? A cafe maybe?",  # Index 1
    "There are 2 cafes: Main building and lecture hall.",# Index 2
    "Is there anything else I can help you with?",       # Index 3
    "You are welcome.",                                  # Index 4
    "Goodbye! Have a great day!"                         # Index 5
]



def simple_chatbot():
    # 2. Start the Infinite Loop
    chatting = True
    while chatting:
		        
        # 3. Get Input and Normalize
        # .lower() ensures "Tea" matches "tea"
        user_message = input("USER: ").lower() 

        # 4. The Logic (Conditions)
        
        # Check if the user wants to quit first
        if user_message == "goodbye":
            # String Concatenation Example:
            print("BOT: " + responses[5]) 
            chatting = False # This stops the loop
            
            
        # Check if the message is in our known list
        elif user_message in precepts:
            # Find the position (index) of the input
            index_of_word = precepts.index(user_message)
            
            # Retrieve the matching response
            bot_response = responses[index_of_word]
            
            # Output
            print(f"BOT: {bot_response}")
            
        # Fallback for unknown words
        else:
            # String Concatenation with variables
            error_msg = "Sorry, I don't understand '" + user_message + "'."
            print("BOT: " + error_msg)

# Run the bot
simple_chatbot()
