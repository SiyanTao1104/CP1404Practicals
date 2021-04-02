"""
CP1404/CP5632 - Practical
Student: Siyan Tao
Sequences
"""
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
menu = "\ni.Show the even numbers\nii.Show the odd numbers\niii.Show the squares\niv.Exit the program"
print(menu)
even_number = []
odd_number = []
choice= input("Enter a choice").upper()
while choice != "iv":
    if choice =="i":
        for i in range(x, y):
            if i % 2 ==0:
                even_number.append(i)
            else:
                odd_number.append(i)
        print(even_number)
        print(menu)
        choice= input("Enter a choice").upper()
    elif choice =="ii":
        for i in range(x, y ):
            if i % 2 == 0:
                even_number.append(i)
            else:
                odd_number.append(i)
        print(odd_number)
        print(menu)
        choice = input("Enter a choice").upper()
    elif choice =="iii":
        for i in range(x,y):
            print(i**2, end=', ')
        print(menu)
        choice = input("Enter a choice").upper()
    else:
        print("Invalid choice")
        choice = input("Enter a choice").upper()
print("Exit the program")

