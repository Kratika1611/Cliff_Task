# Step 1 select default OS image
FROM centos

# Step 2 Setting up environment
RUN yum install  python3-pip -y && pip3 install --upgrade pip 

# Step 3 Configure a software
WORKDIR /app

RUN pip3 install flask
RUN pip3 install pymongo

# Copying project files.
COPY ["app.py", "/app/"]

# Exposing an internal port
EXPOSE 80





