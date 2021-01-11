#Send the request
response = requests.post(endpoint, input_json, headers=headers)

#If we got a valid response, display the predictions
if response.status_code == 200:
    y = json.loads(response.json())
var = int(input(json.loads(response.json())))    
if y > 0:
    print("Positive number")
elif y == 0:
    print("Zero")
else:
    print("Negative number")