import json

dataFile = "Login Stuff/data/userInfo.json"
postsFile = "Login Stuff/data/posts.json"

def load_json_file(file):
    with open(file) as f:
        return json.load(f)

def get_wanted_cities(user_info):
    wanted_cities = []
    for user in user_info:
        if "wantedCities" in user:
            wanted_cities.extend(user["wantedCities"])
    return wanted_cities

def find_matching_posts(user_info_file, posts_file):
    user_info = load_json_file(user_info_file)
    posts = load_json_file(posts_file)
    
    wanted_cities = get_wanted_cities(user_info)
    
    matching_posts = []
    for post in posts:
        if post["city"] in wanted_cities:
            matching_posts.append(post)
    
    return matching_posts

matching_posts = find_matching_posts(dataFile, postsFile)
for post in matching_posts:
    print(f"Post ID: {post['id']}, Title: {post['title']}, Location: {post['location']}")