import logging
from common.findFiles import findFile
class LogFile:

    def __init__(self):
        self.logNmae="refer"
        self.fileName="refer.log"
        self.Level=logging.DEBUG
#定义file文件路径
    def creatFile(self):
        file=findFile().get_filePath(self.fileName,"logs")
        # print(file)
        return file

    def getLogger(self):

        logger=logging.getLogger(self.logNmae)#创建日志收集器
        logger.setLevel(self.Level)
        fmt=logging.Formatter("%(name)s-%(asctime)s-%(filename)s-%(message)s")
        if not logger.hasHandlers():
            sh=logging.StreamHandler()
            sh.setFormatter(fmt=fmt)
            logger.addHandler(sh)
            fh=logging.FileHandler(self.creatFile(),mode='a', encoding="utf-8")
            fh.setFormatter(fmt=fmt)
            logger.addHandler(fh)
        return logger
logger=LogFile().getLogger()

# if __name__ == '__main__':
#
#     logger.info("sssss")

