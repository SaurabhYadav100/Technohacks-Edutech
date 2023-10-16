import random
import string

print("\n--------------------------------------------------------------")
print("                   RANDOM PASSWORD GENERATOR              ")
print("--------------------------------------------------------------")

def generate(length):
    # Define the characters 
    characters = string.ascii_letters + string.digits + "!$%^@&#"
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

a=int(input("\nEnter the length of password:"))
print("Your Password is:",generate(a))

