# raise - used to raise exceptions

def homeScreen():
    print("Welcome to this ATM")

def register():
    in_list = ['name','email','password','age']

    for i in in_list:
        user_data = input("Enter your {} : ".format(i))

        if i == 'age' and int(user_data) < 18:
            raise ValueError("Age must be greater than 18")

        # if i == 'age' and int(user_data) < 18:
        #     print("Age must be greater than 18")
        #     break

    # else:
    #     print("{} is {}".format(i,user_data))
    #     print("Registered Successfully...")

    print("Registered Successfully...")
    homeScreen()

# register()

try:
    register()
except ValueError as err:
    print(err)