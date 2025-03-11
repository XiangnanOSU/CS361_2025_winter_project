import os
import json

# The JSON file for communication
#LOGIN_JSON_FILE = "login_request.json"
#USER_DB_FILE = "./data/users_db.csv"

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
    header = "Name,Type,Active,Date,Stopwatch,Created,Frequency,DateReminder,Detail\n"
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

def process_request():
    print("\n")
    print("Login Service Listening to request...")
    print("...")
    while True:
        # login in user
        request = {}

        try:
            with open("pipe_login.json", "r", encoding='utf-8-sig') as f:
                request = json.load(f) 
        except:
            pass
        

        if "action" not in request:
            continue

        if request["action"] == "login":
            if user_profile_valid(request["username"], request["password"]):
                request["action"] = "done"
                request["status"] = "success"
                request["message"] = "login successfully" 
            else:
                request["action"] = "done"
                request["status"] = "fail"
                request["message"] = "login fail. Invalid user profile.Try agian." 

            with open("pipe_login.json", "w") as f:
                json.dump(request, f, indent=4)
            print("Login request processed with status:")
            print(request["action"])
            print(request["status"])
            print(request["message"])
        
        # create new user
        if request["action"] == "create":
            if user_name_valid(request["username"]):
                register_user(request["username"], request["password"])
                request["action"] = "done"
                request["status"] = "success"
                request["message"] = "Create new user successfully" 
            else:
                request["action"] = "done"
                request["status"] = "fail"
                request["message"] = "Create new user fail" 

            with open("pipe_login.json", "w") as f:
                json.dump(request, f, indent=4)
            print("Create request processed with status:")
            print(request["action"])
            print(request["status"])
            print(request["message"])


if __name__ == "__main__":
    process_request()