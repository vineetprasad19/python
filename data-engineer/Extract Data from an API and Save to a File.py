
# Extract Data from an API and Save to a File
# This script fetches data from a REST API and saves it as a JSON file.

import requests
import json

# API endpoint
url = 'https://api.example.com/data'
headers = {'Authorization': 'Bearer YOUR_API_KEY'}

# Fetch data
response = requests.get(url, headers=headers)
data = response.json()

# Save to JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)
print("Data saved to data.json.")