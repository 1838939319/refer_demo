
import findFiles
import yaml
class getConfig:
    # 获取yaml文件路径并打开文件获取文件信息值返回
    def __init__(self):
        self.fimename="application-global"

    def getMessage(self):
        try:
            path=findFiles.findFile().get_filePath(self.fimename,"config")#调用获取配置文件方法，取得对应配置文件路径
            with open(path,"rb") as file:
                msg = yaml.safe_load(file)#对得到的yaml文件信息进行编码
                # print(msg)
            return msg
        except Exception as e:
            print(e)

    # 得到yaml文件中的数据拼接成完整的初始化url路径
    def geturl(self):
        msg=getConfig().getMessage()#获取配置文件中的信息
        url="http://"+str(msg["HOST"])+":"+str(msg["HOST_PORT"])+str(msg["HOST_PATH"])#获取拼接的初始化http地址
        # print(url)
        return url
    def getVar(self,name):
        msg = getConfig().getMessage()  # 获取配置文件中的信息
        data=msg[name]
        return data


# s=getConfig()
# s2=s.geturl()
