import os
import json
import time
import requests
import operator
import traceback
from functools import reduce

###################################################
# tg_key = '1683239661:AAFcEH4HMuUj1pI4KnJleRZ9tt3gkv8kttU'
m = []
n = []


###################################################

if "TG_KEY" in os.environ:
    tg_key = os.environ["TG_KEY"]

if not tg_key:
    print(f'''【通知参数】 is empty,DTask is over.''')
    exit()


###################################################

# 处理数据
def getCode(tg_key):
    global d
    url = f'https://api.telegram.org/bot{tg_key}/getUpdates'
    try:
        resp = requests.get(url).json()
        # print(resp)
        for i in resp['result']:
            if not (i['message']['text'].rfind('/jdfruit')):
                try:
                    with open('jdfruit_code.txt', 'a+') as f:
                        f.write(i['message']['text'].split(' ')[1])
                        f.write('\n')
                except IndexError:
                    pass
                continue

        time.sleep(10)
        with open('jdfruit_code.txt') as f:
            for line1 in f.readlines():
                line1 = line1.replace('\n', '')
                m.append(line1)
            for line2 in m:
                line2 = line2.split('&')
                n.append(line2)
        d = list(set(reduce(operator.add, n)))
        loadCode(d)

    except:
        print(traceback.format_exc())
        return


# 上传数据
def loadCode(d):
    # data = func()
    for line in d:
        with open('fruit.txt','a') as f:
            f.write(line + '\n')
            

def run():
    getCode(tg_key)


if __name__ == '__main__':
    run()
            
            
            
            
            
