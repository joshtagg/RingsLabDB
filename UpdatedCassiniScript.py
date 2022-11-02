# Joshua Taggart, 10-16-22
# Purpose of this program: convert .sav files into sql formatted files
# New script to work with UVIS 1k and 10k .sav files

from requests import delete
import scipy.io as sio
import os

# assign directory
#directory = 'C:/Users/joshu/Desktop/FixedRawData/UVIS 1km Radially Binned PDS data IDL Save Files'
directory = 'C:/Users/joshu/Desktop/FixedRawData/UVIS 10km Radially Binned PDS Data in IDL Save Files'

'''
(18 total arrays?)
arrays within 10km and 1km binned data:
    pdsdata.radius      -> name it: rad10km if 10km file    else, name it: rad1km
    pdsdata.dat         -> name it: dat10km if 10km file    else, name it: dat1km (binned photon counts)
    pdsdata.nbins       -> name it: nbin10km if 10km file   else, name it: nbin1km
    et (ephimerus time, sec)
    lon (longitude, intertial frame)
    tau (normal optical depth)
    taumax (max measurable nod)
    phi (clock angle, from outward radial direction from saturn to the line of sight to the projection in the line of sight to the star in the ring plane)
    b_angle (ring plane declination angle)
    background (bakcground photon count level)
    dlos (line of sight distance from cassini to the occultation point in the ring)
    imaxrr (radial locations where the unocculted star signal was observed)
    imaxpts (unocculted star signal + background)
    backrr (radial locations where the ring was opaque and the background signal was observed)
    backpts (background signal at those locations)
    flag (note flag, 0-128, note reference)
    source_product (name of the unbinned data file from which these vectors were made)
    cims_product (*unimportant)
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

    #TEST
    print("currenntly creating file: " + curFile)

    '''
    #TEST
    for key in mydata:
        #print("the key name is: " + key + "and its value is: " + mydata[key])
        print(mydata.items())
    '''

    if curFile == "LAM AQL 132_UVIS_Egress_bad_bckgnd_1km.sav" or curFile == "LAM AQL 132_UVIS_Egress_bad_bckgnd_10km.sav":
        #TEST
        #for key in mydata:
            #print(mydata.items())
        imaxrr = mydata.pdsdata.i0rr[0]

    else:
        imaxrr = mydata.pdsdata.imaxrr[0]


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
    #imaxrr = mydata.pdsdata.imaxrr[0]
    backrr = mydata.pdsdata.backrr[0]
    backpts = mydata.pdsdata.backpts[0]
    flag = mydata.pdsdata.flag[0]
    source_product = mydata.pdsdata.source_product[0]
    cims_product = mydata.pdsdata.cims_product[0]

    # find len of array (all arrays in .sav file are the same length)
    arrayLen = len(radius)

    # delete .sav extension from curFile
    deletedExtension = curFile.rsplit(".", 1)[0]
    # delete spaces (sql table name cannot have them)
    deletedExtension = deletedExtension.replace(' ', '')

    '''
    #TEST
    #b_angleLen = len(b_angle)
    #print("length of b_angleLen array: " + str(b_angleLen))
    #print(radius)
    print("b_angle number as string: " + str(b_angle))
    print("b_angle number: " + b_angle)
    
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

    #same length: radius, dat, nbins, et, lon, tau, taumax, phi, background, dlos, flag     (arrayLen)
    #length of 1: b_angle
    #unique length: imaxrr      (arrayLen2)
    #same length: backrr, backpts   (arrayLen3)
    #unique length: source_product  (arrayLen4)
    #unique length: cims_product    (arrayLen5)
    #TEST
    '''

    # change destination based on 1k or 10k files
    # create new .sql file for curFile
    #newFile = open("C:/Users/joshu/Desktop/Repos/RingsLabDB/1k/" + deletedExtension + ".sql", 'wt')
    newFile = open("C:/Users/joshu/Desktop/Repos/RingsLabDB/10k/" + deletedExtension + ".sql", 'wt')
    

    # Printing to new .sql file (inserting table header)
    #CHANGE: print statement. add id array that is the length of arrayLen, in this array. Id starts at 1. NOT NULL, AUTO_INCREMENT
    print("CREATE TABLE " + deletedExtension + "\n(\n\tradius int,\n\tdat int,\n\tnbins int,\n\tet int,\n\tlon int, \n\ttau int, \n\ttaumax int, \n\tphi int, \n\tbackground int, \n\tdlos int, \n\timaxrr int, \n\tbackrr int, \n\tbackpts int, \n\tflag int, \n\tsource_product int, \n\tcims_product int\n);\n\n", file=newFile)
    #CHANGE: don't need to manually update ID here 
    print("INSERT INTO " + deletedExtension + " (radius, dat, nbins, et, lon, tau, taumax, phi, background, dlos, flag)\nVALUES\n", file=newFile)
    i=0
    #CHANGE: don't need to manually update ID here 
    while i < arrayLen:
        print('\t("' + str(radius[i]) + '", "' + str(dat[i]) + '", "' + str(nbins[i]) + '", "' + str(et[i]) + '", "' + str(lon[i]) + '", "' + str(tau[i]) + '", "' + str(taumax[i]) + '", "' + str(phi[i]) + '", "' +  str(background[i]) + '", "' + str(dlos[i]) + '", "' + str(flag[i]) + '"),', file=newFile)
        #if last variable, instead of ending print with ',' you must end print with ';'
        if i == arrayLen-1:
            print('\t("' + str(radius[i]) + '", "' + str(dat[i]) + '", "' + str(nbins[i]) + '", "' + str(et[i]) + '", "' + str(lon[i]) + '", "' + str(tau[i]) + '", "' + str(taumax[i]) + '", "' + str(phi[i]) + '", "' + str(background[i]) + '", "' + str(dlos[i]) + '", "' + str(flag[i]) + '");', file=newFile)
        i += 1

    #CHANGE: print. set b_angle = value where ID = 1 (SQL syntax)
    # Insert b_angle table seperately (length of 1)
    # Turn b_angle into string because it prints with brackets [] for some reason
    b_angleString = str(b_angle)
    b_angleString = b_angleString.replace('[', '')
    b_angleString = b_angleString.replace(']', '')
    print("INSERT INTO " + deletedExtension + " (b_angle)\nVALUES\n", file=newFile)
    #print('\t("' + str(b_angle) + '");', file=newFile)
    print('\t("' + b_angleString + '");', file=newFile)
    
    #CHANGE: print loop, set imaxrr= [i] where ID = i+1 (SQL syntax)
    # Insert imaxrr seperately
    arrayLen2 = len(imaxrr)
    print("INSERT INTO " + deletedExtension + " (imaxrr)\nVALUES\n", file=newFile)
    i = 0
    while i < arrayLen2:
        print('\t("' + str(imaxrr[i]) + '"),', file=newFile)

        if i == arrayLen2-1:
            print('\t("' + str(imaxrr[i]) + '");', file=newFile)
        i+=1

    #CHANGE: change print, set backrr = [i] and backpts = [i]
    # Insert backrr and backpts seperately
    arrayLen3 = len(backrr)
    print("INSERT INTO " + deletedExtension + " (backrr, backpts)\nVALUES\n", file=newFile)
    i=0
    while i < arrayLen3:
        print('\t("' + str(backrr[i]) + '", "' + str(backpts[i]) + '"),', file=newFile)

        if i == arrayLen3-1:
            print('\t("' + str(backrr[i]) + '", "' + str(backpts[i]) + '");', file=newFile)
        i+=1

    #CHANGE: change print, set source_product = [i] where ID = i+1 (SQL syntax)
    # Insert source_product seperately
    arrayLen4 = len(source_product)
    print("INSERT INTO " + deletedExtension + " (source_product)\nVALUES\n", file=newFile)
    i = 0
    while i < arrayLen4:
        print('\t("' + str(source_product[i]) + '"),', file=newFile)

        if i == arrayLen4-1:
            print('\t("' + str(source_product[i]) + '");', file=newFile)
        i+=1

    #CHANGE: change print, set cims_product = [i] where ID = i+1 (SQL syntax)
    # Insert cims_product seperately
    arrayLen5 = len(cims_product)
    print("INSERT INTO " + deletedExtension + " (cims_product)\nVALUES\n", file=newFile)
    i=0
    while i < arrayLen5:
        print('\t("' + str(cims_product[i]) + '"),', file=newFile)

        if i == arrayLen5-1:
            print('\t("' + str(cims_product[i]) + '");', file=newFile)
        i+=1

    #TEST
    print("done creating file: " + deletedExtension)

    # close sql file
    newFile.close()
    
    
    #FIXES:
    #b_angle prints with brackets [] for some reason [FIXED 10-19-22]
    #table name has spaces, remove spaces [FIXED 10-19-22]
    
    #TODO:
    #carefully look over sql files, proofread