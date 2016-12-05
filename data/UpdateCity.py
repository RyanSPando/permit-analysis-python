import csv
from geolocation.main import GoogleMaps

def csv_reader(file_obj):
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))

#----------------------------------------------------------------------
google_maps = GoogleMaps(api_key='AIzaSyDd4dbNcsmcldfq6X8yzCfidMera_KTZDc')
io = pandas.read_csv('BoulderDataLimited.csv',sep=",",usecols=['_id','OriginalCity','OriginalZip','AppliedDate','EstProjectCost','LAT','LON'])
for i in range(0, 3):
    if io.iloc[i]['OriginalCity'] == '':
        location = google_maps.search(lat=io.iloc[i]['LAT'], lng=io.iloc[i]['LON']).first()
        io.iloc[i]['OriginalCity'] = location.city
        print(location)
