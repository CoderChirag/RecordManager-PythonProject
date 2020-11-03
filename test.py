import json

with open('student.json', 'r') as f:
    # Getting data from the student file
    json_data = json.load(f)
    print(type(json_data))
    # Pasrsing the json data to create a dictionary
    # data_dict = json.loads(json_data)
    print("old data found")
