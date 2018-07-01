from itertools import chain
from os import listdir, walk
from os.path import expanduser, isfile, join

# get home dir
homeDir = expanduser("~")

# directories
dirs = ['Downloads', 'Music', 'Desktop', 'Videos', 'Pictures', 'Documents']

downloadsDir = '%s/Downloads/test' % (homeDir)

# get all files in the downloads directory
for root, dirs, files in walk(downloadsDir):
    #loop through all the files
    for file in files:
        if(isfile('%s/%s' % (downloadsDir, file))):
            print(file)
