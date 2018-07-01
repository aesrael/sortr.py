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


def sort(file):
    if mimetypes.guess_extension(file) == ('application/pdf', None):
        rename(file)


# get all files in the downloads directory
for root, dirs, files in walk(downloadsDir):
    # loop through all the files
    for file in files:
        path = join(root, file)
        filePath = path
        # check if it is a file
        if(isfile(filePath)):
            print mimetypes.guess_type(filePath)
            sort(filePath)
