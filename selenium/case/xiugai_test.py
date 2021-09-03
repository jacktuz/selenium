# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time
import os
from ddt import ddt,data
from util.ddtgettestdata import ExcelUtil

@ddt
class MmaChange(unittest.TestCase):
    filepath = os.path.join(os.getcwd(), "../data/case.xlsx")
    #使用ExcelUtil创建对象datas
    datas = ExcelUtil(filepath)
    datadict = datas.read_Excel()
    print(datadict)



    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.set_window_size(1080,800)
        cls.driver.implicitly_wait(1)
        cls.driver.get('https://192.168.3.27:8443/index.html/#/login')

#login-跳过验证码    css、class
    @data(*datadict)
    def test_login(self,k):
        self.driver.find_element_by_xpath('//*[@id="details-button"]').click()
        self.driver.find_element_by_link_text("继续前往192.168.3.27（不安全）").click()

        self.driver.find_element_by_css_selector("[placeholder='用户名']").send_keys(k["username"])
        self.driver.find_element_by_css_selector("[placeholder='密码']").send_keys(k['password'])
        #self.driver.find_element_by_css_selector("[placeholder='验证码']").send_keys("Qwer%1234")#         等待输入验证码
        time.sleep(15)
        self.driver.find_element_by_class_name("ivu-btn-default").click()

# 系统设置-密码修改
#     输入密码、新密码、重复密码
    @data(*datadict)
    def test_loginmimaxiugai(self,d):
        self.driver.find_element_by_css_selector('#headBar > div.edr-header.clearfix > div.userinfo > div.action-wrap > div:nth-child(1) > a > div > div > div > i').click()
        self.driver.find_element_by_class_name("icons-pwd").click()
        self.driver.find_element_by_link_text("登录密码").click()
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(2) > div.m > div > input').send_keys(d["password"])
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(3) > div.m > div.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type > input').send_keys(d["newpassword"])
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(4) > div.m > div > input').send_keys(d["newpassword"])
        self.driver.find_element_by_css_selector(".btn-confirm").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)





#敏感操作密码设置--未设置敏感密码
    # def test_mingganchaozuomima(self):
    #     self.driver.find_element_by_link_text("敏感操作密码").click()
    #     time.sleep(case)
    #     self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(2) > div.m > div > input").send_keys("Qwer%1234")
    #     self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(3) > div.m > div.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type > input").send_keys("qwer@1234")
    #     self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(4) > div.m > div > input").send_keys("qwer@1234")
    #     self.driver.find_element_by_css_selector(".btn-confirm").click()

#敏感操作密码设置--设置了敏感密码
    # def test_mingganmima(self):
    #     self.driver.find_element_by_link_text("敏感操作密码").click()
    #     self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(2) > div.m > div > input").send_keys("1234%Qwer")
    #     self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(3) > div.m > div.ivu-input-wrapper.ivu-input-wrapper-default.ivu-input-type > input").send_keys("1234%QwerT")
    #     self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.content > div > div > div.form-wrapper > div:nth-child(4) > div.m > div > input").send_keys("1234%QwerT")
    #     self.driver.find_element_by_css_selector(".btn-confirm").click()


