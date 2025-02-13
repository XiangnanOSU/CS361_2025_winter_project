import os

def login_view():
    print("Do you already have an account to login?")
    print("1. Yes, I am a current user")
    print("2. No, I am a new user")
    choice = input("Select: ")
    if choice == "1":
        login_current_user()
    elif choice == "2":
        login_new_user()
    elif choice == "3":
        main_view()


def login_current_user():
    while True:
        print("\nPlease provide your username and password, press Enter to contine.")
        user_name = input("1. Username: ")
        user_pwd = input("1. Password: ")
        #print(f"Your username: {user_name}")
        #print(f"Your password: {user_pwd}")
        if user_profile_valid(user_name, user_pwd):
            print("Login successfully")
            break
        else:
            print("Invalid user profile.Try agian")
            continue

def login_new_user():
    while True:
        print("Please setup your username and password, press Enter to contine.")
        user_name = input("1. Username: ")
        user_pwd = input("2. Password: ")
        print(f"Your username: {user_name}")
        print(f"Your password: {user_pwd}")
        if user_name_valid(user_name):
            register_user(user_name, user_pwd)
            break
        else:
            print("User name exists. Please use another one")
            continue
    login_current_user()

def register_user(name, pwd):
    file_path = "./data/users_db.csv"
    if os.path.exists(file_path):
        with open(file_path,'a') as file:
            file.write(f"{name} {pwd}\n")
    else:
        with open(file_path, 'w') as file:
            file.write(f"{name} {pwd}\n")
    print("User account created successfully.")

    #create user events file
    file_name = f"./data/lib_{name}.csv"
    header = "ID,Name,Type,Date,Stopwatch,Detail\n"
    with open(file_name, 'w') as file:
        file.write(header)

def user_profile_valid(name, pwd):
    file_path = "./data/users_db.csv"
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            for line in file:
                str = line.split()
                if name == str[0] and pwd == str[1]:
                    return True     
    else:
        return False
    
def user_name_valid(name):
    file_path = "./data/users_db.csv"
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            for line in file:
                if name in line:
                    return False     
    return True   