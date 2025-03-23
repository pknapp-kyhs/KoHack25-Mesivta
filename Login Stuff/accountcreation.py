import uuid
import datetime
import os
import json

dataFile = "userInfo.json"

# Create a user object to store the user data
class User:
    def __init__(self, id, firstName, lastName, username, email, password, dateCreated, city1, city2, city3, practice, Kohen, active):
        self.id = id
        self.email = email
        self.password = password
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.dateCreated = dateCreated
        self.city1 = city1
        self.city2 = city2
        self.city3 = city3
        self.practice = practice
        self.Kohen = False
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
            "city1": self.city1,
            "city2": self.city2,
            "city3": self.city3,
            "practice": self.practice,
            "Kohen": self.Kohen,
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
    username = input("Username: ").strip()

    # If it exists, try again
    if username in usernames:
        print("Username is taken. Please try again.")
        return createUsername(usernames)
    else:
        return username


def checkOrigin():
    city1 = input("Please input one city/town you would like to follow: ")
    city2 = input("Please input another city/town you would like to follow: ")
    city3 = input("Please input one final city/town you would like to follow: ") 
    return city1, city2, city3
def checkPractice():
    practice = input("Please input your practice (ex: ashekenaz, sephardi, chabad, etc.): ")
    return practice
def checkKohen():
    Kohen = input("Are you a Kohen? (yes or no): ")
    if Kohen == "yes" or Kohen == "Yes":
        Kohen = True
    else:
        Kohen = False
    return Kohen
# Ask for user info
def get_user_info():
    # Creates a unique ID for each user
    id = str(uuid.uuid4())
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    userName = createUsername(uploadUsernames())
    email = input("Email: ")
    password = create_password()
    city1, city2, city3 = checkOrigin()

    practice = checkPractice()
    Kohen = checkKohen()

    # Stores the date that the account is created with formatting for month/day/year
    dateCreated = datetime.datetime.now().strftime("%m/%d/%Y")
    user = User(id, firstName, lastName, userName, email, password, dateCreated, city1, city2, city3, practice, Kohen, True)
    user.handleInfo()
    return userName

def createAccount():
    # Welcome the user to the account creation page
    print("Please input the following information to create an account.")
    get_user_info()
    print("Account created successfully.")
createAccount()