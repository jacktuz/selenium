import os,time,logging

class log_msg():
    def __init__(self):
        timedate = time.strftime("Y%-M%-D%-H%",time.localtime(time.time()))
        log_dir = os.path.dirname(os.getcwd()) + 'logco'
        log_name = log_dir + timedate + '.log'
    #读入磁盘
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)
    #创建一个handler，用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
    #定义Handler的输出格式
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
    #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return  self.logger



-----------尚未完善