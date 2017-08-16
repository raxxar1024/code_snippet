# -*- coding:utf-8 -*-

from splinter.browser import Browser

HOST_NAME = "http://192.168.1.247:8000"


def enter_discussion(name, code, pwd):
    b = Browser()
    b.visit(HOST_NAME)

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
    b.visit(HOST_NAME + '/discuss-detail_25')


def reg(name, code, pwd):
    b = Browser()
    b.visit(HOST_NAME + "/reg")

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
    for i in xrange(25):
        # reg(u"测试00"+str(i+1), "1000"+str(i+1), "123456")
        enter_discussion(u"测试00" + str(i + 1), "1000" + str(i + 1), "123456")
