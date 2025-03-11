with open("input.txt", 'a') as f_in:
    f_in.write("calculate_days 2025-04-03\n")

with open("output.txt", 'r') as f:
    x = f.readline()
print(x)