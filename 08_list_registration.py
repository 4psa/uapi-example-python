import httplib
import json
 
# Modify these values with the ones you intend to use
VN_SERVER_ADDRESS       = 'CHANGEME'
API_ACCESS_TOKEN        = 'CHANGEME'
EXTENSION_NUMBER        = 'CHANGEME'
 
# Setup the requests parameters
headers = {"Content-type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
 
# Makes a HTTP GET request using SSL
conn = httplib.HTTPSConnection(VN_SERVER_ADDRESS)
conn.request("GET", "/uapi/extensions/@me/"+EXTENSION_NUMBER+"/presence", None, headers)
 
# Parses the JSON response
response = conn.getresponse()
print json.dumps(json.loads(response.read()), indent=4)

