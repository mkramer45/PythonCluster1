

with open('test.txt', 'r') as rf:  # original file open & let's read from that file
    with open('test_copy.txt', 'w') as wf:  # here is our file that doesn't exist yet, which we will write to this file, making a copy of our original file
        for line in rf:  # for each line in our original file (readfile) ....
            wf.write(line)  # ... write that line to wf (our write file, which will serve as the copy of our orig)
