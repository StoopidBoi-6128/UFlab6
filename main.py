def encode():
    password = [1, 2, 3, 4, 5]
    for char in range(len(password)):
        password[char] += 3
    print(password)
    return password


def decode():
    password = [1, 2, 3, 4, 5]
    for char in range(len(password)):
        password[char] -= 3
    print(password)


if __name__ == '__main__':
    encode()
    decode()
