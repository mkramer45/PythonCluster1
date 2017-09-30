import os

print(os.getcwd())  # display current working directory


os.chdir('/Users/mkramer/Desktop')  # change directory
# os.mkdir('OSdemo_Python/Sub-dir-1')     # similar to makedirs, however we cannot create a subdir within, only a folder
os.makedirs('OSdemo_Python/Sub-dir-1')  # makedirs is useful if you want to make folder & a subdirectory within

print(os.getcwd())



