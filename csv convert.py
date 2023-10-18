import csv
def every5th():
    count = 0
    with open('firestats.csv') as infile:
        with open('firestats-edit.csv', 'w') as outfile:
            rows = []
            rows += infile.readline()
            for row in infile.readlines():
                count += 1
                if count % 5 == 1:
                    rows += row
            outfile.writelines(rows)
def hrstomins():
    with open("firestats-edit.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        title = next(reader)
        lines = []
        for line in reader:
            line[2] = str((float(line[2]) * 86400) / 60)
            line[3] = str((float(line[3]) * 86400) / 60)
            line[4] = str((float(line[4]) * 86400) / 60)
            line[5] = str((float(line[5]) * 86400) / 60)
            lines.append(line)
    with open("firestats-edit1.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(title)
        writer.writerows(lines)
hrstomins()
