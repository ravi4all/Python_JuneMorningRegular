from datetime import datetime
import readWrite

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
    postData['date'] = datetime.now().date()

    posts.append(postData.copy())

    # print(posts)
    for p in posts:
        print(p)

    login_success(current_user)


def view_profile(current_user):

    print("Your ID :",current_user['email'])
    print("Your Name :",current_user['name'])

    for p in posts:
        if p['username'] == current_user['name']:
            print("Post",p['post'])
            print("Post",p['date'])

    login_success(current_user)


def update_profile(current_user):
    to_update = input("What do you want to update ? ")
    updated_value = input("Enter updated {}".format(to_update))

    if to_update == 'name':
        current_user['name'] = updated_value
    elif to_update == 'email':
        current_user['email'] = updated_value

    login_success(current_user)

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

    # users.clear()
    users.append(userData.copy())

    readWrite.save_user(userData)
    print("Data Saved...")

    for user in users:
        print(user)

def login():
    user = readWrite.read_user()

    # user = ["'ram','ram@gmail.com','ram'\n'shyam'..."]

    # print(type(user))
    # print(user[0].split("\n"))
    user = user[0].split("\n")

    # user = [
    #     ['ram','ram@gmail.com','ram'],
    #     ['shyam','shyam@gmail.com','1234']
    # ]

    emailId = input("Enter emailID : ")
    pwd = input("Enter Password : ")

    for i in range(len(user)):
        if emailId in user[i] and pwd in user[i]:
            print("Login Success")
            login_success(user)
            break
    else:
        print("Login Failed...")

    # for user in users:
    #     if user['email'] == emailId and user['password'] == pwd:
    #         print("Login Success")
    #         login_success(user)
    #         break
    # else:
    #     print("Login Failed")


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







