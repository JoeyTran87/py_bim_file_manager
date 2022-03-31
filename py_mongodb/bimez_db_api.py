import requests
import json
url = "https://data.mongodb-api.com/app/data-nfgez/endpoint/data/beta"

payload = json.dumps({
    "collection": "facilityType",
    "database": "cofico",
    "dataSource": "Cluster0",
    "projection": {
        "_id": 1
    }
})
headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': '62033e81c5f363a8e0a7f9ea'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
