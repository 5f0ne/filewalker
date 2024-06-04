# Description

Searches hard drives/given path for files specified by file extensions

# Installation

`pip install filewalker`

# Usage

**From command line:**

`python -m filewalker [-h] [--path PATH] [--files FILES] [--overrideDefaultFileTypes | --no-overrideDefaultFileTypes | -o]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path which shall be searched. If no path is provided, all available drives will be searched |
|--files | -f | String[] | [] | Comma separated list of file type to be searched for: pdf,jpg,txt |
|--overrideDefaultFileTypes | -o | Boolean | False | If true, the default file types will be overwritten. |

**Default File Types**:

`pdf, doc, docx, ppt, pptx, xls, xlsx, png, jpeg, jpg, gif, txt`


**Programmatically:**

```python
from filewalker.search.Search import Search

s = Search(["md", "txt"]) # Provide the file extension you are interested in
files = s.identifyFiles("path/to/dir")  # If no path is provided, all available 
                                        # hard disk will be searched
                                        # You can see the structure of the files 
                                        # dictionary in the example below.

# Print findings
printable = json.dumps(files, indent=4) 


```


# Example

`py -m filewalker -p path/to/dir -f md,txt -o`

Search for all `md` and `txt` files within the path `path/to/dir` and it's
subdirectories.

```
################################################################################

filewalker by 5f0
Search connected hard drives for given files

Current working directory: path/to/filewalker

Datetime: 01/01/1970 20:20:20

 Targeted path: path/to/dir
Targeted files: ['md', txt]

################################################################################

[
    {
        "type": "md",
        "count": 2,
        "paths": [
            "path/to/dir/LICENSE.md",
            "path/to/dir/config/README.md"
        ]
    },
    {
        "type": "txt",
        "count": 1,
        "paths": [
            "path/to/dir/config/other/options.txt"
        ]
    }
]

################################################################################

Execution Time: 0.016395 sec


```


# License

MIT