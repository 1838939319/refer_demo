import os
class findFile:

    def get_filePath(self,fileName,dir):
        path1 = dir
        path2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取当前文件的路径
        path3 = os.path.normpath(os.path.join(path2,path1,fileName))#规范路径的格式，对于不同环境下的路径做统一处理
        path4 = os.path.normpath(os.path.join(path2,path1))  #获取目录路径
        if not os.path.exists(path4):
            os.mkdir(path4)
        else:
            if not os.path.exists(path3):
                f = open(path3, "w")
                f.close()
                # print(path3)


        return path3

# d=findFile()
# s=d.get_filePath("s.log","commons")