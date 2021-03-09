import requests

Base = "http://127.0.0.1:5000/"

response = requests.put(Base + "channel/24", {'name': 'Monish', 'issue': 'Cannot login to udemy', 'type': 'Login'})
print(response.json())

response = requests.put(Base + "channel/45", {'name': 'Samuel', 'issue': 'getiing redirected many times',
                                              'type': 'Redirect'})
print(response.json())
response = requests.put(Base + "channel/64", {'name': 'Kavin', 'issue': 'GESS is not opening up', 'type': 'Portal'})
print(response.json())
response = requests.put(Base + "channel/82", {'name': 'Ram', 'issue': 'Cannot login to udemy', 'type': 'Login'})
print(response.json())
response = requests.put(Base + "channel/94", {'name': 'Anshal', 'issue': 'Not able to generate payslip',
                                              'type': 'Portal'})
print(response.json())
input()

response = requests.get(Base + "channel/82")
print(response.json())
input()


response = requests.patch(Base + "channel/82", {'issue': 'Udemy is getting redirected', 'type': 'Web'})
print(response.json())