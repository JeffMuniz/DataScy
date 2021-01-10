endpoint = 'http://dacd9ff0-2a81-48d5-9606-daf95d1f1b32.brazilsouth.azurecontainer.io/score'
key = 'rRDerxExsIolVi4qdOoC4O6O2Xr3Lqgd'

import json
import requests

x = [{"Date": "Jan 12, 2021",
      "Price": 5.118,
      "Open": 5.1108,
      "High": 6.9408,
      "Low": 1.3208 }]
      

#Create a "data" JSON object
input_json = json.dumps({"data": x})

#Set the content type and authentication for the request
headers = {"Content-Type":"application/json",
           "Authorization":"Bearer " + key}

#Send the request
response = requests.post(endpoint, input_json, headers=headers)

print(response.content)
print(response.json)
print(response.content)