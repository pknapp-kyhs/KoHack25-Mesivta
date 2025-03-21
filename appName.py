import accountcreation as ac
import login
appName = "App Name"

print(f"Welcome to {appName}!")

while True:
    _input = input(f"'L' to log in, 'C' to create an account, 'X' to exit\n").lower()

    match _input:
        case 'l':
            #Log in
            login.login()
        case 'c':
            #Create an account
            ac.createAccount()
            print(f"Welcome to {appName}!")
        case 'x':
            print("Good Bye!")
            break
        case _:
            print("Invalid Entry. Try again")