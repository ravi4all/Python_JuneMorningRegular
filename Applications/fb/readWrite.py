import csv

def save_user(data):

    with open('users.csv','a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data.values())
        # for row in data:
        #     writer.writerow(row)

def read_user():
    records = []
    with open('users.csv') as file:
        users = file.read()
        records.append(users)

        # for user in users:
        # records.append(user)

    return records

def check_email():
    pass