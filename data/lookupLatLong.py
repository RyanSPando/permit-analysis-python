import geocoder
import csv

csv.register_dialect(
    'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL)

data = []
addresses = [
    '852 S Williams St',
    '2725 N Elizabeth St',
    '2721 N Elizabeth St',
    '1605 S FILLMORE ST',
    '17870 E 44th Pl',
    '4450 N Truckee St',
    '4858 N Dunkirk St',
    '18591 E 50th Pl	',
    '5044 N Andes St	',
    '18501 E 50th Pl	',
    '4201 N QUIVAS ST',
    '3064 S ASH ST	',
    '5498 N Xanthia Ct',
    '5472 N Xanthia Ct',
    '4100 N Albion St ',
    '4474 N Truckee St',
    '4498 N Truckee St',
    '4458 N Truckee St',
    '4808 N Dunkirk St',
    '18171 E 47th Dr	',
    '18571 E 50th Pl	',
    '5048 N Andes St	',
    '5040 N Andes St'	,
    '4985 N Tamarac St',
    '3232 W 30th Ave',
]

for address in addresses:
    data.append(geocoder.google(address + ' Denver, CO').latlng)

with open('mydata.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='mydialect')
    for row in data:
        thedatawriter.writerow(row)
