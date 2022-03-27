
from asyncio import exceptions
import json


def RemoveFileFrom(path):
    path_list = path.glob("*")

    dFiles=["Deleted Files"]
    for f in path_list:
        try:
            if f.is_file():
                f.unlink()
                dFiles.insert(0,f.name + "Removed")
                
        except:
                dFiles.insert(0,"Can't Remove "+f.name)


    # for res in enumerate (dFiles):
    #     print(res)
    return dFiles 


def getPathFromJson(jsonpath):

  with open(jsonpath, 'r') as f:
    settingData = f.read()
    #print(settingData)
    pathDict = json.loads(settingData)
    return pathDict
    

# def addPathToJson():
#     pathDict = {"pathName": "C:\Users\kaili\AppData\Local\Temp"}

#     with open('setting.txt', 'w') as json_file:
#         json.dump(pathDict, json_file)