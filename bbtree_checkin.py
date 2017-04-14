# !/usr/bin/env python
# coding=utf-8
import cookielib
import simplejson
import urllib2
import urllib
import json


checkin_host = "https://pro.zhihuishu.bbtree.com/service/v2/user/sigin_in"


dict_user_info = {
    'yjw':
        "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
        "WhgkKJ1LdLWjnZUHRLt/b+FI8iBDY9n+dLu7f6ojvfJ"
        "//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeSHfaMyS2VSY5r++XUuVWQkq7KYdublbyxH"
        "90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo5eq6HevAY5UZCjyxHytsv"
        "WVhD5Eb252uUuoVKb0CoSL"
        "j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl8cseSrkOs0mWxLopAz3C6s=",
    'qhd':
        "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
        "U69EeQWvU/4aCQt6382iJ2amnoQbiYgVTQp7oIEQmmd"
        "//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeSHfaMyS2VSY5r++XUuVWQkq7KYdublbyxH"
        "90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo5eq6HevAY5UZCjyxHytsv"
        "bmGMNLVnu4o8bG3RwIgjKX"
        "j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl8cseSrkOs0mWxLopAz3C6s="
}


for k, v in dict_user_info.items():
    data_json = {
        "data": v,
        "data_ver": 34,
        "ios_arm64_flag": 1,
        "uuid": "d492dd329a0cd0624df8ced1c741202a"
    }

    data_string = simplejson.dumps(data_json)

    post_header = {
        "User-Agent": "WisdomTree/6.0.1 (iPhone; iOS 10.3.1; Scale/2.00)",
        "Content-Type": "application/json",
        "Accept-Language": "zh-Hans-CN;q=1",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*"
    }

    params = json.dumps(data_json)
    print params
    f = urllib.urlopen(checkin_host, params, post_header)
    rsp = f.read()
    print(rsp)




