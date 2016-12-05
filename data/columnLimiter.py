import pandas
low_memory=False
io = pandas.read_csv('boulderData.csv',sep=",",usecols=['_id','OriginalCity','OriginalZip','AppliedDate','EstProjectCost','LAT','LON','Fee'])
io.to_csv('boulderDataLimited.csv', sep=',', encoding='utf-8', index=False)
