
import request
import pandas as pd
from datetime import datetime
import os


# Configuration
REALM = "nhausa.quickbase.com"
TABLE_ID = "bjt7nptpm"
USER_TOKEN = "b9ntif_bmp7_0_bcn59hstf6mcpci8hgq4cdpeeiw"
#REPORT_ID = 1293  


url = f'https://api.quickbase.com/v1/records/query'

headers = {
    "QB-Realm-Hostname": REALM,
    "Authorization": f"QB-USER-TOKEN {USER_TOKEN}",
    'User-Agent': 'PythonScript',
    "Content-Type": "application/json"
}
payload = {
    "from": TABLE_ID,
    "select": [], 
    "options": {
        "skip": 0,
        "top": 1000  
    }
}
response = requests.post(url, headers=headers, json=payload)

print("Status:", response.status_code)
#print("Response Text:", response.text)
data = print(response.json())


url = 'https://api.quickbase.com/v1/records/query'

headers = {
    "QB-Realm-Hostname": REALM,
    "Authorization": f"QB-USER-TOKEN {USER_TOKEN}",
    'User-Agent': 'PythonScript',
    "Content-Type": "application/json"
}
body = {
    "reportId": 1293,
    "from": TABLE_ID,
    "options": {
        "skip": 0,
        "top": 1000  
    }
}
response = requests.post(url, headers=headers, json=body)

print("Status:", response.status_code)
if response.status_code == 200:
    field_data = response.json()['data']
    field_mapping = {field['id']: field['label'] for field in field_data}
    
    print("Field Mapping:", field_mapping)
#print("Response Text:", response.text)
#data = print(response.json())


if response.status_code == 200:
    data = response.json()['data']
    df = pd.DataFrame(data)
    print(df)
        
      
    df.to_csv("quickbase_data.csv", index=False)


os.getcwd()


    def flatten_record(record):
        return {
            key: (val['value'] if isinstance(val, dict) else val) for key, val in record.items()
        }

    # Flatten the records
    records = [flatten_record(record) for record in data]

    # Create a DataFrame from the records
    df = pd.DataFrame(records)
    print(df)





