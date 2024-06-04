import sys
import json
import argparse

from filewalker.Controller import Controller

from filewalker.util.Util import Util
from filewalker.types.FileType import FileType
from filewalker.search.Search import Search


def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, default="", help="Path which shall be searched. If no path is provided, all available drives will be searched")
    parser.add_argument("--files", "-f", type=Util.createFileList, default=[], help="Comma separated list of file type to be searched for: pdf,jpg,txt")
    parser.add_argument("--overrideDefaultFileTypes", "-o", action=argparse.BooleanOptionalAction, help="If true, the default file types will be overwritten.")
    args = parser.parse_args()


    # Create a unique list of file types to be searched
    if(args.overrideDefaultFileTypes == True and len(args.files) > 0):
        uniqueTypes = args.files
    elif(args.overrideDefaultFileTypes == True and len(args.files) == 0):
        print("Override flag will be ignored because no other file types are provided!")
        uniqueTypes = FileType.getFileTypes([])
    else:
        uniqueTypes = FileType.getFileTypes(args.files)


    c = Controller()
    c.printHeader(args.path, uniqueTypes)

    s = Search(uniqueTypes)
    files = s.identifyFiles(args.path)
    printable = json.dumps(files, indent=4)

    # Print findings
    print(printable)

    c.printExecutionTime()

if __name__ == "__main__":
    sys.exit(main())
