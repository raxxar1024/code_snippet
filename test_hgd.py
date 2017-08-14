# -*- coding:utf-8 -*-

from splinter.browser import Browser

if __name__ == '__main__':
    b = Browser()
    b.visit("http://192.168.1.131:8002")

    # login in
    b.fill('name', u'张三')
    b.fill('code', '123')
    b.fill('pwd', '1')
    b.find_by_name('submit').first.click()

    # choose
    b.choose('classroom_id', '2')
    b.choose('course_id', '2')
    b.find_by_name('submit').first.click()

    # enter discuss-detail
    b.visit('http://192.168.1.131:8002/discuss-detail_19')

    while True:
        import time
        time.sleep(5)
