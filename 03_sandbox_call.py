import httplib
import json
 
# Modify these values with the ones you intend to use
VN_SERVER_ADDRESS   = 'CHANGEME'
API_ACCESS_TOKEN    = 'CHANGEME'
EXTENSION_NUMBER    = 'CHANGEME'
SANDBOX_NUMBER      = 'CHANGEME'
 
# Setup the requests parameters
data = {
    "extension": EXTENSION_NUMBER,
    "phoneCallView" : [{
        "source" : EXTENSION_NUMBER,
        "destination": SANDBOX_NUMBER        
    }]
}
headers = {"Content-type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
 
# Makes a HTTP POST request using SSL
conn = httplib.HTTPSConnection(VN_SERVER_ADDRESS)
conn.request("POST", "/uapi/phoneCalls/@me/simple", json.dumps(data), headers)
 
# Parses the JSON response
response = json.loads(conn.getresponse().read())
print json.dumps(response, indent=4)

