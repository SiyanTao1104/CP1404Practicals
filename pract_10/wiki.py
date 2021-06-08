import wikipedia
def main():
    while True:
        search = input("Enter a number to search info:")
        if search =='':
            print("Thanks to use")
            break
        else:
            print(wikipedia.search(search))

main()