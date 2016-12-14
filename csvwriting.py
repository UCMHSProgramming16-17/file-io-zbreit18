# import the csv module
import csv

# open a csv file in write mode
csvfile = open('csv-test-file.csv', 'w')

# setup a csv writer
csvwriter = csv.writer(csvfile, delimiter = ',')

# write to the csv file
csvwriter.writerow(["Cool things", "Boring Things"])
csvwriter.writerow(["Pigs", "Cows"])
csvwriter.writerow(["Pig emojis", "Cow emojis"])

# close the file
csvfile.close()
