# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest
import time
import os
from ddt import ddt,data
from util.ddtgettestdata import ExcelUtil

@ddt
class MimaChange(unittest.TestCase):
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

#login-手动输入验证码    css、class
    @data(*datadict)
    def test_login(self,data):
        self.driver.find_element_by_xpath('//*[@id="details-button"]').click()
        self.driver.find_element_by_link_text("继续前往192.168.3.27（不安全）").click()

        self.driver.find_element_by_css_selector("[placeholder='用户名']").send_keys(data["username"])
        self.driver.find_element_by_css_selector("[placeholder='密码']").send_keys(data["password"])
        #self.driver.find_element_by_css_selector("[placeholder='验证码']").send_keys("Qwer%1234")#     等待输入验证码
        time.sleep(8)
        self.driver.find_element_by_class_name("ivu-btn-default").click()

        #断言过程
        submit = self.driver.find_element_by_css_selector("#headBar > div.edr-header.clearfix > div.userinfo > div.welcome > span")    #定位元素
        text = submit.text		#获取元素文本信息
        print(text)	#打印元素文本
        if text=="你好，tuzi":
            print("if判断")
        self.assertEqual(text,"你好，tuzi",msg="断言失败时打印的信息")



#生成报表
    def test_search(self):
        self.driver.find_element_by_css_selector('#headBar > div.edr-header.clearfix > div.edr-menu > ul > li.navbar-item.report > a > div > div > div > i').click()
        self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.report-entrance-content.sticky-footer-wrapper > div.sticky-content > div > a:nth-child(3) > div").click()
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-sider > div:nth-child(1) > div.comp-content.show > div.checkbox-row > label').click()
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-main-index > div.report-main-fixed-header > div > div.operate-item.time > div.operate-content > span:nth-child(3)').click()
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-main-index > div.report-main-fixed-header > div > div.operate-item.group > div > div.sch-tag-wrap').click()
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-main-index > div.report-main-fixed-header > div > div.operate-item.group > div > div.edr-modal-hide-close.edr-modal-report-detail > div.allnet-detail-org-tree.ivu-tree > ul > li > label > span > input').click()
        self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-main-index > div.report-main-fixed-header > div > div.operate-item.group > div > div.edr-modal-hide-close.edr-modal-report-detail > div.edr-modal-footer > button.btn-confirm.ivu-btn.ivu-btn-primary').click()
        #元素定位相互覆盖  self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-main-index > div.report-main-fixed-header > div > button > span').click()
        element1 = self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-main-index > div.report-main-fixed-header > div > button > span')
        self.driver.execute_script("arguments[0].click();", element1)

#参数化测试用例

# #新增报表
#     def test_madd(self):
#         self.driver.find_element_by_css_selector('#headBar > div > div.edr-menu > ul > li.navbar-item.report > a > div > div > svg').click()
#         self.driver.find_element_by_css_selector("#app > div > div.page-content > div > div.report-entrance-content.sticky-footer-wrapper > div.sticky-content > div > a:nth-child(3) > div").click()
#         self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-sider > div:nth-child(1) > div.comp-content.show > div.checkbox-row > label').click()
#         self.driver.find_element_by_css_selector('#app > div > div.page-content > div > div.sticky-footer-wrapper > div.page-report-custom.sticky-content > div.layout-content > div.report-main-index > div.report-main-fixed-footer > button > span').click()
#
#         self.driver.find_element_by_css_selector('body > div:nth-child(20) > div.ivu-drawer-wrap > div > div > div > div > div.edr-drawer-body > div.content > div > div.edr-form-item > div > input').send_keys('addMB')
#
#         self.driver.find_element_by_css_selector('body > div:nth-child(20) > div.ivu-drawer-wrap > div > div > div > div > div.edr-drawer-body > div.body-inner-footer > button.btn-confirm.ivu-btn.ivu-btn-primary').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)