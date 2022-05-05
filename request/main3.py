import requests
from pprint import pprint

param = {
    'site': 'stackoverflow',
    'activity': '02.05.2022',
    'creation': '02.04.2022',
    'votes': 300
}
response = requests.get('https://api.stackexchange.com/answers/', params=param)
pprint(dir(response))
pprint(response.status_code)
pprint(response.json())