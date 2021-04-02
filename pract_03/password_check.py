def main():
    password = get_password()
    get_length = len(password)
    print("*" * get_length)



def get_password():
    password = input("Please enter your password: ")
    return password

main()