import uuid
import datetime
import os
import json
import requests

dataFile = "userInfo.json"
api_url = "https://api.api-ninjas.com/v1/geocoding"
api_key = "PfT1mGwaFpS+Dv/8fk1I3A==NefKEwmCGJUHKPb7"

# Create a user object to store the user data
class User:
    def __init__(self, id, firstName, lastName, username, email, password, dateCreated, city1, city2, city3, practice, Kohen, relevance):
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
        self.Kohen = Kohen
        self.relevance = relevance
    
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
            "relevance": self.relevance
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

def get_first_name():
    firstName = input("First Name: ").strip()
    if firstName == "":
        print("First Name cannot be blank. Please try again.")
        return get_first_name()
    return firstName

def get_last_name():
    lastName = input("Last Name: ").strip()
    if lastName == "":
        print("Last Name cannot be blank. Please try again.")
        return get_last_name()
    return lastName

def get_email(): 
    email = input("Email: ").strip()
    if email == "":
        print("Email cannot be blank. Please try again.")
        return get_email()
    return email    

def create_password():
    """Create a password with confirmation"""
    password = input("Password: ").strip()
    if password == "":
        print("Password cannot be blank. Please try again.")
        return create_password()
    confirmPassword = input("Confirm Password: ").strip()
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
    if username == "":
        print("Username cannot be blank. Please try again.")
        return createUsername(usernames)
    
    # If it exists, try again
    if username in usernames:
        print("Username is taken. Please try again.")
        return createUsername(usernames)
    else:
        return username

def load_cities_from_api(city_name):
    """Load city data from the API"""
    response = requests.get(api_url, headers={'X-Api-Key': api_key}, params={'city': city_name})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None

def check_city_exists(city_name):
    """Check if a city exists using the API"""
    city_data = load_cities_from_api(city_name)
    if city_data:
        for city in city_data:
            if city['name'].lower() == city_name.lower():
                return True
    return False

def checkOrigin():
    while True:
        city1 = input("Please input one city/town you would like to follow: ").strip().lower()
        if city1 == "":
            print("City cannot be blank. Please try again.")
            continue
        if not check_city_exists(city1):
            print("City not found. Please try again.")
            continue
        else:
            print("All cities are valid.")
        break

    while True:
        city2 = input("Please input another city/town you would like to follow: ").strip().lower()
        if city2 == "":
            print("City cannot be blank. Please try again.")
            continue
        if not check_city_exists(city2):
            print("City not found. Please try again.")
            continue
        else:
            print("All cities are valid.")
        break

    while True:
        city3 = input("Please input one final city/town you would like to follow: ").strip().lower()
        if city3 == "":
            print("City cannot be blank. Please try again.")
            continue
        if not check_city_exists(city3):
            print("City not found. Please try again.")
            continue
        break

    return city1, city2, city3

def checkPractice():
    practice = input("Please input your practice (ex: ashekenaz, sephardi, chabad, etc.): ").strip()
    if practice == "":
        print("Practice cannot be blank. Please try again.")
        return checkPractice()  
    return practice

def checkKohen():
    Kohen = input("Are you a Kohen? (yes or no): ")
    if Kohen.lower() == "yes":
        Kohen = True
    else:
        Kohen = False
    return Kohen

def checkRelevance():
    while True:
        relevance = input("Please input your relevance score (1-10): ").strip()
        if relevance.isdigit() and 1 <= int(relevance) <= 10:
            return int(relevance)
        else:
            print("Relevance score must be a number between 1 and 10. Please try again.")

# Ask for user info
def get_user_info():
    # Creates a unique ID for each user
    id = str(uuid.uuid4())
    firstName = get_first_name()
    lastName = get_last_name()   
    userName = createUsername(uploadUsernames())
    email = get_email()
    password = create_password()
    city1, city2, city3 = checkOrigin()
    practice = checkPractice()
    Kohen = checkKohen()
    relevance = checkRelevance()

    # Stores the date that the account is created with formatting for month/day/year
    dateCreated = datetime.datetime.now().strftime("%m/%d/%Y")
    user = User(id, firstName, lastName, userName, email, password, dateCreated, city1, city2, city3, practice, Kohen, relevance)
    user.handleInfo()
    return userName

def createAccount():
    # Welcome the user to the account creation page
    print("Please input the following information to create an account.")
    get_user_info()
    print("Account created successfully.")

createAccount()