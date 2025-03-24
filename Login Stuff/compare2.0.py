import json

dataFile = "Login Stuff/data/userInfo.json"
postsFile = "Login Stuff/data/posts.json"

#Load a file with data
def load_file(file):
    with open(file) as f:
        return json.load(f)

def compare_posts_accounts(user_info_file, posts_file):
    """Compares the accounts and posts and sees if a post has a 
    place matching what the user is interested in"""
    
    # loads the files
    user_info = load_file(user_info_file)
    posts = load_file(posts_file)
    
    matching_posts = []
    # Lopp through the users 
    for user in user_info:
        # If it has "city" in it
        if "city" in user:
            # Load the preferred cities
            user_cities = user["city"]
            
            # Loop through the posts
            for post in posts:
                #If the post's city is watched by user 
                if post["city"] in user_cities:
                    # add it to the list
                    matching_posts.append((user["username"], post["city"], post["title"]))
    
    return matching_posts

def main():
    matching_posts = compare_posts_accounts(dataFile, postsFile)
    #Notify the user
    for username, city, post_id in matching_posts:
        print(f"Hello {username}, we have found a match for {city}. The title of the post is: '{post_id}'\n")
main()
