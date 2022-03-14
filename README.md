# MATH_OPERATIONAL_PROJECT
## Table of Content:
- General information

- Technology

### General information:
This project perform math operation of factorial,square,cube on 
a number that will be taken from a user.
we make a docker container for user convenience to run this project 
without any trouble.

>'POST' api is being running now.

### Technologies:
First clone the repository on your local machine  then run ***main.py***
file you have to install all the following requirements in your machine:

install ```python version 3.9```

install ```Conda``` virtual Environment

install ```flask 2.0.3```

install docker engine using this link```https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository``` 
 
**docker-compose.yml** file is used to run docker using command ==>docker-compose up --build

Need little guidance in **.gitignore file**.

**post req.html** is html form.

### Running OF PROJECT:
main code is present in **main.py** file.after running main.py 
file get API or second method is when user run docker container
user get API link then user have to write **mathoperation** and 
after **/** put a number as an argument  on which user want to perform function.Output data is in JSON  format.the applicatiion runs in a docker container with all its dependencies. 
#### POST Request:
 For testing go to http://localhost:5004/data with POST request 
 and send data as www-url-form-encoded.
 
## URL for published documentation

  https://documenter.getpostman.com/view/20009397/UVsJxSdZ
