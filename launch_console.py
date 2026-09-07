print("Welcome to Krish's Launch Console!")

name = input("What is your name? ")
print("Hello, " + name + "!")

while True:
    print("1. About me")
    print("2. My goals")
    print("3. My favorite game")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("My name is Krish. I like basketball, coding, and robotics.")

    elif choice == "2":
        print("My goal is to become a software engineer.")

    elif choice == "3":
        print("My favorite game is Spyder Hangman.")

    elif choice == "4":
        print("Goodbye, " + name + "!")
        break

    else:
        print("Please choose 1, 2, 3, or 4.")