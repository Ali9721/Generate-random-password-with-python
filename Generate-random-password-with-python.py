# At first, import "string" & "random"
import string
import random

# Define "length" as a variable and get "length" of password.
length = int(input("Please enter the password length: "))

# Define "characters" as a variable and use "ascii-letters " & "digits" & "punctuation"
characters = string.ascii_letters + string.digits + string.punctuation

# Define "password" as a variable and use "join" to combine different parts of password. 
password = ''.join(random.choices(characters, k=length))

# Output the result
print(f"Generated password: {password}")