import time
import random
import json
import csv

def save_data_to_file(request, output_format, output_path):
    data = request["data"]
    try:
        # If the requested format is JSON
        if output_format.lower() == "json":
            with open(output_path, "w") as json_file:
                json.dump(data, json_file, indent=4)
        
        # If the requested format is TXT
        elif output_format.lower() == "txt":

            with open(output_path, "w") as txt_file:
                header = []

                if len(data) > 0:
                    header = list(data[0].keys())
                #print(header)
                for i in range(len(header)):
                    if i == len(header) - 1:
                        txt_file.write(f"{header[i]}\n")
                    else:
                        txt_file.write(f"{header[i]},")
                for row in data:
                    for i in range(len(header)):
                        if i == len(header) - 1:
                            txt_file.write(f"{row[header[i]]}\n")
                        else:
                            txt_file.write(f"{row[header[i]]},")
        
        # If the requested format is CSV (exporting the header and rows)
        elif output_format.lower() == "csv":
            if isinstance(data, list) and data:
                with open(output_path, mode='w', newline='') as csv_file:
                    fieldnames = data[0].keys()
                    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(data)
    except Exception as e:
        return {"error": f"An error occurred during export: {str(e)}"}


def handle_request(request):
    pipe_file = "csv_service.json"

    csv_file_path = request.get("csv_file_path")
    output_format = request.get("output_format", "json")
    output_path = request.get("output_path", "")
    data = request.get("data")
    info = []
    info.append(request.get("info"))

    try:
        # Read the CSV file
        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]     
    except FileNotFoundError:
        info.append(f"error: File {csv_file_path} not found.")
    except Exception as e:
        info.append(f"error: {str(e)}")
    
    request["action"] = "done"
    request["data"] = data
    request["info"] = info

    if output_path != "":
        save_data_to_file(request, output_format, output_path)

    with open(pipe_file, "w") as file:
        json.dump(request, file, indent=4)

    print("Request processed successfully!")
    print("Parsed data: ")  
    print(request["data"])

    print("\n")
    print("Hosting service...") 
    print("...")

def process_request():
    print("\n")
    print("Hosting service...")
    print("...")
    while True:
        time.sleep(1)
        #
        request_data = None
        try:
            with open("csv_service.json", "r") as f:
                request_data = json.load(f)
        except:
            pass
        if request_data is not None:
            if isinstance(request_data, dict) and "action" in request_data:
                if request_data.get("action") == "run":
                    print(f"Received request: {request_data}")
                    print("Processing request...")
                    print("...")
                    handle_request(request_data) 
                              

if __name__ == "__main__":
    process_request()