

#request through json
#1. define request parameter
csv_input = "expense1.csv"
format = "json"
#2. write input parameter into request.json
{   
"action": [
    {"request": "parse"},
    {"csv_path": csv_input},
]
}
#3. csv_parser read request.json
#4. csv_parser process request


# receive data
#4. csv_parser process request
#5. csv_parser parser data from input csv
#6. csv_parser write data into request.json
#7. Caller open reqeust.json and read returned data