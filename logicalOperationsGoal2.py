# Get user input
user_input = input("Enter a sentence: ")

# Remove leading and trailing whitespace
user_input = user_input.strip()

# Check if it's a question
is_question = (
    user_input.endswith('?') or
    (user_input.lower().startswith('what ') or 
     user_input.lower().startswith('who ') or 
     user_input.lower().startswith('where '))
)

print("Is a question: " + str(is_question))
