from flask import Flask, render_template, request,send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import json
from uuid import uuid4


app = Flask(__name__)
CastsFile = os.path.join(app.root_path, 'static','castinfo','casts.json')

if os.path.isfile(CastsFile):
	try:
		with open(CastsFile) as casts:
			CastCache = dict(json.loads(casts.read()))
	except:
		CastCache = {}

else:
	print('No casts available!')
	CastCache = {}

print(CastCache)

@app.route("/favicon.ico")
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico',mimetype='image/vnd.microsof.icon')

@app.route('/', methods = ['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html', ASCIINEMAS = CastCache)
	else:
		print(request.files)
		
		file = request.files['file']
		title = request.form.get('title','N.A.')
		description = request.form.get('description','N.A.')
		file_uuid = str(uuid4()) + '.cast'
		file.save(os.path.join(app.root_path, 'static','cast', file_uuid))
		CastCache.update({file_uuid:{"Title":title,"Description":description,"Date":str(datetime.now())}})
		with open(CastsFile,'w') as casts:
			json.dump(CastCache,casts)
		return 'OK'

#r = requests.post(url, files=files, data=values)

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8000)