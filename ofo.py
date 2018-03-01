# coding=utf-8
import urllib
import json
import time
import MySQLdb


search_url = ""

post_header = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
    "X-Requested-With": "XMLHttpRequest"
}

START_ID = 100001
END_ID = 110001

HOST = '106.14.176.105'
DB_NAME = 'ofo'
DB_USER = 'root'
DB_PWD = 'RbTnc2QxLaAGlF30'
TB_NAME = "ofo"
PORT = 3306


def set_pwd(code, pwd):
    conn_a = MySQLdb.connect(db=DB_NAME, user=DB_USER, passwd=DB_PWD, host=HOST, port=PORT)
    cur_a = conn_a.cursor()
    sql_str = "INSERT INTO %s values('%s', '%s', '%s')" % (TB_NAME, code, code, pwd)
    cur_a.execute(sql_str)
    conn_a.commit()
    cur_a.close()
    conn_a.close()


def get_code(start_id, end_id):
    for i in range(start_id, end_id):
        f = urllib.urlopen(search_url, "code={0}".format(i), post_header)
        rsp = f.read()
        rsp_json = json.loads(rsp)
        if rsp_json['success'] is True:
            pwd = rsp_json['password']
        else:
            pwd = rsp_json['code']
        set_pwd(str(i), pwd)
        import random
        time.sleep(random.uniform(0.1, 10.0))


# print rsp
if __name__ == "__main__":
    get_code(START_ID, END_ID)




