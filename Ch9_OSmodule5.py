import os
from datetime import datetime
os.chdir('/Users/mkramer/Desktop')  # change directory

file_path = os.path.join(os.environ.get('HOME'), 'newfile_test.txt')  # os.path.join takes our current path we're are at & efficiently writes a file out to it

print(file_path)



