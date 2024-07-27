import http.client
import json

print("We are trying to execute an API call through Resquest Cleint")
# The API endpoint
url = "fakestoreapi.com"
connection = http.client.HTTPSConnection(url)
# A GET request to the API
connection.request("GET", "/products/1")
response = connection.getresponse()
encoding = response.info().get_content_charset('utf8')
# Print the response
print("Status: {} and reason: {}".format(response.status, response.reason))
if(response.status == 200 and response.reason == 'OK'):
    responseObject =json.loads(response.read().decode(encoding))
    print("Title: {}".format(responseObject['title']))
else:
    print('Issue in calling the API')
connection.close()
