import os
import datetime
#from users_login import *
import tkinter as tk
from tkinter import messagebox

def help_page_view():
    print("-->\n-->\n-->help page view")
    #print("--------------------------------------------------------------------")
    print("--------------------------- HELP -----------------------------------")
    print("1. User need an account to use the app. ")
    print("2. Once login, the user can view the library of current event. For new user, the library is empty.")
    print("3. To add new event, user need to select the “Add Event” option in the prompt.")
    print("4. When adding new event, users can either use the stopwatch (the event will be reminded in days/hours)")
    print("   or the reminder date (the future date event occur).")
    print("5. To delete a event, user need to select the “Delete Event” option in the prompt.")
    print("--------------------------- HELP -----------------------------------")
    print("\n")
    print("Back to main page?")
    print("1. Yes")
    print("2. Exit")
    choice = input("Select: ")
    if choice == "1":
        main_view()
    elif choice =="2":
        exit()

def login_view():
    print("-->\n-->\n-->login view")
    print("Do you already have an account to login?")
    print("1. Yes, I am a current user")
    print("2. No, I am a new user")
    print("3. Exit")
    choice = input("Select: ")
    if choice == "1":
        login_current_user()
    elif choice == "2":
        login_new_user()
    elif choice == "3":
        exit()


def login_current_user():
    user_name = ''
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
    events_library_view(user_name)


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


########################library
def events_library_view(user_name):
    print("-->\n-->\n-->Events Library View")  
    show_events_library(user_name)
    print("Select to proceed")
    print("1. Add event based on stopwatch")
    print("2. Add event based on date")
    print("3. Delete Event")
    print("4. Show Event Details")
    print("5. Exit")
    choice = input("Select: ")
    if choice == "1":
        add_event_stopwatch_view(user_name)
    elif choice == "2":
        add_event_date_view(user_name)
    elif choice == "3":
        delete_event_view(user_name)
    elif choice == "4":
        input_name = input("Which event details? Input event name: ")
        event_details_view(user_name, input_name)
    elif choice =="5":
        exit()
    else:
        print("Invalid input. Select again.")

def add_event_stopwatch_view(user_name):
    print("-->\n-->\n-->Add Event Stopwatch View") 
    print("Enter name, type, stopwatch and details for event.")
    event = {}
    while True:
        event_name = input("Event name: ")
        if event_name_valid(user_name, event_name):
            event["name"] = event_name
            break
        else:
            print("Event name already exist! Try again.")
            continue
    event["type"] = input("Event type [Work/Health/Family/Others: ")
    d = int(input("Stopwatch days: "))
    event["active"] = input("Active(yes/no): ")
    event["stopwatch"] = datetime.timedelta(days=d)
    event["date"] = ""
    event["details"] = input("Event details: ")
    event["created"] = datetime.date.today()
    event["frequency"] = input("Frequency: ")
    e_date = input("Reminder date(yyyy-mm-dd): ")
    e_date = e_date.split('-')
    e_year = int(e_date[0])
    e_month = int(e_date[1])
    e_day = int(e_date[2])
    event["date_reminder"] = datetime.date(e_year,e_month,e_day)

    add_event(user_name, event)
    events_library_view(user_name)

def add_event_date_view(user_name):
    print("-->\n-->\n-->Add Event Date View") 
    print("Enter name, type, date and details for event.")
    event = {}
    while True:
        event_name = input("Event name: ")
        if event_name_valid(user_name, event_name):
            event["name"] = event_name
            break
        else:
            print("Event name already exist! Try again.")
            continue
    event["type"] = input("Event type [Work/Health/Family/Others: ")
    event["active"] = input("Active(yes/no): ")
    event["stopwatch"] = ""
    e_date = input("Event dates (yyyy-mm-dd): ")
    e_date = e_date.split('-')
    e_year = int(e_date[0])
    e_month = int(e_date[1])
    e_day = int(e_date[2])
    event["date"] = datetime.date(e_year,e_month,e_day)
    event["details"] = input("Event details: ")
    event["created"] = datetime.date.today()
    event["frequency"] = input("Frequency: ")

    e_date = input("Reminder date(yyyy-mm-dd): ")
    e_date = e_date.split('-')
    e_year = int(e_date[0])
    e_month = int(e_date[1])
    e_day = int(e_date[2])
    event["date_reminder"] = datetime.date(e_year,e_month,e_day)
    add_event(user_name, event)
    events_library_view(user_name)

def show_events_library(user_name):
    print("\n----------------------Events Library----------------------------")
    file_path = f"./data/lib_{user_name}.csv"
    with open(file_path,'r') as file:
        for line in file:
            print(line)
    print("\n----------------------Events Library----------------------------")

def add_event(user_name, e):
    if e["date"] == "":
        e["date"] = e["created"] + e["stopwatch"]
    else:
        e["stopwatch"] = e["date"] - e["created"]
    with open(f"./data/lib_{user_name}.csv", 'a') as file:
        file.writelines(f'{e["name"]},{e["type"]},{e["active"]},{e["date"]},{e["stopwatch"].days},{e["created"]},{e["frequency"]},{e["date_reminder"]},{e["details"]}\n')
        
