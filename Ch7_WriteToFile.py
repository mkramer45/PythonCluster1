

with open('test2.txt', 'w') as f:  # by including in write mode 'w', you are over-writing a 'test2.txt' file if it exists
    f.write('Test')
    f.seek(0)
    f.write('R')  # R will over-write the 0th position of the character found in first write statment for 'Test'

