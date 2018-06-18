from datetime import datetime

users = []
userData = {}

posts = []
postData = {}

def login_success(current_user):
    print("Welcome to FB")
    print("""
    1. Post Something
    2. View Profile
    3. Update Profile
    4. Delete Profile
    5. Logout
    """)

    userChoice = input("Enter your choice : ")

    choices = {
        "1" : post,
        "2" : view_profile,
        "3" : update_profile,
        "4" : delete_profile,
        "5" : logout
    }

    choices.get(userChoice,err_handler)(current_user)

def post(current_user):
    user_post = input("Post Here : ")

    postData['post'] = user_post
    postData['username'] = current_user['name']
    postData['date'] = datetime.date()

    posts.append(postData.copy())

    print(postData)


def view_profile(current_user):
    pass

def update_profile(current_user):
    pass

def delete_profile(current_user):
    pass

def logout(current_user):
    pass

def register():
    username = input("Enter your name : ")
    usermail = input("Enter your mailID : ")

    userData['name'] = username
    userData['email'] = usermail

    while True:
        userpwd = input("Enter your password : ")
        conf_pwd = input("Confirm Password : ")
        if userpwd == conf_pwd:
            userData['password'] = userpwd
            break
        else:
            print("Password do not match")

    users.append(userData.copy())

    for user in users:
        print(user)

def login():
    emailId = input("Enter emailID : ")
    pwd = input("Enter Password : ")

    for user in users:
        if user['email'] == emailId and user['password'] == pwd:
            print("Login Success")
            login_success(user)
            break
    else:
        print("Login Failed")

def err_handler():
    print("Wrong Choice...")

while True:

    print("""
    1. Register
    2. Login
    """)

    user_choice = input("Enter your choice : ")

    todo = {
        "1" : register,
        "2" : login
    }

    todo.get(user_choice, err_handler)()







