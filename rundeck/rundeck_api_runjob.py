import requests

url = "http://localhost:4440/api/21/job/dd1b5845-efa8-48e7-89dc-b0e351d1a562/run"

payload  = {}
headers = {
  'Accept': 'application/json',
  'X-Rundeck-Auth-Token': 'Wm9fyhan8DB9kO532fO2LtcijweGJ40F',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))