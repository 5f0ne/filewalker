import sys
import json
import argparse

from filewalker.Controller import Controller

from filewalker.args.Args import Args

from filewalker.types.FileType import FileType
from filewalker.search.Search import Search


def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    Args.addArguments(parser)
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
