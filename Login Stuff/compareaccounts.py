import json

dataFile = "userInfo.json"

# Read the existing data from the JSON file
with open(dataFile, "r") as f:
    data = json.load(f)

def get_account_info(index):
    if index < 0 or index >= len(data):
        return None
    account = data[index]
    city1 = account.get("city1")
    city2 = account.get("city2")
    city3 = account.get("city3")
    return city1, city2, city3

def cities_match(account1, account2):
    cities1 = {value for key, value in account1.items() if key.startswith("city")}
    cities2 = {value for key, value in account2.items() if key.startswith("city")}
    return not cities1.isdisjoint(cities2)

def compare_cities(data):
    city_pairs = []
    for i, account1 in enumerate(data):
        for j, account2 in enumerate(data):
            if i != j and cities_match(account1, account2):
                city_pairs.append((i, j))
    return city_pairs

# Example usage
index = 1  # Change this to the index you want to get info from
info = get_account_info(index) 


matching_pairs = compare_cities(data)
if matching_pairs:
    for pair in matching_pairs:
        print(f"Accounts {pair[0] + 1} and {pair[1] + 1} have matching cities.")
else:
    print("No matching cities found between accounts.")