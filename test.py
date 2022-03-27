from cleanWinBot import RemoveFileFrom,getPathFromJson
from pathlib import Path

pathDict = getPathFromJson('setting.json')

for index,jsnPath in enumerate(pathDict):
        removepath = Path(jsnPath['pathloc'])
        print(removepath)
        for res in enumerate(RemoveFileFrom(removepath)):
            print(res)