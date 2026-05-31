import secrets 
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

combined = letters + numbers + symbols 

length = int(input("Enter the password length you require:"))
password = ""

for i in range(length):
    password += secrets.choice(combined)

print("\nPassword Generated:")
print(password)



