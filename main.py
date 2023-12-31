# code by Ethan Calby and Karen Tong


def encoder():  # Coded by Karen Tong
    global encoded
    password = input("Please enter your password to encode: ")
    print("Your password has been encoded and stored!\n")
    encoded = ""
    for char in password:
        encoded += str(int(char) + 3)
        # print(password)
        # print(encoded)
    return encoded


def decoder(encoded):  # Coded by Ethan Calby
    decoded = ""
    for char in encoded:
        decoded += str(int(char) - 3)
    print(f"The encoded password is {encoded}, and the original password is {decoded}.")
    return decoded


def main():  # Coded by Karen Tong
    global password
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu = int(input("Please enter an option: "))
        if menu == 1:
            password = encoder()
        elif menu == 2:
            decoder(encoded)
        elif menu == 3:
            break


if __name__ == "__main__":
    main()
