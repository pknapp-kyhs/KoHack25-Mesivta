import json

dataFile = "userInfo.json"

# Read the existing data from the JSON file
with open(dataFile, "r") as f:
    data = json.load(f)


for account in data:
    city1 = account.get("city1")
    city2 = account.get("city2")
    city3 = account.get("city3")
    if city1 =  in usernames:
        duplicates.append(username)
    else:
        usernames.add(username)

if duplicates:
    print(f"Duplicate usernames found: {duplicates}")
else:
    print("No duplicate usernames found.")