import requests
#city = input()
#Request API
#response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=7dc3694ccc543e704c2e7d90a0f6c1f2')
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Bangkok&lang=th&appid=7dc3694ccc543e704c2e7d90a0f6c1f2')
report = response.json()
report = report['main']
ce = report['temp']-273.15
print(ce)