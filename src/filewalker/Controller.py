import os
import time

from datetime import datetime

class Controller():
    def __init__(self) -> None:
        self.startTime = time.time()

    def printHeader(self, path, fileTypes):
        print("################################################################################")
        print("")
        print("filewalker by 5f0")
        print("Searches hard drives/given path for files specified by file extensions")
        print("")
        print("Current working directory: " + os.getcwd())
        print("")
        print("Datetime: " + datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print("")
        print(" Targeted path: " + path)
        print("Targeted files: " + str(fileTypes))
        print("")
        print("################################################################################")
        print("")

    def printExecutionTime(self):
        end = time.time()
        print("")
        print("################################################################################")
        print("")
        print("Execution Time: " + str(end-self.startTime)[0:8] + " sec")
        print("")