# !/usr/bin/env python
# coding = utf-8
import requests
import collections

SIGN_IN_URL = "https://pro.zhihuishu.bbtree.com/service/v2/user/sigin_in"
HEADER = {
    "User-Agent": "WisdomTree/6.0.1 (iPhone; iOS 10.3.1; Scale/2.00)",
    "Content-Type": "application/json",
    "Accept-Language": "zh-Hans-CN;q=1",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*"
}

if __name__ == "__main__":
    dict_user_info = collections.OrderedDict()
    dict_user_info['yjw'] = "gaYP/g3PUh5xMy432Y3LiDasGu2fzfIyuoD1GTk+SzWhgkKJ1LdLWjnZUHRLt/b+FI8iBDY9n+dLu7f6ojvfJ//2Omry/n/0OuLgmfYzoOb0BitUFHsI18Zl5bRxu4QRJ2zx42MI6d3+TYdvwRg+8lMfmdoXCa1M3XfUjRKGD3Eq7KYdublbyxH90q+EhXoiaOGC/SGv3Hn46hV7BzR2Xa4LQKFxWD87gr+5LoDpopvaNTYM3jK3iGdSRA3Qw5wo5eq6HevAY5UZCjyxHytsvVgBLgvlkFk9tp8BsPh6KQOuinkcnN00KTWDBEeSxoBNtUOMXz5pz5SLq5nGYgpj7JCOanxvQjbD1KTDIjoxHDtj5adHVgAxdITMoVI0HDZAAqd5cmvGt81ca+9LP+7fJ0IVsv3T5FafOtNOWJAhfIkEfzCbqw0WHCrjad/yxkAyz99aVuYTj6SJ8OtsHNf5y6/oxpuCX6R7BUwE4jnPz+TS+GOHvWzZmCJSn3IgVl0l"

    for k in dict_user_info:
        print k
        data_json = {
            "data": dict_user_info[k],
            "data_ver": 35,
            "ios_arm64_flag": 1,
            "uuid": "d492dd329a0cd0624df8ced1c741202a"
        }
        r = requests.post(SIGN_IN_URL, json=data_json, headers=HEADER, verify=False)
        print r.status_code






