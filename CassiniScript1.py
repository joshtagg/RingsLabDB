# Joshua Taggart, 9-26-2022
# Purpose of this program: convert .sav files into sql formatted files
# C might be able to traverse the .sav arrays more efficiently??

import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.interpolate as interpolate
import numpy as np

#read in local file (.sav file)
# mydata read as py dictionary
mydata = sio.readsav("C:/Users/joshu/Desktop/FixedRawData/AlpAra032I_data_rad_phi_cpck_070318.sav")

# mydata is read-only
radius = mydata.radius
data = mydata.data
et = mydata.et
lon = mydata.lon
ringoccphi = mydata.ringoccphi

#create new sql file 
#newFile = open('test.sql', 'wt')
newFile = open('C:/Users/joshu/Desktop/TestSQLfiles/test1.sql', 'wt')


#ALL ARRAYS ARE SAME LENGTH
radiusLen = len(mydata.radius)
dataLength = len(mydata.data)
etLength = len(mydata.et)
lonLength = len(mydata.lon)
ringoccphiLength = len(mydata.ringoccphi)
#print('length of radius array: ' + str(radiusLen))
#print('length of data array: ' + str(dataLength))
#print('length of et array: ' + str(etLength))
#print('length of lon array: ' + str(lonLength))
#print('length of ringoccphi array: ' + str(ringoccphiLength))

#-------Process data---------------

#sql file header here
print("CREATE TABLE tableName\n(\n\tradius int,\n\tdata int,\n\tet int,\n\tlon int,\n\tringoccphi int,\n);\n\n", file=newFile)
print("INSERT INTO tableName (radius, data, et, lon, ringoccphi)\nVALUES\n", file=newFile)
i = 0
while i < radiusLen:
    #do thing
    print('\t("' + str(radius[i]) + '", "' + str(data[i]) + '", "' + str(et[i]) + '", "' + str(lon[i]) + '", "' + str(ringoccphi[i]) + '"),', file=newFile)
    i += 1
    #if last variable, instead of ending print with ',' you must end print with ';'

print("program end")


#-------END process data-------






#end of program, close the newly created file
newFile.close()



#test 1 sql file size: 727,495KB

