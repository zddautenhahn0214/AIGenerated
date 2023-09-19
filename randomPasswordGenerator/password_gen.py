import random
import string

def generate_password(length):
  # generate a random string of characters, numbers, and special characters
  password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
  return password

# prompt the user for the desired password length
password_length = input("Enter the desired password length: ")

# convert the password length to an integer
password_length = int(password_length)

# generate and print the password
password = generate_password(password_length)
print(f"Your generated password is: {password}")
