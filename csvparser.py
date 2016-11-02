import csv
with open('greenhouse.csv', 'rb') as f:
    r = csv.DictReader(f, delimiter=',', skipinitialspace=True)
    for row in r:
    	print "['"  +row['Country Code'] + "'," + row['2012'] + "],"