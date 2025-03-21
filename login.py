import os
import json

dataFile = "userInfo.json"

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
    data = load_data()
    username = input("Enter username...\n").strip()  # Strip any leading/trailing spaces
    #print(f"Looking for username: {username}")
    
    for user in data:
        #print(f"Checking user: {user}")
        if username in user.values():
            #print(f"Found user: {user}")
            return user
    
    print("Username not found")
    return None

#This code is not finished and will not work
