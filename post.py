import json
import uuid
import os

class Post:
    """Create a 'Post' class"""
    def __init__(self, id, title, msg, loc, image, audio):
        self.id = id
        self.title = title
        self.msg = msg
        self.loc = loc
        self.image = image
        self.audio = audio

    def send_to_file(self):
        """Send the post to a json file"""
        post = {
            "id": self.id,
            "title": self.title,
            "message": self.msg,
            "location": self.loc,
            "image": self.image,
            "audio file": self.audio
        }

        # Store the post in a file
        with open("posts.json", "r") as f:
            posts = json.load(f)
            posts.append(post)

        with open("posts.json", "w") as f:
            json.dump(posts, f, indent= 4)


def create_post():
    """Get all the post info from the user"""

    id = str(uuid.uuid4())
    title = input("Enter the title of the post.\n")
    msg = input("Add some notes about it.\n")
    loc = input("Where is it from?\n")
    image = upload_image()
    audio = upload_audio()
    
    # Create an instance of the Post with all of the user
    post = Post(id, title, msg, loc, image, audio)
    return post

def upload_image():
    """Handle the image upload"""
    
    file_name = input("Enter the link to the file (.jpeg, .png, or .jpg)\n")
    # Check if it's a valid image file and if it exists
    if file_name.lower().endswith(('.jpeg', '.png', '.jpg')) and os.path.exists(file_name):
        # Return the name of the file
        return file_name
    # Otherwise...
    print("File not found")
    return upload_image()

def upload_audio():
    file_name = input("Enter name of audio file. (.MP3 ONLY!)\n")
    # Check if it's a valid audio file and if it exists
    if file_name.endswith(".mp3") and os.path.exists(file_name):
        # Return the name of the file
        return file_name
    
    print("File not found")
    return upload_audio()

post = create_post()
post.send_to_file()