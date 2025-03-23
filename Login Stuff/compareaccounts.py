import json

dataFile = "userInfo.json"

# Read the existing data from the JSON file
with open(dataFile, "r") as f:
    data = json.load(f)


for account in data:
    username = account.get("username")
    if username in usernames:
        duplicates.append(username)
    else:
        usernames.add(username)

if duplicates:
    print(f"Duplicate usernames found: {duplicates}")
else:
    print("No duplicate usernames found.")