import os
import json
import accountcreation as ac

dataFile = "userInfo.json"
userData = None
print(userData)

def load_data():        
    # Check if file exists and create one if it doesn't
    if not os.path.exists(dataFile):
        with open(dataFile, "w") as f:
            json.dump([], f, indent=4)

    # Load all the data from the file
    with open(dataFile, "r") as f:
        data = json.load(f)
        return data
    
# Check if the username is in the data
def get_user_data():
    global userData
    data = load_data()

    username = input("Enter username...\n").strip()
    
    for user in data:
        if username in user["username"]:
            # If it is, return all the data
            userData = user
            return userData, username

    return {}, "n/a"
        
    # Otherwise create an account 


def get_Password(user):
    user, username = get_user_data()
    if username in user.values():
        password = input("Enter account password...\n")
        if user['password'] == password:
            print(f"Welcome {user['username']}")
        else:
            print("Wrong password, try again.")
            get_Password(user)
    else:
        print("User not found.")
        ac.createAccount()
        print("\nLog in:")
        login()

def login():    
    get_Password(userData)