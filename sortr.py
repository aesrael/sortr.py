from itertools import chain
from os import listdir, walk, rename
from os.path import expanduser, isfile, join
import mimetypes

mimetypes.init()

# get home dir
homeDir = expanduser("~")

# directories
dirs = ['Downloads', 'Music', 'Desktop', 'Videos', 'Pictures', 'Documents']

downloadsDir = '%s/Downloads/test' % (homeDir)

# get all files in the downloads directory
for root, dirs, files in walk(downloadsDir):
    # loop through all the files
    for file in files:
        file = '%s/%s' % (downloadsDir, file)
        # check if it is a file
        if(isfile(file)):
            print(file)
            sort(file)


def sort(file, mime, dst):
    if mimetypes.guess_type(file) == ('application/pdf', None):
        rename(file, dst)
