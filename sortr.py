from itertools import chain
from os import walk, rename, path
from os.path import expanduser, isfile, join
from timeit import default_timer

start = default_timer()
# get home dir
homeDir = expanduser("~")

# input directory to sort prompt
dirInput = raw_input(
    'enter directory to sort eg downloads,desktop etc : ') or 'Downloads'

# sortDir, set dir to sort here, default dir is 'home/user/Downloads'
sortDir = '%s/%s' % (homeDir, dirInput.capitalize())

if (path.exists(sortDir) == True):
    print('sorting %s...' % (sortDir))
else:
    print('%s not a directory, set directory to sort' % (sortDir))

# folders to sort to
music = '%s/Music' % (homeDir)
videos = '%s/Videos' % (homeDir)
pictures = '%s/Pictures' % (homeDir)
documents = '%s/Documents' % (homeDir)


def sort(exts, dst):
    # get all files in the downloads directory
    for root, dirs, files in walk(sortDir):
        # loop through all the files
        for file in files:
            # create path to file
            path = join(root, file)
            filePath = path
            # check if it is a file
            if(isfile(filePath)):
                # loop through the extensions argument list
                for ext in exts:

                    # find filename with one of the extension type
                    if filePath.lower().endswith('.%s' % (ext)):
                        newFilePath = '%s/%s' % (dst, file)

                        # change dir of file(sort file)
                        rename(filePath, newFilePath)
                        print('%s found and sorted' % (file))
                    else:
                        continue
                    print('no more files to sort')



# sort music files
sort(['mp3', 'ogg', 'wav'], music)
# sort videos
sort(['mp4', 'avi', 'flv', 'vob', 'mpg', 'webm', 'mpeg'], videos)
# sort documents and utils
sort(['zip', 'gzip', 'rar', 'pdf', 'epub', 'dmg', 'exe', 'doc', 'ppt'], documents)
# sort pictures
sort(['png', 'jpeg', 'jpg'], pictures)

stop = default_timer()

print('time taken: %s secs.' % (stop-start))
