"""
CP1404/CP5632 - Practical
Student: Siyan Tao
Menus
"""
name = input("Enter the name:")
print("(H)ello\n(G)oodbye\n(Q)uit")
choice = input(">>>").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello",name)
    elif choice =='G':
        print("Goodbye",name)
    else:
        print("Invalid message")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input(">>>").upper()
print("Finished.")
