# import csv
import csv
from math import sqrt

# open file in write mode
pythagTriples = open('pythag-triples.csv', 'w')

# create the csv writer
csvwriter = csv.writer(pythagTriples, delimiter = ",")

# write the array to the csv file
    # header
csvwriter.writerow(['Leg 1', 'Leg 2', 'Hypotenuse'])

    # generate the pythagrean triples array
for a in range(1, 11):
    for b in range(a, 11):
        c = sqrt(a**2 + b**2)
        csvwriter.writerow([a, b, c])


# close the csv file
pythagTriples.close()
