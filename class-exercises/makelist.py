# Create the file to store the list
listFile = open('list.txt', 'w')

# Write out a 10-item ordered list using user input
for listItem in range(1, 11):
    listFile.write("%d. %s\n" % (listItem, input("Enter item " + str(listItem) + ": ")))

# Close the file
listFile.close()
