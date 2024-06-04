class FileType():
    defaultTypes = ["pdf", "doc", "docx", "ppt", "pptx", "xls", "xlsx", "png", "jpeg", "jpg", "gif", "txt"]

    def getFileTypes(files):
        return list(set(files + FileType.defaultTypes))