import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
length = input("Enter desired length of password: ")
length = int(length)
pass_pool = characters + numbers
password = ""
for i in range(length):
    password = password + random.choice(pass_pool)
print(f"Your password is: {password}")
