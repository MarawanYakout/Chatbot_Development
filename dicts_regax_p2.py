#Second Part
#Created by Marawan Yakout
#Check out the README file for information

import re # importing regex language to our python file

def zip_responses(precepts, responses):
    """
    Takes two lists and returns a dictionary mapping categories to responses.
    """
    # zip(precepts, responses) creates an iterator of tuples: ('greeting', 'Hello!...')
    # dict() converts those tuples into a dictionary

    mapping = dict(zip(precepts, responses))
    return mapping


def mappings():
    # We use broad categories now, not specific words like "tea"
    precepts = ["greetings", "farewell", "gratitude", "no_match", "name_query", "color_query"]

    responses = [
        "Hello! How can I help you today?",
        "Goodbye! Have a great day.",
        "You are very welcome!",
        "I am sorry, I don't understand that.",
        "Hello {name}, nice to meet you!",  # Note the placeholder {name}
        "Oh, I love {color} too! It's a great color." # Note the placeholder {color}
    ]
    return zip_responses(precepts, responses)



def re_patterns():
    # Returns a list of compiled regex patterns
    # [pattern, category_key]
    
    patterns = [
        
         # ADVANCED: Entity Extraction
        # Captures a name starting with Capital letter after "name is"i
        # Has to be at the top so it can be detected with hello 
        (r"name is ([A-Z][a-z]+)", "name_query"),
        
        # Captures a color word after "like" or "love"
        (r"(?:like|love) (red|blue|green|yellow|black|white)", "color_query"),

        # Checks for hello, hi, hey (case insensitive is handled in search)
        (r"hello|hi|hey", "greetings"), 
        
        # Checks for bye, goodbye, see ya
        (r"bye|goodbye|see you", "farewell"),
        
        # Checks for thanks, thank you
        (r"thank", "gratitude")
    ]
    return patterns

# Global state to remember user details we are collecting the name and color here so we can use it later on
user_state = {"name": "User", "color": "unknown"}


def detect_pattern(user_input):
    patterns = re_patterns()
    
    for pattern, category in patterns:
        # re.search looks for the pattern ANYWHERE in the string
        match = re.search(pattern, user_input, re.IGNORECASE)
        
        if match:
            # ADVANCED: If we found a name or color, save it!
            if category == "name_query":
                # .group(1) gets the text inside the parenthesis () of the regex
                found_name = match.group(1)
                user_state["name"] = found_name
                return category
                
            elif category == "color_query":
                found_color = match.group(1)
                user_state["color"] = found_color
                return category
            
            # Standard match (hello, bye, etc.)
            return category
            
    # If the loop finishes with no match
    return "no_match"

def chatbot_response(user_input):
    category = detect_pattern(user_input)
    knowledge_base = mappings()
    response_template = knowledge_base.get(category)
    # .format uses the user_state to replace {name} or {color}
    return response_template.format(**user_state)


# --- Main Loop ---
def chat():
    print("Chatbot: Hello! I'm ready to learn about you. (Type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit": 
            break
            
        bot_response = chatbot_response(user_input)
        print(f"Chatbot: {bot_response}")
        
        if "Goodbye" in bot_response:
            break

# Run the bot
chat()
