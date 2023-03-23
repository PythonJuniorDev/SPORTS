import requests
import json

# #the required first parameter of the 'get' method is the 'url':
# x = requests.get('https://w3schools.com/python/demopage.htm')

# #print the response text (the content of the requested file):
# print(x.text)

req = requests.get("https://api.postalpincode.in/pincode/110001")
response = req.json()
for item in response:
    print(item['Message'])
    print(item['Status'])
    postalArray = item['PostOffice']
    for k in postalArray:
        print(k['Name'])
        print(k['District'])

        

