import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.interpolate as interpolate
import numpy as np

#as to my understanding, the .sav file just contains arrays for: radius, data, et, lon, ringoccphi

# read in .sav file
# occultation of Alpha Arae on orbit 32
mydata = sio.readsav("C:/Users/joshu/Desktop/FixedRawData/AlpAra032I_data_rad_phi_cpck_070318.sav")

'''
# mydata is read-only
radius = mydata.radius
data = mydata.data
et = mydata.et
lon = mydata.lon
ringoccphi = mydata.ringoccphi
'''
# create a clone of mydata
radius = np.copy(mydata.radius)
data = np.copy(mydata.data)
et = np.copy(mydata.et)
lon = np.copy(mydata.lon)
ringoccphi = np.copy(mydata.ringoccphi)

#print(lon[0])

#plot data
#plt.plot(radius, data)
#plt.show()

#zoom in on smaller set
plt.plot(radius, data, 'b-', [84750, 84950], [10, 40], 'ro') # 'b-' == blue line, 'ro' == red dot
plt.show()


