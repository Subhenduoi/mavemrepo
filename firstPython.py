import http.client
import json
import os

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
    
    # Read Json Data from a json file and seiralize to a jons Object
    print('basename:    ', os.path.basename(__file__))
    print('dirname:     ', os.path.dirname(__file__))
    print(os.path.join(os.path.dirname(__file__), 'inputJson.json'))
    dataFile = open(os.path.join(os.path.dirname(__file__), 'inputJson.json'), "r")
    json_post_data = json.dumps(json.load(dataFile))
    dataFile.close()
    print(json_post_data)

    #Posting the Content to the API
    headers = {'Content-type': 'application/json'}
    connection.request('POST', '/products', json_post_data, headers)
    response = connection.getresponse()
    
    print("Status: {} and reason: {}".format(response.status, response.reason))
    
    encoding = response.info().get_content_charset('utf8')
    responseObject=json.loads(response.read().decode(encoding))
    print(responseObject)
    if(response.status == 200 and response.reason == 'OK'):
        with open(os.path.join(os.path.dirname(__file__), 'response.json'), 'w', encoding='utf-8') as f:
            json.dump(responseObject, f, ensure_ascii=False, indent=4)
    else:
        print('Issue in calling the POST API')
else:
    print('Issue in calling the GET API')
connection.close()
