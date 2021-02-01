import requests
import operator
from functools import reduce

key = '1683239661:AAFcEH4HMuUj1pI4KnJleRZ9tt3gkv8kttU'
url = f'https://api.telegram.org/bot{key}/getUpdates'
resp = requests.get(url).json()

for i in resp['result']:
    if not (i['message']['text'].rfind('/jdfruit')):
        try:
            # print(i['message']['text'].split(' ')[1])
            with open('jdfruit_code.txt', 'a') as f:
                f.write(i['message']['text'].split(' ')[1])
                f.write('\n')
        except IndexError:
            pass
        continue

