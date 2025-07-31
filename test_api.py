import requests
import json

# Load JSON data
with open("test_data2.json", "r") as file:
    data = json.load(file)


# online link to the API https://credit-card-fraud-detection-api-hsrz.onrender.com
# Send POST request to your local API
response = requests.post("https://credit-card-fraud-detection-api-hsrz.onrender.com/predict", json=data)

# Show the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())


"""
#other method to test all json files at once
for i in range(4):
    name = "test_data$.json".replace('$',str(i))
    with open(name) as file:
        data = json.load(file)
    response = requests.post("http://127.0.0.1:5000/predict",json=data)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
"""
