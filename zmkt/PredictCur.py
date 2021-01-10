endpoint = 'http://dacd9ff0-2a81-48d5-9606-daf95d1f1b32.brazilsouth.azurecontainer.io/score'
key = 'rRDerxExsIolVi4qdOoC4O6O2Xr3Lqgd'

import json
import requests

x = [{"Date": "Jan 08, 2021",
      "Price": 5.4178,
      "Open": 5.4108,
      "High": 5.4408,
      "Low": 5.3208}]
      #"Change %": "0.14%"}]

#Create a "data" JSON object
input_json = json.dumps({"data": x})

#Set the content type and authentication for the request
headers = {"Content-Type":"application/json",
           "Authorization":"Bearer " + key}

#Send the request
response = requests.post(endpoint, input_json, headers=headers)

#If we got a valid response, display the predictions
if response.status_code == 200:
    y = json.loads(response.json())
    #Get the first prediction in the results
    print("Prediction:", y["result"][0])
    if y["result"][0] == 1:
        print('Diabetic')
    else:
        print("Not Diabetic")
else:
    print(response)