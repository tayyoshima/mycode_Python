import requests
#city = input()
#Request API
response = requests.get('....')
report = response.json()
report = report['main']
ce = report['temp']-273.15
print(ce)