def event_name_valid(user_name, e_name):
    file_path = f"./data/lib_{user_name}.csv"
    if os.path.exists(file_path):
        with open(file_path,'r') as file:
            for line in file:
                str = line.split(',')
                if e_name == str[0]:
                    return False     
    return True   

def delete_event_view(user_name):
    print("-->\n-->\n-->Delete Event View") 
    show_events_library(user_name)
    e_name = input("Input event name to delete: ")

    root = tk.Tk()
    root.withdraw()
    response = messagebox.askyesno("Confirm", "Are you sure you want to delete the event? Once confirm, it will be deleted permanently!")
    if response:
        print("You chose Yes.")
        delete_event(user_name, e_name)
    else:
        print("You choose No.")
    events_library_view(user_name)
    

def delete_event(user_name, e_name):
    file_path = f"./data/lib_{user_name}.csv"
    all_lines = []
    with open(file_path,'r') as file:
        for line in file:
            str = line.split(',')
            if e_name != str[0]:
                all_lines.append(line)
    with open(file_path,'w') as file:
        for line in all_lines:
            file.write(line)
    print(f"Delete event {e_name} successfully.")


def event_details_view(user_name, e_name):
    print("-->\n-->\n-->Events Details View") 
    show_event_detail(user_name, e_name)
    print("Select to proceed")
    print("1. Edit the event")
    print("2. Delete the event")
    print("3. Back to Event Library View")
    print("4. Exit")
    choice = input("Select: ")
    if choice == "1":
        edit_event_view(user_name, e_name)
    elif choice == "2":
        delete_event(user_name, e_name)
        events_library_view(user_name)
    elif choice == "3":
        events_library_view(user_name)
    elif choice =="4":
        exit()
    

def show_event_detail(user_name, e_name):
    file_path = f"./data/lib_{user_name}.csv"
    header = ''
    event_query=''
    with open(file_path,'r') as file:
        header = file.readline()
    with open(file_path,'r') as file:
        for line in file:
            str = line.split(',')
            if e_name == str[0]:
                event_query = line
    header = header.replace("\n","")
    event_query = event_query.replace("\n","")
    header = header.split(',')
    event_query = event_query.split(',')
    #print(header)
    #print(event_query)
    print("\n----------------------Event Detail----------------------------")
    for i in range(len(header)):
        print(f"{header[i]}: {event_query[i]}")
    print("\n----------------------Event Detail----------------------------")

def edit_event_view(user_name, e_name):
    print("-->\n-->\n-->Edit Event View") 
    print("Please enter to modify your event.")
    #print("For unmodified field, just press enter.")
    event = {}
    event["name"] = e_name
    event["type"] = input("Event type [Work/Health/Family/Others: ")
    event["active"] = input("Active(yes/no): ")
    event["stopwatch"] = ""
    e_date = input("Event dates (yyyy-mm-dd): ")
    e_date = e_date.split('-')
    e_year = int(e_date[0])
    e_month = int(e_date[1])
    e_day = int(e_date[2])
    event["date"] = datetime.date(e_year,e_month,e_day)
    event["details"] = input("Event details: ")
    event["created"] = datetime.date.today()
    event["frequency"] = input("Frequency: ")

    e_date = input("Reminder date(yyyy-mm-dd): ")
    e_date = e_date.split('-')
    e_year = int(e_date[0])
    e_month = int(e_date[1])
    e_day = int(e_date[2])
    event["date_reminder"] = datetime.date(e_year,e_month,e_day)
    edit_event(user_name, e_name, event)
    event_details_view(user_name, e_name)

def edit_event(user_name, e_name, e):
    if e["date"] == "":
        e["date"] = e["created"] + e["stopwatch"]
    else:
        e["stopwatch"] = e["date"] - e["created"]

    file_path = f"./data/lib_{user_name}.csv"
    all_lines = []
    with open(file_path,'r') as file:
        for line in file:
            str = line.split(',')
            if e_name != str[0]:
                all_lines.append(line)
            else:
                newline = (f'{e["name"]},{e["type"]},{e["active"]},{e["date"]},{e["stopwatch"].days},{e["created"]},{e["frequency"]},{e["date_reminder"]},{e["details"]}\n')
                all_lines.append(newline)

    with open(file_path,'w') as file:
        for line in all_lines:
            file.write(line)
    print(f"Edit event: {e_name} successfully.")


def main_view():
    #print("\n")
    print("-->\n-->\n-->main view")
    print("--------------------------------------------------------------------")
    print("----------------------Event Reminder App----------------------------")
    print("                          Welcome!                               ")
    print("This event reminder app help the user manage important events such")
    print("as daily work, workout, birthday reminder, family events and so on.")
    print("The user can add, delete, search, and view their events.")
    print("----------------------Event Reminder App----------------------------")
    print("--------------------------------------------------------------------")
    #print("\n")
    print("Would you like to continue to login?")
    print("1. Yes")
    print("2. No")
    print("3. Help")
    print("4. Exit")
    choice = input("Select: ")
    if choice == "1":
        login_view()
    elif choice == "2":
        print("log out")
    elif choice == "3":
        help_page_view()
    elif choice =="4":
        exit()

if __name__ == "__main__":
    main_view()