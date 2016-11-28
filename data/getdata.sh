for i in 2015 2016
do
    for j in Jan Feb Mar April May June July August September October November December
    do
        curl -O -k https://www.denvergov.org/content/dam/denvergov/Portals/696/documents/PermitRecords/$i/$j-$i.xls
    done
done
