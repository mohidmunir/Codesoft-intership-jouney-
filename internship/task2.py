import random
import string

print("Welcome to the Password Generator")

length = int(input("Enter the desired length of the password: "))

if length <= 0:
    print("Please enter a valid length greater than 0.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated password:", password)
