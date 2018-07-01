from itertools import chain
from os import listdir, walk
from os.path import expanduser, isfile, join

# import the python magic module using pip install python-magic
import magic

mime = magic.Magic(mime=True)
# get home dir
homeDir = expanduser("~")

# directories
dirs = ['Downloads', 'Music', 'Desktop', 'Videos', 'Pictures', 'Documents']

downloadsDir = '%s/Downloads/test' % (homeDir)

# get all files in the downloads directory
for root, dirs, files in walk(downloadsDir):
    # loop through all the files
    for file in files:
        # print(file)
        file = '%s/%s' % (downloadsDir, file)
        if(isfile(file)):
            print(file)
            mime.from_file(file)

# sort function


# def sort(fileType, directory):
