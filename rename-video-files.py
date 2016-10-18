import shutil, os, time, datetime, re
from PIL import Image

os.chdir('C:\\Users\\Laura\\Pictures\\from phone')

fileNamePattern = re.compile(r'.*\.mp4')
absWorkingDir = os.path.abspath('.')

for file in os.listdir('.'):

    searchResult = fileNamePattern.search(file)

    if searchResult != None:

        creationDate = datetime.datetime.strptime(time.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y").strftime("%Y-%m-%d %H.%M.%S")

        originalFileName = os.path.join(absWorkingDir, file)
        newFileName = os.path.join(absWorkingDir, creationDate + ".mp4")

        print("Old file name: " + originalFileName)
        print("New file name: " + newFileName)

        # Uncomment after testing
        # shutil.move(originalFileName, newFileName)

    print()