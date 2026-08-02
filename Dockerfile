#Official slim version of a python image 
FROM python:3.11.9-slim

#CREATING A FOLDER CALLED APP INSIDE DOCKER IMAGE
WORKDIR /app
#COPYING REQUIREMENTS to app folder in image
COPY requirements.txt ./
#INSTALLING LIBRARIES INSIDE REQUIREMENTS
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y \
    libxcb1 \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install\
    libgl1\
    libgl1-mesa-glx \ 
    libglib2.0-0 -y && \
    rm -rf /var/lib/apt/lists/*
#COPY ALL THE CONTENT TO APP folder
COPY . .
#FLASK SERVER RUNS ON PORT 5000
EXPOSE 5000
#EXECUTE COMMANDS TO RUN THE FLASK APP
CMD ["python","app.py"]
