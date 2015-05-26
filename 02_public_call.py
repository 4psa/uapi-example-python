import httplib
import json
 
# Modify these values with the ones you intend to use
VN_SERVER_ADDRESS   = 'CHANGEME'
API_ACCESS_TOKEN    = 'CHANGEME'
EXTENSION_NUMBER    = 'CHANGEME'
PUBLIC_NUMBER1      = 'CHANGEME'
PUBLIC_NUMBER2      = 'CHANGEME'
 
# Setup the requests parameters
data = {
    "extension": EXTENSION_NUMBER,
    "phoneCallView" : [{
        "source" : PUBLIC_NUMBER1,
        "destination": PUBLIC_NUMBER2           
    }]
}
 
headers = {"Content-type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
 
# Makes a HTTP POST request using SSL
conn = httplib.HTTPSConnection(VN_SERVER_ADDRESS)
conn.request("POST", "/uapi/phoneCalls/@me/simple", json.dumps(data), headers)
 
# Parses the JSON response
response = conn.getresponse()
print json.dumps(json.loads(response.read()), indent=4) 

