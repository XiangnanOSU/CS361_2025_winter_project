import os
import json
import datetime

# The JSON file for communication
#LOGIN_JSON_FILE = "login_request.json"
#USER_DB_FILE = "./data/users_db.csv"
def add_event(user_name, e):

    if e["date"] == "":
        created = datetime.datetime.strptime(e["created"], "%Y-%m-%d")
        created = created.date()
        days = int(e["stopwatch"].split()[0].replace('days', ''))
        stopwatch = datetime.timedelta(days=days)

        e["date"] = created + stopwatch
        e["date"] = str(e["date"])
    else:
        created = datetime.datetime.strptime(e["created"], "%Y-%m-%d")
        created = created.date()
        date = datetime.datetime.strptime(e["date"], "%Y-%m-%d")
        date = date.date()

        e["stopwatch"] = date - created
        e["stopwatch"] = str(e["stopwatch"])
    with open(f"./data/lib_{user_name}.csv", 'a') as file:
        file.writelines(f'{e["name"]},{e["type"]},{e["active"]},{e["date"]},{e["stopwatch"]},{e["created"]},{e["frequency"]},{e["date_reminder"]},{e["details"]}\n')


def process_request():
    print("\n")
    print("Event Service Listening to request...")
    print("...")
    while True:
        # login in user
        request = {}
        try:
            with open("pipe_events.json", "r", encoding='utf-8-sig') as f:
                request = json.load(f) 
        except:
            pass
        
        if "action" not in request:
            continue

        if request["action"] == "add-stopwatch" or request["action"] == "add-date":
            add_event(request["username"], request["event"][0])
            request["action"] = "done"
            request["status"] = "success"
            request["message"] = "Add event successfully"
            with open("pipe_events.json", "w") as f:
                json.dump(request, f, indent=4)
            print(request["message"])

if __name__ == "__main__":
    process_request()