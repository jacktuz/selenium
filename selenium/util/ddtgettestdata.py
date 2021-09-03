#本函数作用--1、创建含有多个字典的列表

#来源链接   https://zhuanlan.zhihu.com/p/109636684
#    ddt模块    +     xlrd模块     =    实现数据驱动测试



#操作步骤：
# 1、创建含有多个字典的列表       --xlrd    可对按照固定格式的.xlsx文件转化为【{}，{}，{}...{}】含有多个字典的列表格式
# 2、使用@ddt注解测试类
# 3、创建一个方法把数据取出来
# 4、使用@data注解单元测试用例

import xlrd
class ExcelUtil():
    def __init__(self,path,sheetname = "Sheet1"):
        self.data = xlrd.open_workbook(path)
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # print(self.keys)
        # 获取总行数
        self.rowNum = self.table.nrows
        # print(self.rowNum)
        # 获取总列数
        self.colNum = self.table.ncols
        # print(self.colNum)

    def read_Excel(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.rowNum-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)     #j取1，第二行的值
                # print(values)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]       #集合s，包含键值对   self.keys[x] : values[x]
                r.append(s)
                j+=1
            return r


