#!/usr/bin/env python
#coding=utf-8
import cookielib
import simplejson
import urllib2
import urllib


m_host = "https://pro.zhihuishu.bbtree.com/service/v2/user/login_v5"

data_json = {
    "data": "Sf/LZAiec/D6yRc9ftk7hcTM7WAyvqYiAbTF028B6igLJ6eCw1TVqlEkCyp0gVLEPZOsYzIt1Yvz1HoTDx1zXIObYyDmVCTWRN/M1UZ7npfQR2Cl69PUs+NC4dXtjKnwdrqDDPpLTGFSq/+vTQeORXW5VFY1gqBsqATKOJW2dbC9rhzwC3xaQQhX5u3pC1IAh3rshxTiqFcSMjIvI18oQAhKRVJLIDJ+aYB7zg8DMExcfmFYBUQ3OiLANNu4Dsm51JdwwnZmylXu2hjMPaQxCAFBLwT+psk+OXd70w2f5JaCpV9FFht5j9fqqUOH93gA1wjV2J0S2gkrYga9KO4TeY8B1/073STFNrvAvAGnoLuba+4o6TyGpTx0gabrxpGlmylotv5bzZv24eIt0UMEBA==",
    "data_ver": 34,
    "ios_arm64_flag": 1,
    "uuid": "d492dd329a0cd0624df8ced1c741202a"
}
data_string = simplejson.dumps(data_json)

post_header = {
    "User-Agent": "WisdomTree/6.0.1 (iPhone; iOS 10.3.1; Scale/2.00)",
    "Content-Length": str(len(data_string)),
    "Content-Type": "application/json",
    "Accept-Language": "zh-Hans-CN;q=1",
    "Accept-Encoding": "gzip, deflate"
}

# login
post_data = urllib.urlencode(data_json)   # 将post消息化成可以让服务器编码的方式
opener = urllib2.build_opener()
req = urllib2.Request(m_host, post_data, post_header)
content = opener.open(req)
print content.read()

# checkin



