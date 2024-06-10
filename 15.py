import csv
with open('File.csv',mode='r') as file1:
    reader = csv.reader(file1)
    for row in reader:
        print(row)