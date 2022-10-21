import requests
from get_hostUrl import getConfig
from log.logginfFile import logger

class API:


    def sendAPI(self,mode,way, **kwargs):
        api=getConfig().geturl()
        #拼接url地址
        path=api+way
        result=""
        if mode=="post":
            res = requests.post(path,data=None,**kwargs)
            result=res.json()
        elif mode=="get":
            res = requests.get(path, data=None)
            result = res.json()
        else:
            result="请求方式不正确"
        logger.info(result)
        return result



