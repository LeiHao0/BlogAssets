# py /Users/lei/Movies/tmp/shrink.py namePrefix

import os
import subprocess
import sys

path =  os.path.dirname(__file__) + "./new"
namePrefix=sys.argv[1]

os.chdir(path)
# subprocess.run(["mkdir", "-p", "to"])

convertList = []
files = sorted(os.listdir("./"))
i = 0
for file in files:
    if file.endswith('.jpeg'):
        filename = os.path.splitext(file)[0]
        newFilename = filename
        
        if namePrefix:
            newFilename = namePrefix + "-" + str(i).zfill(2)
            i += 1

        convertList.append(f"convert -resize x1080 -strip -quality 80% \"{file}\" \"../{newFilename}.jpg\"")

from functools import partial
from multiprocessing.dummy import Pool
from subprocess import call

pool = Pool(10)
for i, returncode in enumerate(pool.imap(partial(call, shell=True), convertList)):
    if returncode != 0:
       print("%d command failed: %d" % (i, returncode))
