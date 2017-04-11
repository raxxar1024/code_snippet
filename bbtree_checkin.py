#!/usr/bin/env python
#coding=utf-8
import cookielib
import simplejson
import urllib2
import urllib
import json


# m_host = "https://pro.zhihuishu.bbtree.com/service/v2/user/login_v5"
m_host = "https://pro.zhihuishu.bbtree.com/service/v2/user/sigin_in"

data_json = {
    "data": "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+SzWhgkKJ1L"
            "dLWjnZUHRLt/b+FI8iBDY9n+dLu7f6ojvfJ//2Omry/n/0OuLgm"
            "fYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeSHf"
            "aMyS2VSY5r++XUuVWQkq7KYdublbyxH90q+EhXoiaOGC/SGv3Hn"
            "46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo"
            "5eq6HevAY5UZCjyxHytsvWVhD5Eb252uUuoVKb0CoSLj/sZi03wsc0"
            "bV1hefsSXmsYZoR5x7gX7YQyggwS0vl8cseSrkOs0mWxLopAz3C6s=",
    "data_ver": 34,
    "ios_arm64_flag": 1,
    "uuid": "d492dd329a0cd0624df8ced1c741202a"
}
# post_data = urllib.urlencode(data_json)   # 将post消息化成可以让服务器编码的方式
# post_data = str(data_json)   # 将post消息化成可以让服务器编码的方式
data_string = simplejson.dumps(data_json)

post_header = {
    "User-Agent": "WisdomTree/6.0.1 (iPhone; iOS 10.3.1; Scale/2.00)",
    # "Content-Length": str(len(data_string)),
    "Content-Type": "application/json",
    "Accept-Language": "zh-Hans-CN;q=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*"
}

# checkin
# req = urllib2.Request(m_host, data_string, post_header)
# response_stream = urllib2.urlopen(req)
# res = response_stream.read()
# print(res)

params = json.dumps(data_json)
print params
f = urllib.urlopen(m_host, params, post_header)
rsp = f.read()
print(rsp)




