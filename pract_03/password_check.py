def main():
    password = get_password()
    get_length = len(password)
    print_length(get_length)


def print_length(get_length):
    print("*" * get_length)


def get_password():
    password = input("Please enter your password: ")
    return password


main()