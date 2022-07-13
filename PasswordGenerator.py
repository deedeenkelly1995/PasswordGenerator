import random
import string
print("Welcome to the password generator")

choice = input("Would you like to generate a password(y/n):")

if choice == "y":
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-0987654321,./;[]()'

    print("Password Generator")
    print("==================")

    number = input('Amount of passwords to generate: ')
    number = int(number)

    length = input('Your password length: ')
    length = int(length)

    print('\n\nHere are your passwords:')

    for pwd in range(number):
        passwords = ''
        for c in range(length):
            passwords += random.choice(chars)

        print(passwords)
else:
    print("Exit")