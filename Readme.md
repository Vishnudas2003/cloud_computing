REAL TIME SYSTEM MONITOR MONITORING PYTHON APP ON K8s!

Things you will Learn 🤯
Python and How to create Monitoring Application in Python using Flask and psutil
How to run a Python App locally.
Learn Docker and How to containerize a Python application
Creating Dockerfile
Building DockerImage
Running Docker Container
Docker Commands
Create ECR repository using Python Boto3 and pushing Docker Image to ECR
Learn Kubernetes and Create EKS cluster and Nodegroups
Create Kubernetes Deployments and Services using Python!

- First we create the app.py, implemented the psutil, flask for backend and rtrieved the cpu and memoty monitor
- Second I created a HTML file with a proper UI
- Used different parameters for preparing 
- source refered : https://www.youtube.com/watch?v=kBWCsHEcWnc&t=949s&ab_channel=CloudChamp
- github : https://github.com/N4si/cloud-native-monitoring-app
- Added the docker file
    - How docker works
        - First initializing the python which is the base image
        - then we define the WORKING DIRECTORY
        - Then copy the requirements.txt 
        - Run the command to install everything from requirements.txt
        - copy the code the application to working directory
        - Set environment variables for the flsk app
        - Expose the port on which the Flask app will run
        - Start the Flask app when the Container is run

- Run docker using  "docker build -t my-flask-app ."

- next step is to deploy in Kubernetes

- ECR share deploy container, publically and privtelly Create a repository to store the images to store then use by containers in kubernetes  

- Instead of creating Repository in ECR website, we are using Boto3 for creating the EC2 repository

- Created the repository using Boto3 successfully. In the Amazon ECR console the repository is properly visiible

Stats Cards:

CPU Usage

RAM Usage

Disk Usage

Uptime

Running Processes

Network I/O

- trying to set back will be back soon