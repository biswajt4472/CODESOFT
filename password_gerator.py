import random
import string

password_length = int(input("Enter the length of the Password : "))

def password_generator(length):
    letters = string.ascii_letters + string.digits + string.punctuation + string.digits
    password = ''.join(random.choice(letters) for char in range(length))
    return password

Generated_Password = password_generator(password_length)

print("Generated Password is  : " + Generated_Password)