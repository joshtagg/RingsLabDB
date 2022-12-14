from flask import Flask, render_template, request, redirect, url_for

import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.interpolate as interpolate
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('template.html')

#handler for managing "upload file" button
@app.route('/', methods=['POST'])
def upload_file():
	uploaded_file = request.files['file']
	if uploaded_file.filename != '':
		uploaded_file.save(uploaded_file.filename)
	

	#------------------SCRIPT-------------------------------
	mydata = sio.readsav(uploaded_file.filename)
	radius = mydata.radius
	data = mydata.data
	et = mydata.et
	lon = mydata.lon
	ringoccphi = mydata.ringoccphi

	#DELETE .SAV FROM FILENAME
	deletedExtension = uploaded_file.filename.rsplit( ".", 1 )[ 0 ]
	#DELETE .SAV FROM FILENAME

	newFile = open(deletedExtension + ".sql", 'wt')

	radiusLen = len(mydata.radius)

	#Printing to the sql file
	print("CREATE TABLE " + deletedExtension + "\n(\n\tradius int,\n\tdata int,\n\tet int,\n\tlon int,\n\tringoccphi int,\n);\n\n", file=newFile)
	print("INSERT INTO " + deletedExtension + " (radius, data, et, lon, ringoccphi)\nVALUES\n", file=newFile)
	i = 0
	while i < radiusLen:
		#do thing
		print('\t("' + str(radius[i]) + '", "' + str(data[i]) + '", "' + str(et[i]) + '", "' + str(lon[i]) + '", "' + str(ringoccphi[i]) + '"),', file=newFile)
		#if last variable, instead of ending print with ',' you must end print with ';'
		if i == radiusLen-1:
			print('\t("' + str(radius[i]) + '", "' + str(data[i]) + '", "' + str(et[i]) + '", "' + str(lon[i]) + '", "' + str(ringoccphi[i]) + '");', file=newFile)
		i += 1

	newFile.close()
	#------------------SCRIPT-------------------------------


	return redirect(url_for('index'))
	
	

#app.run(port=9999, debug=True)

##TEST##
import random, threading, webbrowser
if __name__ == '__main__':
	port = 5000 + random.randint(0, 999)
	url = "http://127.0.0.1:{0}".format(port)

	threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
	app.run(port=port, debug=False)





#--------------------------------

# NEXT STEPS:
# upload multiple files at one instance
# send .sql files into specific folder, away from everything else