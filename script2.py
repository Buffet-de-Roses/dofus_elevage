import csv

mangeoire = open('csv/mangeoire.csv', 'w')
baffeur = open('csv/baffeur.csv', 'w')
foudroyeur = open('csv/foudroyeur.csv', 'w')
caresseur = open('csv/caresseur.csv', 'w')
dragofesse = open('csv/dragofesse.csv', 'w')
abreuvoir = open('csv/abreuvoir.csv', 'w')

writer = csv.writer(mangeoire)

with open('csv/do.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if 'Mangeoire' in row[0]:
            writer = csv.writer(mangeoire)
        if 'Abreuvoir' in row[0]:
            writer = csv.writer(abreuvoir)
        if 'Baffeur' in row[0]:
            writer = csv.writer(baffeur)
        if 'Foudroyeur' in row[0]:
            writer = csv.writer(foudroyeur)
        if 'Caresseur' in row[0]:
            writer = csv.writer(caresseur)
        if 'Dragofesse' in row[0]:
            writer = csv.writer(dragofesse)
        writer.writerow(row)

mangeoire.close()
abreuvoir.close()
baffeur.close()
foudroyeur.close()
caresseur.close()
dragofesse.close()