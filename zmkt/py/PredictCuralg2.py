endpoint = 'http://2bce8a8c-8f24-4922-877c-14b38b86957c.brazilsouth.azurecontainer.io/score'
key = 'ulUGe6d1TldTQBleipi5jmb8vuM8ieJJ'


import json
import requests

x = [{"Date": "Jan 12, 2021",
      "Price": 12.4178,
      "Open": 7.4108,
      "High": 9.4408,
      "Low": 3.3208}]
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
    print(y)
    #Get the first prediction in the results
    print("Prediction:", y["result"][0])
    if y["result"][0] == 1:
        print('Diabetic')
    else:
        print("Not Diabetic")
else:
    print(response)