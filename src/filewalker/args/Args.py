import argparse
from filewalker.util.Util import Util

class Args():
    def addArguments(parser):
        parser.add_argument("--path", "-p", type=str, default="", help="Path which shall be searched. If no path is provided, all available drives will be searched")
        parser.add_argument("--files", "-f", type=Util.createFileList, default=[], help="Comma separated list of file type to be searched for: pdf,jpg,txt")
        parser.add_argument("--overrideDefaultFileTypes", "-o", action=argparse.BooleanOptionalAction, help="If true, the default file types will be overwritten.")