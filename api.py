import json
import requests
from connect_db import connect

url = 'https://api.genkimiru.jp/api/v1/user/my_data/dashboard'
tokens = connect('SELECT token FROM accounts WHERE id = 19778')
t = None
for token in tokens:
    t = token[0]
headers = {
    'token': f'{t}'}
params = {"current_time": "1714702855"}
response = requests.get(url, headers=headers, params=params)
if response.status_code == 200:
    data = response.json()
    formatted_json = json.dumps(data, indent=4)
    # print("DATA", formatted_json)
    data_1 = json.loads(formatted_json)
    body = data_1['body']
    body_1 = body['data']
    sleep = body_1['sleep']
    print('Sleep:', sleep)
    total = sleep['total_sleep_time']
    print('Total sleep time :', total)
    print("DATA", formatted_json)
else:
    print("Error ",  response.status_code, response.text)
