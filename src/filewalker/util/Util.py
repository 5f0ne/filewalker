from filewalker.types.FileType import FileType

class Util():
    def createFileList(t):
        return t.split(',')
    
    def getUniqueFileList(isOverride, files):
        uniqueTypes = []
        if(isOverride == True and len(files) > 0):
            uniqueTypes = files
        elif(isOverride == True and len(files) == 0):
            print("Override flag will be ignored because no other file types are provided!")
            uniqueTypes = FileType.getFileTypes([])
        else:
            uniqueTypes = FileType.getFileTypes(files)
        return uniqueTypes