from model.user import User

import csv

# get all user detailsprint
def get_users():
    users = []
    with open("./data/user.csv", mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            users.append(User(**row))
    return users

def get_user(id: int):
    users = get_users()
    for user in users:
        if user.id == id:
            return user
    return None
    
