import httplib
import json
# Modify these values with the ones you intend to use
VN_SERVER_ADDRESS       = 'CHANGEME'
API_ACCESS_TOKEN        = 'CHANGEME'
PHONECALL_ID            = 'CHANGEME'
PHONECALLVIEW_ID        = 'CHANGEME'
# Setup the requests parameters
data = {
    'action': 'Park',
    'phoneCallViewId': PHONECALLVIEW_ID
}
headers = {"Content-type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
# Makes a HTTP PUT request using SSL
conn = httplib.HTTPSConnection(VN_SERVER_ADDRESS)
conn.request("PUT", "/unifiedapi/phoneCalls/@me/@self/"+PHONECALL_ID, json.dumps(data), headers)
# Parses the JSON response
response = conn.getresponse()
print json.dumps(json.loads(response.read()), indent=4)

