email = input("Enter your Email: ")

# This code takes an email input from the user and splits it into the username and domain.
# It uses string slicing and the index method to find the position of the '@' character.
# The username is everything before the '@' and the domain is everything after it.
# The result is printed in a formatted string.
print(f"Your user name is: {email[:email.index('@')]} and your domain is: {email[email.index('@')+1:]}")