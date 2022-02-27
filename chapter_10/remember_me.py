import json

def get_stored_username():

    """Get stored username if available."""

    filename = 'chapter_10/usernames.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new user name"""

    filename = 'chapter_10/usernames.json'   
    username = input("What is your name? ")
    with open(filename, 'w') as f_object:
        json.dump(username, f_object)
    
    return username

def greet_user():
    """Greet the user."""

    username = get_stored_username()
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_new_username()
        print(f"Don't worry {username}, we'll remember you when you return.")

greet_user()