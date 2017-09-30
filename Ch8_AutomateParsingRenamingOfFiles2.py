import os

os.chdir('/Users/mkramer/Desktop/PythonFun/Planets')

for f in os.listdir():
    print(f)    # lets make sure the files we are expecting are in the directory
