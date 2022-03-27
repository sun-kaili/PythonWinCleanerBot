

def RemoveFileFrom(path):
    path_list = path.glob("*")

    for f in path_list:
        try:
            if f.is_file():
                f.unlink()
                return "Removed"
                
        except:
            return "Can't Remove "

