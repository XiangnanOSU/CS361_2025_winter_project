import os
import json
import datetime
import csv

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

def export_events(user_name, outfile):
    csv_filename = f"./data/lib_{user_name}.csv"
    txt_filename = f"./{outfile}.txt"

    with open(csv_filename, 'r', newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Open the TXT file in write mode
        with open(txt_filename, 'w', encoding='utf-8') as txt_file:
            # Loop through each row in the CSV
            for row in csv_reader:
                # Join the values in the row and write to the TXT file
                txt_file.write('\t'.join(row) + '\n')

def process_request():
    print("\n")
    print("Export Service listening to request...")
    print("...")
    while True:
        # login in user
        request = {}
        try:
            with open("pipe_export.json", "r", encoding='utf-8-sig') as f:
                request = json.load(f) 
        except:
            pass
        
        if "action" not in request:
            continue

        if request["action"] == "export":
            export_events(request["username"], request["outputfile"])
            request["action"] = "done"
            request["status"] = "success"
            request["message"] = f"Export events successfully to file: {request["outputfile"]}.txt."
            with open("pipe_export.json", "w") as f:
                json.dump(request, f, indent=4)
            print(request["message"])

if __name__ == "__main__":
    process_request()