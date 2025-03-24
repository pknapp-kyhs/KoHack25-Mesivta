import json

dataFile = "userInfo.json"
postsFile = "posts.json"

# Read the user info from the JSON file
with open(dataFile, "r") as f:
    data = json.load(f)

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
               #creates a set of all items that start with 'city' from the account data
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

def compare_cities_with_posts(data, posts_data):
    matching_pairs = []
    for i, account in enumerate(data):
        account_cities = {value for key, value in account.items() if key.startswith("city")}
        for j, post in enumerate(posts_data):
            post_cities = {value for key, value in post.items() if key.startswith("city")}
                                  # checks if two lists have overlapping cities
            if not account_cities.isdisjoint(post_cities):
                matching_pairs.append((i, j))
    return matching_pairs

# Example usage
info = get_account_info()

matching_pairs = compare_cities(data)
if matching_pairs:
    for pair in matching_pairs:
        print(f"Accounts {pair[0] + 1} and {pair[1] + 1} have matching cities.")
else:
    print("No matching cities found between accounts.")

matching_pairs_with_posts = compare_cities_with_posts(data, posts_data)
if matching_pairs_with_posts:
    for pair in matching_pairs_with_posts:
        print(f"Account {pair[0] + 1} and Post {pair[1] + 1} have matching cities.")
else:
    print("No matching cities found between accounts and posts.")