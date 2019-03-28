# https://pbpython.com/pathlib-intro.html
import os
from pathlib import Path
# 1.1 way1 by using os
in_file = os.path.join(os.getcwd(), "in/input.xlsx")
out_file = os.path.join(os.getcwd(), "out/output.xlsx")
print(in_file, out_file)
print(type(in_file))

# 1.2 way2 by using pathlib
in_file_1 = Path.cwd() / "in" / "input.xlsx"
out_file_1 = Path.cwd() / "out" / "output.xlsx"
print(in_file_1, out_file_1)
print(type(in_file_1))

in_file_2 = Path.cwd().joinpath("in").joinpath("input.xlsx")
out_file_2 = Path.cwd().joinpath("out").joinpath("output.xlsx")
print(in_file_2, out_file_2)

parts = ["in", "input.xlsx"]
in_file_3 = Path.cwd().joinpath(*parts)
print(in_file_3)

dir_to_scan = "/Users/mwang/Desktop/Work_Related"
p = Path(dir_to_scan)
print(p.is_dir())
print(p.is_file())
print(p.parts)
print(p.absolute())
print(p.anchor)
print(p.as_uri())
print(p.parent)

# folders or files
folders = []
files = []
for entry in os.scandir(p):
    if entry.is_dir():
        folders.append(entry)
    elif entry.is_file():
        files.append(entry)
print(folders)
print(files)

# list all folders and files, even if the hidden folders and files
for dirName, subdirList, fileList in os.walk(p):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)

# list all files in p path
for i in p.glob('*.*'):
    print(i.name)
# rglob: automatically recurse through the subdirectorie
print(list(p.rglob('*.csv')))
print(list(p.rglob('*.[!xlsx]*')))