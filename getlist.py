#!/usr/bin/env python2

import os

def getlist():
    # folder path
    dir_path = r'./'

    # list to store files
    res = []
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    res1 = str(res)
    with open ('./files.txt','a+') as f:
        f.write(res1)
    #print(res)

path = str(os.path.isfile("./files.txt"))
if (path == "False"):
    getlist()

else:
    os.remove('./files.txt')
    getlist()