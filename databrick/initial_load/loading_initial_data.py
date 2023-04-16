import pathlib
import requests
import json

data_file=pathlib.Path("./data/databricks-dolly-15k.json")
with open(data_file) as fh:
    all_records=json.load(fh)

url = 'http://localhost:8000/api/v1/'
headers = {'Content-type': 'application/json'}


for i,record in enumerate(all_records):
    json_record=json.dumps(record)
    response = requests.post(url, data=json_record, headers=headers)
    if response.status_code == 201:
        print(f"{i+1}/{len(all_records)} Data added successfully!")
    else:
        print(f"{i+1}/{len(all_records)} Error adding data:", response.content)