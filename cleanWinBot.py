
from asyncio import exceptions


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
   