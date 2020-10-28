import csv
import os

targets = os.listdir('MER Data')
dict = {}
final = {}
sorted = []

for dataset in targets:
    with open ('MER Data/'+dataset,newline = '') as File:
        reader = csv.reader(File)
        next(reader)
        for row in reader:
            dict[row[0]] = row[8]
        keylist = list(dict.keys())
        keylist.sort()
        for key in keylist:
            if '000' not in key:
                sorted.append(dict[key])
        final[dataset.replace(".csv","")] = sorted
        sorted = []
        dict = {}

with open ('Bounty Gains.csv', mode = 'w', newline = '') as file:
    csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, )
    for key,value in final.items():
        value.insert(0,key)
        csv_writer.writerow(value)




