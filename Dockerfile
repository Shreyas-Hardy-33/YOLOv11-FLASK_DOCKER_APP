#Official slim version of a python image 
FROM python:3.11.9-slim

#CREATING A FOLDER CALLED APP INSIDE DOCKER IMAGE
WORKDIR /app
#COPYING REQUIREMENTS to app folder in image
COPY requirements.txt ./
#INSTALLING LIBRARIES INSIDE REQUIREMENTS
RUN pip install --no-cache-dir -r requirements.txt

#COPY ALL THE CONTENT TO APP folder
COPY . .
#FLASK SERVER RUNS ON PORT 5000
EXPOSE 5000
#EXECUTE COMMANDS TO RUN THE FLASK APP
CMD ["python","app.py"]
