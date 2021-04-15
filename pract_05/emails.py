"""
CP1404 Practical
emails.py
A program that stores users' emails (unique keys) and names (values) in a dictionary
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        name_check = input("Is your name {}? (Y/n) ".format(name))
        if name_check.upper() != "Y" and name_check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    remove_symbol = email.split("@")[0]
    part = remove_symbol.split(".")
    part.sort()
    name = "".join(part).title()
    return name


main()
