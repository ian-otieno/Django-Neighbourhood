# Django-Neighbourhood
This Djanngo neighbourhood web application was created on 17/4/2022

# Author
## By **[ IAN OTIENO](https://github.com/ian-otieno)**

## Description
A Django web application that allows registered users to know about everything happening in their current neighborhoods. Registered user must be a member to a given neighbourhood to post or see news related.

## Live Demo
Click on the link below to view the site :https://ianeighbourhood.herokuapp.com/

## Requirements
The user can perform the following functions:

- A user can sign in with the application to start using.
- A user can set up a profile about me and a general location and my neighborhood name.
- A user can find a list of different businesses in my neighborhood.
- A user can create posts that will be visible to everyone in my neighborhood.
- A user can change their neighborhood when I decide to move out.
- A user can find contact information for the health department and Police authorities near my neighborhood.
- A user can only view details of a single neighborhood.

## Installation / Setup instruction
The application requires the following installations to operate:
- pip
- gunicorn
- django
- postgresql

## Technologies Used
- python 3.8.10

## Setup/Installation Requirements
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/ian-otieno/Django-Neighbourhood.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations 
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Known Bugs

No known bugs


## Contacts
Email: ian.otieno@student.moringaschool.com

 &#169; 2022 Ian Otieno
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)