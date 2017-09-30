with open('dudes.jpeg', 'rb') as rf:  # rb for read mode means we are reading in binary mode
    with open('dude_copy.jpeg', 'wb') as wf:  # wb for write mode means we are writing in binary mode
        for line in rf:
            wf.writeline(line)

