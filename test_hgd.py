# -*- coding:utf-8 -*-

from splinter.browser import Browser


def enter_discussion(name, code, pwd):
    b = Browser()
    b.visit("http://192.168.1.131:8002")

    # login in
    b.fill('name', name)
    b.fill('code', code)
    b.fill('pwd', pwd)
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


def reg(name, code, pwd):
    b = Browser()
    b.visit("http://192.168.1.131:8002/reg")

    # reg
    b.fill('name', name)
    b.fill('code', code)
    b.fill('pwd', pwd)
    b.fill('organization', u"海工大")
    b.fill('position', u"管理系")
    b.select('degree', u"2")
    b.fill('title', u"学生")
    b.fill('college', u"海工大")
    b.fill('major', u"学生")
    b.find_by_name('submit').first.click()


if __name__ == '__main__':
    # enter_discussion(u'张三', '123', '1')
    for i in xrange(25):
        reg(u"测试00"+str(i+1), "1000"+str(i+1), "123456")
