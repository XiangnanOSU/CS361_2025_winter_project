import json
import time
# function to put request into pipe file
def request_service(request):
    pipe_file = "csv_service.json"
    with open(pipe_file, "w") as f:
        json.dump(request, f, indent=4)
    time.sleep(1)
    with open(pipe_file, "r") as f:
        request = json.load(f) 
    return request

# request
# action: "run", "done"(after service process)
# csv_file_path: csv file to be parsed
# data: parsed data
# info: error information. If successfully, info = ""

# Besides response from service, user can additionaly request the parsed data is writen into json/txt/csv file
# output_format: json/txt/csv
# output_path: additional ouput file path
my_request = {
        "action": "run",
        "csv_file_path": "./data/people.csv",
        "output_format": "json",
        "output_path": "./data/people.json",
        "data": "",
        "info": ""}
#response
response = request_service(my_request)
if response["action"] == "done":
    print("...")
    print("Data is received successfully!")
    print(response["data"])



    

