import os

os.chdir('/Users/mkramer/Desktop/PythonFun/Planets')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)  # we are using the python library keyword splitext to split the filename from it's extension ... useful builtin function of python

    f_planetName, f_num, = file_name.split('-')  # now dealing with only our filename, which format follows 'mars-3' .. we are splitting these by delimiter of - into their respective variables

    new_name = '{}-{}{}'.format(f_num, f_planetName, file_ext)  # this is where we are creating our new file name ... which will look like 3-mars.txt

    os.rename(f, new_name)      # here is our execute statement where we are referencing our OS environment, using the rename builtin python KW rename(old filename, new filename)






