# coding=utf-8
import urllib
import json
import time


search_url = ""

post_header = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest"
}

START_ID = 100000
END_ID = 200000


def get_code(start_id, end_id):
    for i in range(start_id, end_id):
        f = urllib.urlopen(search_url, "code={0}".format(i), post_header)
        rsp = f.read()
        rsp_json = json.loads(rsp)
        if rsp_json['success'] is True:
            print rsp_json['password']
        else:
            print rsp_json['code']
        import random
        time.sleep(random.uniform(0.1, 10.0))
        # time

# print rsp

if __name__ == "__main__":
    get_code(START_ID, END_ID)




