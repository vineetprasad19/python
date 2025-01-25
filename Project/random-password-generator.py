import random
import string

# A function to shuffle all the characters of a string
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)

# Function to generate a random password
def generate_password():
    # Generate random uppercase letters
    uppercase_letter1 = chr(random.randint(65, 90))
    uppercase_letter2 = chr(random.randint(65, 90))

    # Generate random lowercase letters
    lowercase_letter1 = chr(random.randint(97, 122))
    lowercase_letter2 = chr(random.randint(97, 122))

    # Generate random digits
    digit1 = chr(random.randint(48, 57))
    digit2 = chr(random.randint(48, 57))

    # Generate random special characters
    special_char1 = random.choice(string.punctuation)
    special_char2 = random.choice(string.punctuation)

    # Combine all characters
    password = (
        uppercase_letter1
        + uppercase_letter2
        + lowercase_letter1
        + lowercase_letter2
        + digit1
        + digit2
        + special_char1
        + special_char2
    )

    # Shuffle the password to make it more random
    return shuffle(password)

# Main program starts here
user_input = input("Enter a word: ")

# Check the length of the user's input
if len(user_input) < 15:
    print("Generating a random strong password because your input is too short...")
    password = generate_password()
else:
    print("Your input is already strong enough!")
    password = user_input

# Output the password
print("Generated Password:", password)
