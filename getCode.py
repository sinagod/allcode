import os
import json
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

# 写入数据
def getCode(tg_key):
    url = f'''https://api.telegram.org/bot{tg_key}/getUpdates'''
    try:
        resp = requests.get(url).json()
        for i in resp['result']:
            if not (i['message']['text'].rfind('/jdfruit')):
                try:
                    with open('jdfruit_code.txt', 'a') as f:
                        f.write(i['message']['text'].split(' ')[1])
                        f.write('\n')
                except IndexError:
                    pass
                continue
    except:
        print(traceback.format_exc())
        return


# 去重数据
def formateCode():
    with open('jdfruit_code.txt', 'a') as f:
        for line1 in f.readlines():
            line1 = line1.replace('\n', '')
            m.append(line1)
        for line2 in m:
            line2 = line2.split('&')
            n.append(line2)
    return list(set(reduce(operator.add, n)))


# 上传数据
def loadCode(func):
    data = func()
    for line in data:
        with open('fruit.txt', 'a') as f:
            f.write(line + '\n')


def run():
    getCode(tg_key)
    loadCode(formateCode())
    

if __name__ == '__main__':
    run()
