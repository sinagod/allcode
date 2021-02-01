import requests
import operator
from functools import reduce


if "TG_KEY" in os.environ:
    """
    判断是否运行自GitHub action,"XMLY_SPEED_COOKIE" 该参数与 repo里的Secrets的名称保持一致
    """
    print("执行自GitHub action")
    tg_key = os.environ["TG_KEY"]

# tg_key = '1683239661:AAFcEH4HMuUj1pI4KnJleRZ9tt3gkv8kttU'
url = f'https://api.telegram.org/bot{tg_key}/getUpdates'
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

