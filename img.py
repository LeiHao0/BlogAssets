# py /Users/lei/Movies/tmp/shrink.py namePrefix

from subprocess import call
from multiprocessing.dummy import Pool
from functools import partial
import os
import subprocess
import sys

path = os.path.dirname(__file__) + "/img"
namePrefix = sys.argv[1]

try:
    ext= '.' + sys.argv[2]
except IndexError:
     ext= '.webp'
   

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
            newFilename = namePrefix + "-" + str(i).zfill(2) + ext
            i += 1
            
        convertList.append(f"magick \"{file}\" -resize x1080 -quality 50 -strip  \"{newFilename}\"")
        print(f"![](https://raw.githubusercontent.com/LeiHao0/BlogAssets/assets/{newFilename})")

pool = Pool(6)
for i, returncode in enumerate(pool.imap(partial(call, shell=True), convertList)):
    if returncode != 0:
        print("%d command failed: %d" % (i, returncode))
