import random
import time
import threading


def generate_random_command():
    # Define possible command types and parameters
    command_type = random.choice([
        "convert_time_zones", 
        "convert_duration", 
        "calculate_days", 
        "calculate_due_date"
    ])

    if command_type == "convert_time_zones":
        timestamp = random.choice(["2025-02-21-12:40:00", "2025-03-15-08:30:00", "2025-04-10-17:25:00"])
        from_zone = random.choice(["America/Los_Angeles", "America/New_York", "Europe/London"])
        to_zone = random.choice(["America/New_York", "Europe/London", "Asia/Tokyo"])
        return f"{command_type} {timestamp} {from_zone} {to_zone}"

    elif command_type == "convert_duration":
        amount = random.choice([2, 5, 10, 20])
        from_unit = random.choice(["hours", "minutes"])
        to_unit = "minutes" if from_unit == "hours" else "hours"
        return f"{command_type} {amount} {from_unit} {to_unit}"

    elif command_type == "calculate_days":
        date = random.choice(["2025-02-24", "2025-05-01", "2025-08-15"])
        return f"{command_type} {date}"

    elif command_type == "calculate_due_date":
        duration = random.choice(["5 days", "10 hours", "120 minutes", "2 days", "30 minutes"])
        return f"{command_type} {duration}"

def append_random_command_to_file(filename):
    # Generate a random command
    command = generate_random_command()

    # Append the command to the file
    with open(filename, 'a') as file:
        file.write(command + "\n")

    print(f"Command generated and added: {command}")

def read_output_file(filename):
    # Read and display the content of output.txt
    with open(filename, 'r') as output_file:
        output_file.seek(0, 2)  # Start from the end of the file (to avoid reading old data)
        while True:
            line = output_file.readline()
            if line:
                print(f"Output: {line.strip()}")
            else:
                time.sleep(0.1)

# Keep generating random commands and writing to the input file
filename = "input.txt"
output_reader_thread = threading.Thread(target=read_output_file, args=('output.txt',))
output_reader_thread.daemon = True  # This ensures the thread exits when the main program ends
output_reader_thread.start()

while True:
    append_random_command_to_file(filename)
    time.sleep(2)  # Wait for 2 seconds before generating the next command
