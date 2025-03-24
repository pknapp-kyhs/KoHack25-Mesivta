import json

dataFile = "Login Stuff/data/userInfo.json"
postsFile = "Login Stuff/data/posts.json"
print(dataFile)
# Read the user info from the JSON file
with open(dataFile, "r") as f:
    data = json.load(f)
    print(f"\n{data}\n")
# Read the posts info from the JSON file
with open(postsFile, "r") as f:
    posts_data = json.load(f)


def get_account_info():
    """
    Get the user chosen cities from the first user in the data.
    """
    for a in data:
        city1, city2, city3 = a["city1"], a["city2"], a["city3"]
        break  # Only get the cities from the first user
    return city1, city2, city3

def cities_match(account1, account2):
    #creates a dictionary of all items that start with 'city' from the account data
    cities1 = {value for key in account1 if key.startswith("city")}
    cities2 = {value for key in account2 if key.startswith("city")}
    return not cities1.isdisjoint(cities2)

def compare_cities(data):
    city_pairs = []
    #first loop loops through all the cities in account 1
    for i, account1 in enumerate(data):
        #second loop loops through all the cities in account 2
        for j, account2 in enumerate(data):
#this compares them to make sure they arent comapring to themselves while also seeing if theyre the same
            if i != j and cities_match(account1, account2):
    #this adds accounts with matching cities to a list
                city_pairs.append((i, j))
    return city_pairs

def compare_cities_with_posts(data, posts_data):
    matching_pairs = []
    # this loops through all the accounts and makes note of their cities
    for i, account in enumerate(data):
        account_cities = {for key in account if key.startswith("city")}
    #this loops through all the posts and makes note of their cities
        for j, post in enumerate(posts_data):
            post_cities = {for key in post if key.startswith("city")}
    # checks if two lists have overlapping cities
            if not account_cities.isdisjoint(post_cities):
                if cities_match(account_cities, post_cities):
                    matching_pairs.append((i))
                    
                    print("cities match")
    print(matching_pairs)
    return matching_pairs

info = get_account_info()

"""matching_pairs = compare_cities(data)
if matching_pairs:
        print(f"Accounts {pair[0] + 1} and {pair[1] + 1} have matching cities.")
else:
    print("No matching cities found between accounts.")
"""
matching_pairs_with_posts = compare_cities_with_posts(data, posts_data)
if matching_pairs_with_posts:
    for pair in matching_pairs_with_posts:
        print(f"Account {pair[0] + 1} and Post {pair[1] + 1} have matching cities.")
else:
    print("No matching cities found between accounts and posts.")
    print(matching_pairs_with_posts)