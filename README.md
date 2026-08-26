What this project includes:

->Collection of over 1k images from roboflow dataset ([https://universe.roboflow.com/proyectos-cityfix/pothole-detection-object](https://universe.roboflow.com/aimlprojects/pothole-detection-w3iq7-1msjv)).

<img width="1721" height="818" alt="Screenshot 2026-08-26 231909" src="https://github.com/user-attachments/assets/df01a20c-0b6b-429d-a381-f44aaaaac753" />


->Training of Yolov11n model with the  dataset in colab notebook: !yolo model=yolo11n.pt task=detect mode=train epochs=20 imgsz=640 data=location_of_dataset

->A simple locally run Flask app  that uses YOLOv11n model to detect number of potholes in an image.

<img width="573" height="104" alt="Screenshot 2026-08-26 234106" src="https://github.com/user-attachments/assets/5cece284-5aab-47cd-b7c1-fe7963dab4e6" />

->Users can upload their image with the help of a html page rendered by the Flask backend that ingests images later  processed by a python script . Python script helps create JSON files that store metadata about the pothole,location,severity.New markers are rendered by  the  leaflet library  with javascript .

->Users can navigate to the 'dashboard' page that is available on different page of the same local flask app.

<img width="1443" height="575" alt="Screenshot 2026-08-26 234305" src="https://github.com/user-attachments/assets/f2bc4c9d-201b-4ec9-b7cf-a3089fcee621" />


->There is also a page called 'Output' that showcases the detected potholes with a confidence score from the model inference.

<img width="1455" height="593" alt="Screenshot 2026-08-26 234201" src="https://github.com/user-attachments/assets/964ae09f-6db6-48d7-bc47-43b950bef33a" />



   

To use this app:
Download ultralytics,flask libraries:
        pip install flask ultralytics opencv-python requests werkzeug
