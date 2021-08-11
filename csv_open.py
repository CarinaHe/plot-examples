import csv

with open("dmv.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(' , '.join(row))


# andere möglichkeit:
# fhand = open("dmv.csv")
# for x in fhand:
#     print(x)
