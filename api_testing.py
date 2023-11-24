import requests
import json

# Define the API endpoint
api_url = "http://localhost:5000/process_judgment"

# Replace with the actual file path you want to test
file_path = r'C:\Users\Hdsadmin\Downloads\12.txt' 

# Prepare the data to send in the request
data = {
    "file_path": file_path,
    "run_type": "sent"  # Optional, specify the run_type if needed
}

# Send a POST request to the API
response = requests.post(api_url, json=data)

# Check the response
if response.status_code == 200:
    result = response.json()
    print("Entity extraction result:")
    # print(json.dumps(result, indent=4))
else:
    print("API request failed with status code:", response.status_code)

