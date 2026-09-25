### Task 2.11: Get Key with Maximum Value
print("Task 2.11: Get Key with Maximum Value")

given_dict = {
    "dalmations": 101, 
    "pi": 3.14,
    "life": 42,
    "googol": 10**100,
    "jordan": 23,
    "life, the universe and everything": 42, 
    "emergency": 911,
    "euler": 2.71828
}

max_key = ""
max_value = 0
for key in given_dict:
    max_key = key if given_dict[key] > max_value else max_key
    max_value = given_dict[key] if given_dict[key] > max_value else max_value


print(f"Max Key: {max_key}")
print(f"Max Value: {max_value}")