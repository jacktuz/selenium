'''
import unittest,os
case_path = os.path.join(os.getcwd(), "../case")


discover = unittest.defaultTestLoader.discover(case_path,pattern='*test')
suite = unittest.TestSuite()
case_suite = suite.addTest(discover)
runner = unittest.TextTestRunner
runner.case_suite

简单的只多条一起执行
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="*test.py")
    print(discover)
    return discover

if __name__ =="__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())
'''

#可生成报告的
import HTMLTestRunner
import unittest,os,time
import xlrd
from suite.kk import kkk

case_path = os.path.join(os.getcwd(), "../case")
def createsuite():
    testunite=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_path,pattern='*test.py',top_level_dir=None)
    print(discover)
    for test_suite in discover:                          #遍历所有的列表中元素（字典）
        for test_case in test_suite:                     #遍历所有的字典中元素（用例）
            testunite.addTests(test_case)
            print(testunite)

    now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    #filename="C:\\Users\\Administrator\\Desktop\\工作\\学习资源\\自动化测试\\test2\\report\\"+now+"_result.html"   #绝对路劲
    filename=os.path.join(os.getcwd(), "../report/")+now+"_result.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'功能测试报告',description=u'用例执行情况：')

    runner.run(testunite)

#关闭文件流，不关的话生成的报告是空的
    fp.close()

if __name__ == '__main__':
    createsuite()
    kkk()



