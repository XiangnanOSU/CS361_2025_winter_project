import os
import datetime
#from users_login import *
import tkinter as tk
from tkinter import messagebox
import json
import time
import random


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

#####################################################################################
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

def send_request_to_service_login(request):
    pipe_file = "pipe_login.json"
    with open(pipe_file, "w") as f:
        json.dump(request, f, indent=4)
    time.sleep(1)
    with open(pipe_file, "r") as f:
        request = json.load(f) 
    return request


def login_current_user():
    user_name = ''
    while True:
        print("\nPlease provide your username and password, press Enter to contine.")
        user_name = input("1. Username: ")
        user_pwd = input("2. Password: ")

        my_request = {"action": "login",
                      "username": user_name,
                      "password": user_pwd,
                      "status": "pending",
                      "message": ""}
        response = send_request_to_service_login(my_request)
        print(response["message"])
        if response["status"] == "success":
            break
        else:
            continue
    events_library_view(user_name)

def login_new_user():
    while True:
        print("Please setup your username and password, press Enter to contine.")
        user_name = input("1. Username: ")
        user_pwd = input("2. Password: ")

        print(f"Your username: {user_name}")
        print(f"Your password: {user_pwd}")
        my_request = {"action": "create",
                      "username": user_name,
                      "password": user_pwd,
                      "status": "pending",
                      "message": ""}
        response = send_request_to_service_login(my_request)
        print(response["message"])
        if response["status"] == "success":
            break
        else:
            continue
    login_current_user()
#####################################################################################
def send_request_to_service_events(request):
    pipe_file = "pipe_events.json"
    with open(pipe_file, "w") as f:
        json.dump(request, f, indent=4)
    time.sleep(1)
    with open(pipe_file, "r") as f:
        request = json.load(f) 
    return request

def show_events_library(user_name):
    print("\n----------------------Events Library----------------------------")
    file_path = f"./data/lib_{user_name}.csv"
    with open(file_path,'r') as file:
        for line in file:
            print(line)
    print("\n----------------------Events Library----------------------------")

def events_library_view(user_name):
    print("-->\n-->\n-->Events Library View")  
    show_events_library(user_name)
    print("Select to proceed")
    print("1. Add event based on stopwatch")
    print("2. Add event based on date")
    print("3. Delete Event")
    print("4. Show Event Details")
    print("5. Export history")
    print("6. Exit")
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
        export_history_view(user_name)
    elif choice =="6":
        exit()
    else:
        print("Invalid input. Select again.")

def send_request_to_service_history(request):
    pipe_file = "pipe_export.json"
    with open(pipe_file, "w") as f:
        json.dump(request, f, indent=4)
    time.sleep(1)
    with open(pipe_file, "r") as f:
        request = json.load(f) 
    return request

def export_history_view(user_name):
    selected = input("Export History?[yes/no]")
    if selected:
        outfile = input("Output file name: ")
        my_request = {"action": "export",
                "username": user_name,
                "password": "",
                "outputfile": outfile,
                "status": "pending",
                "message": "" 
                }
    response = send_request_to_service_history(my_request)
    events_library_view(user_name)


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
    event["stopwatch"] = str(datetime.timedelta(days=d))
    event["date"] = ""
    event["details"] = input("Event details: ")
    event["created"] = str(datetime.date.today())
    event["frequency"] = input("Frequency: ")
    e_date = input("Reminder date(yyyy-mm-dd): ")
    e_date = e_date.split('-')
    e_year = int(e_date[0])
    e_month = int(e_date[1])
    e_day = int(e_date[2])
    event["date_reminder"] = str(datetime.date(e_year,e_month,e_day))

    my_request = {"event": [event],
                "action": "add-stopwatch",
                "username": user_name,
                "password": "",
                "status": "pending",
                "message": "" 
                }
    response = send_request_to_service_events(my_request)
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
    event["date"] = str(datetime.date(e_year,e_month,e_day))
    event["details"] = input("Event details: ")
    event["created"] = str(datetime.date.today())
    event["frequency"] = input("Frequency: ")

    e_date = input("Reminder date(yyyy-mm-dd): ")
    e_date = e_date.split('-')
    e_year = int(e_date[0])
    e_month = int(e_date[1])
    e_day = int(e_date[2])
    event["date_reminder"] = str(datetime.date(e_year,e_month,e_day))
    my_request = {"event": [event],
                "action": "add-date",
                "username": user_name,
                "password": "",
                "status": "pending",
                "message": "" 
                }
    response = send_request_to_service_events(my_request)
    events_library_view(user_name)


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
    print("4. Check Due Date")
    print("5. Exit")
    choice = input("Select: ")
    if choice == "1":
        edit_event_view(user_name, e_name)
    elif choice == "2":
        delete_event(user_name, e_name)
        events_library_view(user_name)
    elif choice == "3":
        events_library_view(user_name)
    elif choice == "4":
        check_due_date(user_name, e_name)
        event_details_view(user_name, e_name)
    elif choice =="5":
        exit()
def check_due_date(user_name, e_name):
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
    event_query = event_query.split(',')

    print(event_query)
    print(event_query[3])

    due_date = event_query[3]

    request = f"calculate_days {due_date}"
    response = ''
    with open("./MicroserviceA/input.txt", 'a') as f_in:
        f_in.write(request)
    with open("./MicroserviceA/output.txt", 'r') as f:
        response = f.readline()
    print(f"Request: {request}")
    print(f"Response: {response}")
    print(f"{e_name} will be due in days: {response}")

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

if __name__ == "__main__":
    main_view()