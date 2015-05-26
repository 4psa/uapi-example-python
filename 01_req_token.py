import httplib
import json
 
# Modify these values with the ones you intend to use
VN_SERVER_ADDRESS = 'CHANGEME'
APP_KEY = 'CHANGEME'
APP_SECRET = 'CHANGEME'
REDIRECT_URI = 'https://' + VN_SERVER_ADDRESS + '/ouath/token.php'
TYPE = 'unifiedapi'
URI = 'https://' + VN_SERVER_ADDRESS + '/oauth/token.php'
 
# Setup the requests parameters
headers = {"Content-type": "application/x-www-form-urlencoded"}
content = "&client_id=" + APP_KEY + "&client_secret=" + APP_SECRET + "&grant_type=client_credentials&type=" + TYPE + "&redirect_uri=" + REDIRECT_URI
conn = httplib.HTTPSConnection(VN_SERVER_ADDRESS)
conn.request("POST",URI, content, headers)
 
# Parses the JSON response
response = conn.getresponse()
print json.dumps(json.loads(response.read()), indent=4)

