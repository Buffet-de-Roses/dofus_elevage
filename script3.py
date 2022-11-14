import csv, operator, sys

csv_file = open(sys.argv[1], 'r+')

reader = csv.reader(csv_file, delimiter=',')

sorted_array = []
for row in reader:
    if 'efficacité' in row[1]:
        continue
    sorted_array.append((row[0], int(row[1]), int(row[2])))

csv_file.close()

open(sys.argv[1], 'w').close()

csv_file = open(sys.argv[1], 'w')
writer = csv.writer(csv_file)

sorted_array.sort(key=lambda a:a[2], reverse=True)
writer.writerow(['name', 'efficacité', 'utilisation'])
for row in sorted_array:
    writer.writerow(row)


