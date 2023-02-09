## Deployment link
### Airflow:
```
http://ec2-15-206-100-39.ap-south-1.compute.amazonaws.com:8080
(Link might have expired)
```
### For real-time prediction:
```
http://thyroiddiseasedetection-env-1.eba-wj7msmpa.us-east-1.elasticbeanstalk.com/

```
### Problem Statement
Thyroid disease is one of the most common disease with endocrine disorder in the human population today. For example hyperthyroidism (over) and hypothyroidism (under), which are relate to release of amount of thyroid hormones the thyroid gland produces and whether it is over active trusted source (when thyroid gland makes too much thyroid hormone) or under active trusted source (when the thyroid gland doesn’t make enough thyroid hormone). We need to identify whether the patient has thyroid or not.

### Solution Proposed 
We need to build a ML model which will be used by hospitals and help the hospital authority to identify if the patient has thyroid or not. If it is a positive case then medical will do further test to know what type of thyroid the person is suffering from and according to that the treatment will be on fast-track. The doctors will start treating the patients. If the result will come negative then the patient will be sent to a junior doctor and the junior doctors by using their own expertise they will decide that if the model has done correct prediction or not. If analysis comes true then the doctor release the patient. By seeing the readings if doctor analysed that there may be a chance of thyroid then patient sent to the senior doctors. 

## Tech Stack Used
1. Python 
2. VS Code 
3. Machine learning algorithms
4. Docker
5. MongoDB
6. Flask

## Infrastructure Required.
1. AWS S3
2. AWS EC2
3. AWS ECR
4. Github Actions
5. Airflow
6. AWS Elastic Beanstalk

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

By running the Airflow link you will get this interface

![image](https://user-images.githubusercontent.com/102937478/217749340-80b32acb-614b-48d8-b886-97c47891c3ef.png)


For real-time prediction you can use the above Elastic Beanstalk link 

or 

1. Run this project in local by executing the code "python app.py"
2. In browser open "http://127.0.0.1:5000/" link or Check the log file to get the default link
3. You will get an UI displayed below.
![Throid](https://user-images.githubusercontent.com/88229259/217767176-f931639e-1881-480d-a1a4-8013f5e5f044.PNG)
4. Enter patients data and click on "Predict" button
![3 PNG](https://user-images.githubusercontent.com/88229259/217767290-dc073461-9b57-4e8e-902f-713440c2e6ec.jpg)
5. You'll get the result below input table
![4](https://user-images.githubusercontent.com/88229259/217767364-e26b90bf-782a-4fb5-8cf3-3f173d9fb0c5.jpg)
6. To get out of the terminal use cntr + C.

## Data Collections
![image](https://user-images.githubusercontent.com/102937478/216246951-7c187908-a8b0-4c64-8f37-6549c49e20fa.png)


## Project Archietecture
![image](https://user-images.githubusercontent.com/102937478/216756199-b340e838-74e8-43c7-964a-5ac6e3a8d5ff.png)

![image](https://user-images.githubusercontent.com/102937478/216757352-0d9a4c4c-b0c3-43c1-9bf8-92ee9a6df352.png)


#### Real-time Prediction

![image](https://user-images.githubusercontent.com/102937478/216313545-4db56ed7-63f0-4476-b518-10ed51a32f17.png)


## Deployment Archietecture
![Screenshot_19-overlay](https://user-images.githubusercontent.com/102937478/216320740-d0494ad2-c99c-4a1b-91e3-01b86c0deaee.png)

![image](https://user-images.githubusercontent.com/102937478/216247497-0d54dd7b-3916-4670-8465-3f1fcf6e0a9a.png)

## Pipeline
![image](https://user-images.githubusercontent.com/102937478/216771378-4990ae29-e5c2-44df-9af4-abb1724e26b5.png)

![image](https://user-images.githubusercontent.com/102937478/216771387-5ff808e2-fda3-449c-b444-37d064d552e4.png)


### Step 1: Clone the repository
```bash
git clone https://github.com/itsguptaaman/Thyroid-Disease-Detection
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create --prefix ./env python=3.7 -y
conda activate ./env
```

```bash
conda activate thyroid
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://admin:Aman@cluster0.a75efai.mongodb.net/?retryWrites=true&w=majority"

```

### Step 5 - Run the application server
```bash
python main.py
```


## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

To run the project  first execute the below commmand.
MONGO DB URL: 
```
mongodb+srv://MongoDB:Sai12345@cluster0.i7o85x8.mongodb.net/?retryWrites=true&w=majority
```
windows user

```
MONGO_DB_URL=mongodb+srv://MongoDB:Sai12345@cluster0.i7o85x8.mongodb.net/?retryWrites=true&w=majority
```

Linux user

```
mongodb+srv://MongoDB:Sai12345@cluster0.i7o85x8.mongodb.net/?retryWrites=true&w=majority
```

then run 
```
python main.py
```

### To download the dataset 
```
wget https://raw.githubusercontent.com/itsguptaaman/Thyroid-Disease-Detection/main/hypothyroid.csv
```
## For Neuro lab users
### To check and reset git log
```
git log
git reset --soft 6afd
6afd -> last 4 digit of log. 
```

### To add and uplod to git
```
git add filename
we can also use . for all file(Current directory)

git commit -m "Message"
git push origin main
```

### To run jupyter-notebook in vscode
```
 pip install ipykernel
```

### **To create a new environment in vscode** 
 1. Select the command prompt as a terminal 
```
conda create -p venv python==3.87 -y
```

### Create a .env It contains details.
```
MONGO_DB_URL="mongodb://localhost:27017/neurolabDB"
AWS_ACCESS_KEY_ID="aagswdiquyawvdiu"
AWS_SECRET_ACCESS_KEY="sadoiuabnswodihabosdbn"
```
### **To install dockers in aws machine (EC2)**
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

**Secrets**
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME=
BUCKET_NAME=
MONGO_DB_URL=
```
