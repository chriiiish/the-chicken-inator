import re

# Read in file
inFile = open('test.txt', 'r')
outFile = open('test.chicken', 'w')

# Regex \w+ with 'chicken'
for line in inFile:
    partialChickenLine = re.sub("[A-Z][\w']*", 'Chicken', line)
    completeChickenLine = re.sub("\s[a-z0-9']+", ' chicken', partialChickenLine)
    outFile.write(completeChickenLine)

# Close output file
outFile.close()

