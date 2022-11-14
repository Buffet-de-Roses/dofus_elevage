import json
import csv

f = open('do.json')
c = open('do.csv', 'w')

writer = csv.writer(c)
data = json.load(f)

input_line = ['nom', 'efficacité', 'utilisation']

writer.writerow(input_line)
input_line.clear()

for i in data['items']:
    if ('effects' in i and len(i['effects']) >= 2):
        input_line.append(i['name'])
        input_line.append(i['effects'][0]['int_minimum'])
        input_line.append(i['effects'][2]['int_minimum'])
        writer.writerow(input_line)
        input_line.clear()
f.close()
