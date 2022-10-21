import yaml
from findFiles import findFile


"""针对yaml文件的读、写、清空操作"""
class Yamls:

    #读取yaml中信息并以dict的形式返回
    def readYaml(self,file):
        filePath=findFile().get_filePath(file,"params")#定义yaml文件的路径
        with open(filePath,mode="r",encoding="utf-8") as f:
            dict=yaml.load(f,Loader=yaml.FullLoader)
        return dict

    #清除yanml中的信息
    def cleanYaml(self,file):
        filePath = findFile().get_filePath(file, "params")  # 定义yaml文件的路径
        with open(filePath,mode="w") as f:
            f.truncate()

    #将文件写入yaml文件
    def writeYaml(self,data,file):
        filePath = findFile().get_filePath(file, "params")
        with open(filePath , mode="a", encoding="utf-8")as file:
            yaml.dump(data, file, encoding='utf-8',allow_unicode=True)









s=Yamls()
data={"/api/oneMap/getEventRAT":{"data":"测试","header":1}}
s1=s.writeYaml(data,"api.yaml")