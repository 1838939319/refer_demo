import xlrd
from findFiles import findFile
import yaml
from ReadYaml import Yamls
"""读取excle文件中的信息，并将Excel文件中的信息以字典的方式写入yaml文件中"""
class getExlce:
    def openExcle(self):
        filePath=findFile().get_filePath("API.xlsx","params")
        workdata=xlrd.open_workbook(filePath)
        sh=workdata.sheet_names()
        for i in sh:
            apiFile=findFile().get_filePath("%s.yaml"%i,"params")
            data=workdata.sheet_by_name(i)
            Yamls().cleanYaml(apiFile)
            # 通过sheet表对excle表格中的数据进行获取，并通过URL：数据字典的形式返回
            for i in range(1,data.nrows):
                params={data.cell_value(i,2):dict(zip(data.row_values(0), data.row_values(i)))}
                # file=open(apiFile,"a",encoding="utf-8")
                Yamls().writeYaml(params,apiFile)#将模块下的接口信息写入yaml文件中





s=getExlce().openExcle()
