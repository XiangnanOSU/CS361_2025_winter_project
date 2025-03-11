import json
import datetime

def send_request_to_service_events(request):
    pipe_file = "pipe_events.json"
    with open(pipe_file, "w") as f:
        json.dump(request, f, indent=4)
    with open(pipe_file, "r") as f:
        request = json.load(f) 
    return request

event = {}
#event["created"] = datetime.date.today()
#event["frequency"] = 4

event["type"] = input("Event type [Work/Health/Family/Others: ")
d = int(input("Stopwatch days: "))
event["active"] = input("Active(yes/no): ")
event["stopwatch"] = str(datetime.timedelta(days=d))


my_request = {"event": [event],
                "action": "add",
                "username": "luca",
                "password": " ",
                "status": "pending",
                "message": ""}
response = send_request_to_service_events(my_request)