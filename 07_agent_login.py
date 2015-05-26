import httplib
import json
 
# Modify these values with the ones you intend to use
VN_SERVER_ADDRESS       = 'CHANGEME'
API_ACCESS_TOKEN        = 'CHANGEME'
QUEUE_NUMBER            = 'CHANGEME'
AGENT_NUMBER            = 'CHANGEME'
 
# Setup the requests parameters
data = {'status': '1'}
headers = {"Content-type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
 
# Makes a HTTP PUT request using SSL
conn = httplib.HTTPSConnection(VN_SERVER_ADDRESS)
conn.request("PUT", "/uapi/extensions/@me/"+QUEUE_NUMBER+"/queue/agents/"+AGENT_NUMBER, json.dumps(data), headers)
 
# Parses the JSON response
response = conn.getresponse()
print json.dumps(json.loads(response.read()), indent=4)

