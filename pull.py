#This program exports Okta groupId users to a CSV
# HOW TO RUN PROGRAM: python3 pull.py <enter okta groupId>
import requests
import json
import sys, os
import csv
from datetime import date
from datetime import datetime

#groupID
var = sys.argv[1]

#api call
url = "https://<URL>/api/v1/groups/" + var + "/users"
payload = ""
headers = {
    'Accept': "application/json",
    'Content-Type': "application/json",
    'Authorization': "SSWS <API KEY>",
    'cache-control': "no-cache",
    'Postman-Token': "<Postman-Token>"
    }

#writing JSON output to a txt file
response = requests.request("GET", url, data=payload, headers=headers)
today = str(date.today())
with open('out.txt', 'w') as f:
	f.write(response.text)

#parse JSON output to CSV
with open('out.txt') as json_data:
	d = json.load(json_data)
	outputFile = open('output' + '-' + today +'.csv', 'w')
	outputWriter = csv.writer(outputFile)
	#Change 'profile' and/or 'login' ([item['profile']['login']]) to grab different json data
	for item in d:
		outputWriter.writerow([item['profile']['login']])
