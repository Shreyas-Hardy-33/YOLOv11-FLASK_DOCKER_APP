import requests
import subprocess as sp
import os
import json
import datetime
from ultralytics import YOLO
from werkzeug.utils import secure_filename
import requests

from flask import Flask, render_template,request

app = Flask(__name__)


#PYTHON FUNCTIONS:
model = YOLO('best.pt')

def get_geolocation():
        try:
            res= requests.get("https://ipinfo.io")
            data=res.json()
            city=data['city']
            print(city)
            location = data['loc'].split(',')
            latitude = float(location[0])
            longitude = float(location[1])
            return city,latitude,longitude
        except Exception as e:
            print(f"Error getting geolocation: {e}")
            return None, None,None


def detect(image):
    results = model.predict(source = image,device=0,save=True,save_dir='static\\output_images')
    severity = 0
    for r in results:
        for box in r.boxes:
            severity = severity + 1
    return severity


UPLOAD_FOLDER = 'inputs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/',methods=['GET','POST'])
@app.route('/uploader',methods=['GET','POST'])
def uploader():
    filename = None
    if request.method=='POST':
        file =  request.files['file']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
            file.save(filepath)
            filename = file.filename
            severity = detect(filepath)
            _,latitude,longitude = get_geolocation()
            time = datetime.datetime.now()
            output_path = "static\\output_images\\" + filename



            json_data = {
                "input_image" : filepath,
                "severity" : severity,
                "time" : str(time),
                "output_image" : output_path,
                "longitude" : longitude, 
                "latitude": latitude
            }

            

            if not os.path.exists('static\\pothole_data.json'):
                with open('static\\pothole_data.json','w') as f:
                    json.dump([json_data],f,indent=4)
            else:
                with open('static\\pothole_data.json','r') as f:
                    data = json.load(f)
                data.append(json_data)
                with open('static\\pothole_data.json','w') as file: 
                    json.dump(data,file)


    return render_template('uploader.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/output')
def output():
    
    with open('static\\pothole_data.json','r') as f:
        data = json.load(f)
    
    image = data[-1].get("output_image")
    return render_template('output.html',image=image)


if __name__ == '__main__':
    app.run(debug=True)