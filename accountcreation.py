import uuid
import datetime
import os
import json

dataFile = "userInfo.json"

# Create a user object to store the user data
class User:
    def __init__(self, id, firstName, lastName, username, email, password, dateCreated, active):
        self.id = id
        self.email = email
        self.password = password
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.dateCreated = dateCreated
        self.active = True
    
    def handleInfo(self):
        """Create a dictionary to store user info and append it to a JSON file"""
        userInfo = {
            "id": self.id,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "dateCreated": self.dateCreated,
            "active": self.active
        }
        
        # Ensure the file exists before reading from it
        if not os.path.exists(dataFile):
            with open(dataFile, "w") as f:
                json.dump([], f, indent=4)
        
        # Read the existing data from the JSON file
        with open(dataFile, "r") as f:
            data = json.load(f)
        
        # Append the new data to the existing data
        data.append(userInfo)
        
        # Write the updated data back to the JSON file with indentation
        with open(dataFile, "w") as f:
            json.dump(data, f, indent=4)

    #Disable/enable account
    def toggle_active(self):
        match self.active:
            case True:
                self.active = False
            case False:
                self.active = True
        

# Create a password
def create_password():
    """Create a password with confirmation"""
    password = input("Password: ")
    confirmPassword = input("Confirm Password: ")
    if password == confirmPassword:
        return password
    else:
        print("Passwords do not match. Please try again.")
        return create_password()

def uploadUsernames():
    """Make a list of all the usernames to check if the input username is taken"""
    usernames = []
    # Ensure the file exists before reading from it
    if not os.path.exists(dataFile):
        with open(dataFile, "w") as f:
            json.dump([], f, indent=4)
    
    # Make a list of all of the usernames
    with open(dataFile, "r") as f:
        data = json.load(f)
        for user in data:
            usernames.append(user["username"])
    
    return usernames

def createUsername(usernames):
    """Create a username and check if it's taken already"""
    username = input("Username: ")

    # If it exists, try again
    if username in usernames:
        print("Username is taken. Please try again.")
        return createUsername(usernames)
    else:
        return username

# Ask for user info
def get_user_info():
    # Creates a unique ID for each user
    id = str(uuid.uuid4())
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    userName = createUsername(uploadUsernames())
    email = input("Email: ")
    password = create_password()
    # Stores the date that the account is created with formatting for month/day/year
    dateCreated = datetime.datetime.now().strftime("%m/%d/%Y")
    user = User(id, firstName, lastName, userName, email, password, dateCreated)
    user.handleInfo()

def createAccount():
    # Welcome the user to the account creation page
    print("Please input the following information to create an account.")
    get_user_info()