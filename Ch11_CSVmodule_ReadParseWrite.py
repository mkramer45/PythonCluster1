import csv

with open('CommaSep.csv', 'r') as csv_file:  # open our CSV file, use 'r' to tell python to read it (instead of write)
    csv_reader = csv.reader(csv_file)  # variable csv_reader set to the csv.reader method ... pointed at our commasep csv file

    for line in csv_reader:  # for every line in our csv file ....
        print(line)  # print that shit

