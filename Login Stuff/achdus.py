import accountcreation as ac
import login
import post 
import compare

appName = "Achdus"

print(f"Welcome to {appName}!")

while True:
    _input = input(f"'L' to log in,c 'C' to create an account, 'X' to exit\n").lower()

    match _input:
        case 'l':
            #Log in
            login.login()
            post.main()
            compare.main()
        case 'c':
            #Create an account
            ac.createAccount()
            print(f"Welcome to {appName}!")
            post.main()
            compare.main()
        case 'x':
            print("Good Bye!")
            break
        case _:
            print("Invalid Entry. Try again")