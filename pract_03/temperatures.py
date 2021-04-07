"""
CP1404 - Practical
Temperature conversions
"""
def main():
    menu ="""C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("What is your Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Wh at is your Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Result: {} C".format(celsius))
        else:
            print("Invalid option")
            print(menu)
        choice = input(">>> ").upper()
        print("Thank you for using.")


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return 5.0 * (fahrenheit - 32) / 9


main()