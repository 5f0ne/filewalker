import os

class Search():
    def __init__(self, fileTypes) -> None:
        self.__fileTypes = fileTypes
        self.__files = []
        self.__init()

    def identifyFiles(self, _path):
        pathes = []
        
        if(_path != ""):
            pathes.append(_path)
        else:
            pathes = os.listdrives()

        for path in pathes:
            for dirPath, dirNames, fileNames in os.walk(path,topdown=True):
                for fileName in fileNames:
                    for fileType in self.__fileTypes:
                        if fileName.endswith("." + fileType):
                            filePath = os.path.join(dirPath, fileName)
                            for f in self.__files:
                                if(f["type"] == fileType):
                                    f["count"] = f["count"] + 1
                                    f["paths"].append(filePath)
        return self.__files
    
    def __init(self):
        for type in self.__fileTypes:
            self.__files.append({ "type": type, "count": 0, "paths": [] })