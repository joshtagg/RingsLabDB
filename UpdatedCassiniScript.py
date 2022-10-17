# Joshua Taggart, 10-16-22
# Purpose of this program: convert .sav files into sql formatted files
# New script to work with UVIS 1k and 10k .sav files

import scipy.io as sio
import os

# assign directory
directory = 'C:/Users/joshu/Desktop/FixedRawData/testFolder'

'''
(18 total arrays?)
arrays within 10km and 1km binned data:
    pdsdata.radius      -> name it: rad10km if 10km file    else, name it: rad1km
    pdsdata.dat         -> name it: dat10km if 10km file    else, name it: dat1km
    pdsdata.nbins       -> name it: nbin10km if 10km file   else, name it: nbin1km
    et
    lon (longitude)
    tau
    taumax
    phi
    b_angle
    background
    dlos
    imaxrr
    imaxpts
    backrr
    backpts
    flag (note flag)
    source_product
    cims_product
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

    # readsav for current .sav file, sav file is now a dict
    mydata = sio.readsav(curFileDirectory)

    '''
    #TEST
    for key in mydata:
        #print("the key name is: " + key + "and its value is: " + mydata[key])
        print(mydata.items())
    '''

    radius = mydata.pdsdata.radius[0]
    dat = mydata.pdsdata.dat[0]
    nbins = mydata.pdsdata.nbins[0]
    et = mydata.pdsdata.et[0]
    lon = mydata.pdsdata.et[0]
    tau = mydata.pdsdata.tau[0]
    taumax = mydata.pdsdata.taumax[0]
    phi = mydata.pdsdata.phi[0]
    b_angle = mydata.pdsdata.b_angle #TEST - THIS ARRAY IS DIFFERENT(?) only one number in it
    background = mydata.pdsdata.background[0]
    dlos = mydata.pdsdata.dlos[0]
    imaxrr = mydata.pdsdata.imaxrr[0]
    backrr = mydata.pdsdata.backrr[0]
    backpts = mydata.pdsdata.backpts[0]
    flag = mydata.pdsdata.flag[0]
    source_product = mydata.pdsdata.source_product[0]
    cims_product = mydata.pdsdata.cims_product[0]

    # find len of array (all arrays in .sav file are the same length)
    arrayLen = len(radius)

    # delete .sav extension from curFile
    deletedExtension = curFile.rsplit(".", 1)[0]

    '''
    #TEST
    #b_angleLen = len(b_angle)
    #print("length of b_angleLen array: " + str(b_angleLen))
    #print(radius)

    print("length of radius array: " + str(len(radius)))
    print("length of dat array: " + str(len(dat)))
    print("length of nbins array: " + str(len(nbins)))
    print("length of et array: " + str(len(et)))
    print("length of lon array: " + str(len(lon)))
    print("length of tau array: " + str(len(tau)))
    print("length of taumax array: " + str(len(taumax)))
    print("length of phi array: " + str(len(phi)))
    print("length of background array: " + str(len(background)))
    print("length of dlos array: " + str(len(dlos)))
    print("length of imaxrr array: " + str(len(imaxrr)))
    print("length of backrr array: " + str(len(backrr)))
    print("length of backpts array: " + str(len(backpts)))
    print("length of flag array: " + str(len(flag)))
    print("length of source_product array: " + str(len(source_product)))
    print("length of cims_product array: " + str(len(cims_product)))

    #same length: radius, dat, nbins, et, lon, tau, taumax, phi, background, dlos, flag
    #length of 1: b_angle
    #unique length: imaxrr
    #same length: backrr, backpts
    #unique length: source_product
    #unique length: cims_product
    #TEST
    '''

    
    # create new .sql file for curFile
    newFile = open(deletedExtension + ".sql", 'wt')

    # Printing to new .sql file (inserting table header)
    print("CREATE TABLE " + deletedExtension + "\n(\n\tradius int,\n\tdat int,\n\tnbins int,\n\tet int,\n\tlon int, \n\ttau int, \n\ttaumax int, \n\tphi int, \n\tbackground int, \n\tdlos int, \n\timaxrr int, \n\tbackrr int, \n\tbackpts int, \n\tflag int, \n\tsource_product int, \n\tcims_product int,\n);\n\n", file=newFile)
    print("INSERT INTO " + deletedExtension + " (radius, dat, nbins, et, lon, tau, taumax, phi, background, dlos, imaxrr, backrr, backpts, flag, source_product, cims_product)\nVALUES\n", file=newFile)
    i=0
    while i < arrayLen:
        print('\t("' + str(radius[i]) + '", "' + str(dat[i]) + '", "' + str(nbins[i]) + '", "' + str(et[i]) + '", "' + str(lon[i]) + '", "' + str(tau[i]) + '", "' + str(taumax[i]) + '", "' + str(phi[i]) + '", "' + '", "' + str(background[i]) + '", "' + str(dlos[i]) + '", "' + str(imaxrr[i]) + '", "' + str(backrr[i]) + '", "' + str(backpts[i]) + '", "' + str(flag[i]) + '", "' + str(source_product[i]) + '", "' + str(cims_product[i]) + '"),', file=newFile)
        #if last variable, instead of ending print with ',' you must end print with ';'
        if i == arrayLen-1:
            print('\t("' + str(radius[i]) + '", "' + str(dat[i]) + '", "' + str(nbins[i]) + '", "' + str(et[i]) + '", "' + str(lon[i]) + '", "' + str(tau[i]) + '", "' + str(taumax[i]) + '", "' + str(phi[i]) + '", "' + '", "' + str(background[i]) + '", "' + str(dlos[i]) + '", "' + str(imaxrr[i]) + '", "' + str(backrr[i]) + '", "' + str(backpts[i]) + '", "' + str(flag[i]) + '", "' + str(source_product[i]) + '", "' + str(cims_product[i]) + '");', file=newFile)
        i += 1

    # Insert b_angle table seperately
    print("INSERT INTO " + deletedExtension + " (b_angle)\nVALUES\n", file=newFile)
    print('\t("' + str(b_angle) + '");', file=newFile)
    
    # close sql file
    newFile.close()
    
    
    
