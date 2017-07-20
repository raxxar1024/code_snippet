# !/usr/bin/env python
# coding=utf-8
import urllib
import json
import time
import collections

check_in_url = "https://pro.zhihuishu.bbtree.com/service/v2/user/sigin_in"
dict_user_info = collections.OrderedDict()
dict_user_info['yjw'] = "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
"WhgkKJ1LdLWjnZUHRLt/b+FI8iBDY9n+dLu7f6ojvfJ"
"//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeSHfaMyS2VSY5r++XUuVWQkq7KYdublbyxH"
"90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo"
"5eq6HevAY5UZCjyxHytsvWVhD5Eb252uUuoVKb0CoSL"
"j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl8cseSrkOs0mWxLopAz3C6s="
dict_user_info['qhd'] = "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
"U69EeQWvU/4aCQt6382iJ2amnoQbiYgVTQp7oIEQmmd"
"//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeSHfaMyS2VSY5r++XUuVWQkq7KYdublbyxH"
"90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo"
"5eq6HevAY5UZCjyxHytsvbmGMNLVnu4o8bG3RwIgjKX"
"j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl8cseSrkOs0mWxLopAz3C6s="
dict_user_info['yaj'] = "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
"Vo/ZOicJj0a7RE4tN/lcxX4Nr4PNf3qIjLGWOP5zIjG"
"//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeTw39fQzvk45kKVUZi6tDEQq7KYdublbyxH"
"90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo"
"lrM5CoMKQQA266PQH0ArYXoxjQT09l6ADT0pjFEnpif"
"j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl4+bCQpKlp+XwjAfi3duOY4="
dict_user_info['qp'] = "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
"Wxv3olzYBWBIdAeAPikfQRTmENCOAeAthgNBvDlc4PU"
"//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeTw39fQzvk45kKVUZi6tDEQq7KYdublbyxH"
"90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo"
"KKDtIJafKQjHj8fAZ9LLucasLSfnrdbxunuS6uv/1+v"
"j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl4+bCQpKlp+XwjAfi3duOY4="
dict_user_info['zqr'] = "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
"W7R6Ba7c4k8d5KYXDrJrVXtUH/FGnQhT7Civ/iPKWS2"
"v/2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeTw39fQzvk45kKVUZi6tDEQq7KYdublbyxH"
"90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo"
"u/a4Axf5sphf64MAvXbm0+1K8t03miuxq0X+puMX5oj"
"j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl4+bCQpKlp+XwjAfi3duOY4="
dict_user_info['zyz'] = 'gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz'
'WgESDAE4A0w3P8lPlgkNUIi4T+qWsyVW064ujXW0UXN'
'v/2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeTw39fQzvk45kKVUZi6tDEQq7KYdublbyxH'
'90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo'
'5eq6HevAY5UZCjyxHytsvXRLvgeuvVzP8yJ8yW5Y6JPj'
'/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl4+bCQpKlp+XwjAfi3duOY4='
dict_user_info['yj'] = "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz"
"VByKRl6mzQvy62XjJCP4qzFI8iBDY9n+dLu7f6ojvfJ"
"//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeTw39fQzvk45kKVUZi6tDEQq7KYdublbyxH"
"90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo"
"b/m33UWH46scwKGuP/ukEdn0TNpTC6TW5gIT06Dgex3"
"j/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl4+bCQpKlp+XwjAfi3duOY4="
dict_user_info['lys'] = 'gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+Sz'
'U+uZljbjkhLqkbOY9T4B7/waKBL7YwwHEkXXQWTccIi'
'v/2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QR1wjV2J0S2gkrYga9KO4TeTw39fQzvk45kKVUZi6tDEQq7KYdublbyxH'
'90q+EhXoiaOGC/SGv3Hn46hV7BzR2XVq+sGSbIljtoIJfhzPdtMPaNTYM3jK3iGdSRA3Qw5wo'
'b/m33UWH46scwKGuP/ukEfy/D22g+DotqcHptqFDsYLj'
'/sZi03wsc0bV1hefsSXmsYZoR5x7gX7YQyggwS0vl4+bCQpKlp+XwjAfi3duOY4='


def check_in(req_data):
    count = 0
    data_json = {
        "data": req_data,
        "data_ver": 39,
        "ios_arm64_flag": 1,
        "uuid": "d492dd329a0cd0624df8ced1c741202a"
    }

    post_header = {
        "User-Agent": "WisdomTree/6.4.2 (iPhone; iOS 10.3.2; Scale/2.00)",
        "Content-Type": "application/json",
        "Accept-Language": "zh-Hans-CN;q=1",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*"
    }

    params = json.dumps(data_json)
    print k
    print params
    while True:
        f = urllib.urlopen(check_in_url, params, post_header)
        rsp = f.read()
        print(rsp)
        if "HTTP Status 415" not in rsp:
            break
        time.sleep(3)
        if count > 5:
            break
        else:
            count += 1


if __name__ == "__main__":
    list_success = []
    for k, v in dict_user_info.items():
        check_in(v)
