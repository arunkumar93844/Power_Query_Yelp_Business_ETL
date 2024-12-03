# The script reads the NDJSON file line by line and organizes the data into a structured JSON list.
# The output file is saved as a new JSON file.
import json

with open(r"C:\Users\Administrator\Desktop\data analytics\Projects\Data\yelp_academic_dataset_business.json",'r') as file:
    data_array = file.read()
    file.close()

data_array = [line for line in data_array.split('\n')]

with open(r"C:\Users\Administrator\Desktop\data analytics\Projects\Data\yelp_academic_dataset_business_formatted(1).json",'w') as file:
    json.dump(data_array, file, indent= 4)
    file.close()
