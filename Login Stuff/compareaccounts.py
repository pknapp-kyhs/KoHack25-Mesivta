import json

dataFile = "Login Stuff/data/userInfo.json"
postsFile = "Login Stuff/data/posts.json"

def load_data_file(file):
    with open(file) as f:
        userData = json.load(f)
    #with open(postsFile) as f:
     #   postsData = json.load(f)
    for a in userData:
        print(a)
        if a == "city":
            print()
    return userData

#def compare_posts_accounts():
    #cities1 = {value for key, value in load_data_file(dataFile) if key.startswith("city")}
    #print(cities1)
    #cities2 = {value for key, value in postsFile if key.startswith("city")}
    #print(cities2)
    #return not cities1.isdisjoint(cities2)  # Returns True if there's a common city

load_data_file()
#compare_posts_accounts()