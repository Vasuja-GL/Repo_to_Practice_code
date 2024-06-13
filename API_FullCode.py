######   Question 1. Send /get requests and validate response code########
import requests 
  
# Making a get request 
resp = requests.get('https://httpbin.org/') 
#Added Assertion
assert resp.status_code == 200, "Unexpected status code: " + str(resp.status_code)
# print response 
print(resp) 
  
# print request status_code 
print(resp.status_code) 

### Output ###
##<Response [200]>
# 200
###  Output when status_code is not equal to 200 ####
# AssertionError: Unexpected status code: 404




######   Question 2. Send /post request with json body and validate response contains relevant data ########

import requests

testdata = {"Candidate name": "Vasuja Kookkal", "email": "vasuja.kookkal@globallogic.com"}

response = requests.post("https://httpbin.org/post", json=testdata)
print(response.status_code)
assert response.status_code == 200, "Unexpected status code: " + str(response.status_code)
print(response.text)

####  OutPut  ###
# 200
# {
#   "args": {}, 
#   "data": "{\"Candidate name\": \"Vasuja Kookkal\", \"email\": \"vasuja.kookkal@globallogic.com\"}", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "*/*", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Content-Length": "79", 
#     "Content-Type": "application/json", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.32.3", 
#     "X-Amzn-Trace-Id": "Root=1-6665dc41-59d5e40b6a7e06aa14203769"
#   }, 
#   "json": {
#     "Candidate name": "Vasuja Kookkal", 
#     "email": "vasuja.kookkal@globallogic.com"
#   }, 
#   "origin": "101.0.62.138", 
#   "url": "https://httpbin.org/post"
# }

###  Output when status_code is not equal to 200 ####
# AssertionError: Unexpected status code: 404





######   Question 3. Validate request with delayed response ########

import requests 
  
# Making a get request with delayed response
resp = requests.get('https://httpbin.org/delay/10') 
  
# print response 
print(resp) 
  
# print request status_code 
print(resp.status_code) 
assert resp.status_code == 200, "Unexpected status code: " + str(resp.status_code)

### Output ###
# <Response [200]>
# 200

###  Output when status_code is not equal to 200 ####
# AssertionError: Unexpected status code: 404





# ######   Question 4. Write any negative scenario ########
#  Example1 ## Negative test case for invalid URL   

import requests 
invalid_response = requests.get("https://httpbin.org/inalid_url")  # Using an invalid URL
assert invalid_response.status_code == 404, "Expected a 404 status code, but got: " + str(invalid_response.status_code)
    
#  Example2 ## Here passing a wrong url to see the error in response - by using try except block

import requests 
  
url = "https://httpbin.org/invalid_url"
  
try: 
    r = requests.get(url, timeout=1) 
    r.raise_for_status() 
except requests.exceptions.HTTPError as errh: 
    print("HTTP Error") 
    print(errh.args[0]) 
# Prints the response code 
print(r) 

# #####   Output   ######
# # HTTP Error
# # 404 Client Error: NOT FOUND for url: https://httpbin.org/wrong_url
# # <Response [404]>





# ############### Question 5. Simulate Unauthorized Access   #####
###  Here user is trying to pass an Invalid token to reproduce Unauthorized Access error ###
from pipedrive.client import Client

client = Client(domain="https://test-sandbox38.pipedrive.com/")
client.set_api_token("48ab0394d695cb52ee8ad72589eeed6ed440")   # This is an invalid token. Correct token is 48ab0394d695cb52ee8ad72589eeed6ed44048de

resp = client.deals.get_all_deals()
print(resp)
# #####   Output   ######
# Traceback (most recent call last):
#   File "/Users/vasuja.kookkal/Desktop/Practice/Assignment/API_Testing.py", line 96, in <module>
#     resp = client.deals.get_all_deals()
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pipedrive/deals.py", line 11, in get_all_deals
#     return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pipedrive/client.py", line 94, in _get
#     return self._request("get", url, params=params, **kwargs)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pipedrive/client.py", line 119, in _request
#     return self._parse(requests.request(method, url, headers=_headers, params=_params, **kwargs))
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages/pipedrive/client.py", line 135, in _parse
#     raise exceptions.UnauthorizedError(error, response)
# pipedrive.exceptions.UnauthorizedError: unauthorized access
