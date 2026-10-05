import requests
import csv
import json

with open("backend/MOCK_DATA.csv", mode="r", newline ="", encoding="utf-8") as csvFile:
    reader_object = list(csv.reader(csvFile))
    for row in reader_object:
        print(row)
with open("backend/MOCK_DATA.json", mode="w", encoding="utf-8") as jsonFile:
    json.dump(reader_object, jsonFile, indent=4)
    data = json.load(jsonFile)

for item in data:
    response = response = requests.post("http://localhost:8000/items/")
    json = item
    


# def import_data():
#     url = "/MOCK_DATASET.csv"
#     response = requests.get(url)
#     with open("MOCK_DATASET.csv", "wb") as f:
#         f.write(response.content)


