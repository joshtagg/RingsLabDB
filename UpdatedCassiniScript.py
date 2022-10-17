# Joshua Taggart, 10-16-22
# Purpose of this program: convert .sav files into sql formatted files
# New script to work with UVIS 1k and 10k .sav files

import scipy.io as sio
import os

#assign directory
directory = 'C:/Users/joshu/Desktop/FixedRawData/testFolder'

'''
(12 total arrays)
arrays within 10km and 1km binned data:
    pdsdata.radius      -> name it: rad10km if 10km file    else, name it: rad1km
    pdsdata.dat         -> name it: dat10km if 10km file    else, name it: dat1km
    pdsdata.nbins       -> name it: nbin10km if 10km file   else, name it: nbin1km

'''
#mydata = sio.readsav(.sav)
#mydata.pdsdata.radius
#rad10km = mydata.pdsdata.radius

#iterate over files in directory
for filename in os.listdir(directory):
    # directory for one file
    curFileDirectory = os.path.join(directory, filename)
    curFile = filename
    #print(curFileDirectory)
    #print(curFile)

    # readsav for current .sav file
    mydata = sio.readsav(curFile)
    
    # find len of array (all arrays in .sav file are the same length)
    arrayLen = len(mydata.pdsdata.radius)

    # delete .sav extension from curFile
    deletedExtension = curFile.rsplit(".", 1)[0]

    #create new .sql file for curFile
    newFile = open(deletedExtension + ".sql", 'wt')

    # Printing to new .sql file (inserting table header)
    print("CREATE TABLE " + deletedExtension + "\n(\n\tradius int,\n\tdata int,\n\tet int,\n\tlon int,\n\tringoccphi int,\n);\n\n", file=newFile)