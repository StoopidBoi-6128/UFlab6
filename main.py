#code by Ethan Calby

print("Menu")
print("-------------")
print("1. Encode")
print("2. Decode")
print("3. Quit")

choice = int(input('Please enter an option:'))
if choice == 1:
    encode()
if choice == 2:
    decode()
if choice == 3:
    break



def encode():
    password = int(input('Please enter your password to encode:')
    for char in range(len(password)):
        password[char] += 3
    print("Your password has been encoded and stored!")
    return password


def decode():
    password = [1, 2, 3, 4, 5]
    for char in range(len(password)):
        password[char] -= 3
    print(password)
