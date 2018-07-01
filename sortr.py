from itertools import chain
from os import listdir, walk, rename
from os.path import expanduser, isfile, join
import mimetypes

mimetypes.init()

# get home dir
homeDir = expanduser("~")

downloadsDir = '%s/Downloads/test' % (homeDir)

# folders to sort to
music = '%s/Music' % (homeDir)
video = '%s/Video' % (homeDir)
pictures = '%s/Pictures' % (homeDir)
documents = '%s/Documents' % (homeDir)

def sort(exts, dst):
    # get all files in the downloads directory
    for root, dirs, files in walk(downloadsDir):
        # loop through all the files
        for file in files:
            path = join(root, file)
            filePath = path
            # check if it is a file
            if(isfile(filePath)):
                for ext in exts:
                    if filePath.find(ext) > -1:
                        rename(filePath, dst)
                        print('%s found' % (file))
                        # print(filePath,dst)


# sort mp3 files
sort(['mp3', 'ogg', 'wav'], music)
# sort video files
sort(['mp4', 'avi', 'flv', 'vob', 'mpg', 'mpeg'], video)
# sort books
sort(['pdf', 'epub'], documents)
# sort zip, gzip and rar files
sort(['zip', 'gzip', 'rar'], documents)
# sort apps
sort(['dmg', 'exe'], documents)
# sort pictures
sort(['png', 'jpeg', 'jpg'], pictures)
# sort documents
sort(['doc', 'ppt'], documents)