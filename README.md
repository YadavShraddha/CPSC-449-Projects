# CPSC-449 Microblog Project

Description - This project is a microblogging service similar to twitter, created as two separate Flask applications and connected to a single SQLite Version 3 database.


Installation - 

1. Install python 3 and Use the python3 command to run Python and pip from the terminal

2. Run the following command to install Flask

	python3 -m pip install Flask python-dotenv

3. Run the following commands to install Foreman
	
	sudo apt update
	sudo apt install --yes ruby-foreman


How To Run This Application -

1. To create database you can use command flask init. This will create users_887352110.db with user table, posts table, followers table and test data. After running flask init command, users_887352110.db will be created in current directory.
  
2. To run user and timelines services you can simply use foreman start command. 

Files-

1. user.py - This file cotains all the API's related to user service.

2. timelines.py - This file has all the API's related to timeline service.

3. schema.sql - This file will be used to create database tables and populated it with test data.

4. app.py  - This file is responsible for creating custom commands for the application.

5. Procfile - Procfile is used by foreman to start the user and timeline services.

6. RestAPI.pdf - Document describing all the rest endpoints for user and timeline services.


