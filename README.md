What this project includes:

1. Collection of over 1k images from roboflow dataset ([https://universe.roboflow.com/proyectos-cityfix/pothole-detection-object](https://universe.roboflow.com/aimlprojects/pothole-detection-w3iq7-1msjv)).

<img width="1721" height="818" alt="Screenshot 2026-08-26 231909" src="https://github.com/user-attachments/assets/df01a20c-0b6b-429d-a381-f44aaaaac753" />


3. Training of Yolov11n model with the  dataset.
    
3.A simple locally run Flask app  that uses YOLOv11n model to detect number of potholes in an image.

4.Users can upload their image with the help of a html page rendered by the Flask backend that ingests images later  processed by a python script . Python script helps create JSON files that store metadata about the pothole,location,severity.New markers are rendered by  the  leaflet library  with javascript .

Users can navigate to the 'dashboard' page that is available on different page of the same local flask app.
5. There is also a page called 'Output' that showcases the detected potholes.

   

To use this app:
Download ultralytics,flask libraries:
        pip install flask ultralytics opencv-python requests werkzeug
