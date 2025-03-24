import json

dataFile = "Login Stuff/data/userInfo.json"
postsFile = "Login Stuff/data/posts.json"

def load_data_file(file):
    with open(file) as f:
        return json.load(f)

def load_posts_file(file):
    with open(file) as f:
        return json.load(f)

def compare_posts_accounts(user_info_file, posts_file):
    user_info = load_data_file(user_info_file)
    posts = load_posts_file(posts_file)
    
    matching_posts = []
    for user in user_info:
        if "city" in user:
            user_cities = user["city"]
            for post in posts:
                if post["city"] in user_cities:
                    matching_posts.append((user["username"], post["city"], post["title"]))
    
    return matching_posts

def main():
    matching_posts = compare_posts_accounts(dataFile, postsFile)
    for username, city, post_id in matching_posts:
        print(f"Hello {username}, we have found a match for {city} that you are following. The title of the post is is {post_id}\n")

