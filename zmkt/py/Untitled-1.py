endpoint = 'http://e26917e6-882b-49f9-a214-54be23233555.brazilsouth.azurecontainer.io/score'
key = 'uebM5YzQwdfe4eNl4T2MKAYAKnLAll5q'

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

#Get the first prediction in the results
print("Prediction:", y["result"][0])
if y["result"][0] == 1:
      print('Amor o mercado vai cair. VENDE SAPORRA!!')
      else:
      print("Amor o mercado vai subir. COMPRA SAPORRA!!")
      else:
      print(response)