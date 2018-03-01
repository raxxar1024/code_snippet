# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time



class XiaoMi():
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = 'http://item.mi.com/'
        self.verificationErrors = []
        self.accept_next_alert = True

    def login(self):
        """
        用户登陆
        """
        self.driver = webdriver.Chrome()
        self.driver.get("http://item.mi.com/product/10000041.html")
        self.driver.find_element_by_xpath(".//*[@id='J_userInfo']/a[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='username']").clear()
        self.driver.find_element_by_xpath(".//*[@id='username']").send_keys('18627012250')
        self.driver.find_element_by_xpath(".//*[@id='pwd']").clear()
        self.driver.find_element_by_xpath(".//*[@id='pwd']").send_keys('Thierry2')
        self.driver.find_element_by_id('login-button').click()
        # assertEqual(u'登陆失败', u'198154593', driver.find_element_by_xpath(".//*[@id='J_userInfo']/span[1]/a/span").span)

    def get_xiaomi6(self):
        '''
        设置9：59：55开始浏览器模拟用户行为不停的点击加入购物车
        '''
        def getSysTime():
            sys_time = time.time()
            return sys_time

        def set_stamp():
            set_time = '2017-05-12 09:59:55'   #设置抢购时间，最好提前几秒
            # 将其转换为时间数组
            timeArray = time.strptime(set_time, '%Y-%m-%d %H:%M:%S')
            # 转换为时间戳
            timeStamp = int(time.mktime(timeArray))
            return timeStamp

        # if getSysTime() >= set_stamp():
        time.sleep(1)
        while True:
            try:
                buybtn = self.driver.find_element_by_class_name('btn btn-primary btn-biglarge J_proBuyBtn add')
                buybtn.click()
                break
            except:
                try:
                    self.driver.refresh()
                except:
                    pass
                time.sleep(1)
        print "get it"


if __name__ == '__main__':
    # unittest.main()
    xiaomi = XiaoMi()
    xiaomi.setUp()
    xiaomi.login()
    xiaomi.get_xiaomi6()
