

with open('test.txt', 'r') as f:
    for line in f:      # using this for loop is useful when reading large files due to memory efficiency ... if doing read or readline all at once
                            # that makes it prone to running into a memory resource issue
        print(line, end = '')


