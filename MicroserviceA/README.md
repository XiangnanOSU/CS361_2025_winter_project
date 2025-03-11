# Microservice Unit Converter

## Introduction

This microservice provides various functions to convert time zones, durations, and calculate due dates. It is designed to process requests from a client and send responses back. The goal is to offer clear and reliable communication between the microservice and any client interacting with it.

## Communication Contract

The microservice handles requests for time zone conversion, duration conversion, days calculation, and due date calculation. The client can programmatically request data, and the microservice will respond with the requested results.

### 1. Requesting Data from the Microservice

To request data from the microservice, you will need to send a request in the correct format to the service endpoint. The microservice listens for requests from an `input.txt` file, which contains the specific actions to be performed.

#### Example Request

```txt
convert_time_zones 2025-02-21-12:40:00 PST America/New_York
convert_duration 2 hours minutes
calculate_days 2025-02-24
calculate_due_date 5 days
```

Each line of the input.txt corresponds to a different action and will be processed accordingly. Here’s what each request means:

1. convert_time_zones: Converts the provided time from one time zone to another.
2. convert_duration: Converts a duration from one unit to another (e.g., from hours to minutes).
3. calculate_days: Calculates how many days are left from today to the given date.
4. calculate_due_date: Adds the given duration (e.g., 5 days, 10 hours) to today’s date and returns the resulting date.

You can write your own code to send these requests to input.txt.

#### Example Request (Programmatically)
If you're writing a Python script to request data from the microservice, you would simply write the actions into input.txt, like so:

```python
# Example Python script to request data from the microservice
# Write the request data to input.txt
with open('input.txt', 'w') as f:
    f.write("convert_time_zones 2025-02-21-12:40:00 PST America/New_York\n")
    f.write("convert_duration 2 hours minutes\n")
    f.write("calculate_days 2025-02-24\n")
    f.write("calculate_due_date 5 days\n")
```
    
### 2. Receiving Data from the Microservice
After the microservice processes the data, it writes the results to output.txt. The results will be written one per line in the same order as the requests.

#### Example Request (in output.txt)
```txt
2025-02-21-15:40:00-EST
120
3
2025-02-26 00:00:00
2025-02-21 22:40:00
2025-02-21 14:40:00
```
The response corresponds to the results of the following actions:

1. Time Zone Conversion: 2025-02-21 15:40:00 EST (converted from 2025-02-21 12:40:00 PST).
2. Duration Conversion: 120 (2 hours converted to minutes).
3. Days Calculation: 3 (from 2025-02-21 to 2025-02-24).
4. Due Date Calculation: The due date after adding 5 days, 10 hours, and 120 minutes to today.

You can use a Python script to read output.txt like this:

```python
# Example Python script to read the output from the microservice

with open('output.txt', 'r') as f:
    response = f.readlines()

for line in response:
    print(line.strip())  # Print each line of the response
```

### 3. UML Sequence Diagram
Below is a UML sequence diagram that illustrates how the client requests data and receives a response from the microservice.
```
+--------------+           +------------------+           +------------------+
|    Client    |           |   Microservice   |           |     File System  |
+--------------+           +------------------+           +------------------+
       |                           |                            |
       |    1. Request (input.txt) |                            |
       |-------------------------->|                            |
       |                           |    2. Process input        |
       |                           |--------------------------->|
       |                           |                            | 
       |                           |   3. Write output to       |
       |                           |       output.txt           |
       |                           |<---------------------------|
       |    4. Read output.txt     |                            |
       |<--------------------------|                            |
       |                           |                            |
+--------------+           +------------------+           +------------------+
```

Diagram Steps:
1. Request: The client writes the input data to input.txt, which includes the conversion requests.
2. Processing: The microservice reads input.txt, processes each line, and generates the corresponding result.
3. Output: The microservice writes the results to output.txt.
4. Read Output: The client reads the processed data from output.txt.

## Conclusion
This microservice provides a flexible way to handle various time zone and duration conversions, as well as day calculations. The communication contract described here allows the client to interact with the microservice by reading from input.txt and receiving results in output.txt. The sequence diagram illustrates the flow of data, ensuring a clear understanding of how the system works.
