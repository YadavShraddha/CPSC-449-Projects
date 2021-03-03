# Name - Shraddha Yadav 

from flask import Flask, jsonify,request,make_response,abort
from werkzeug.security import generate_password_hash, check_password_hash
import re
import sqlite3

app = Flask(__name__)

# create a new user

@app.route('/createUser', methods=["GET","POST"])
def newuser():
# extract values from json
    username = request.json["username"].replace(" ", "")
    email = request.json["email"]
    password = request.json["password"]      
    
# validate given input
    if username == "":
            return jsonify("Enter valid Username!"),400

    if password == "" or len(password) < 5:
        return jsonify("Passowrd is less than 5 characters. Enter a strong password!"),400
        
    regex = '^[a-z0-9]+[\\._]?[a-z0-9]+[@]\\w+[.]\\w{2,3}$'
    if email == "" or not re.search(regex,email): 
        return jsonify("Enter a email in correct format!"),400

# insert into database
    password = generate_password_hash(password)

    try:
        with sqlite3.connect("users_887352110.db") as con:      
            cursor = con.cursor()
            cursor.execute("INSERT into user (username, email, password) values (?,?,?)",(username,
                email,password))
            con.commit()
    except sqlite3.IntegrityError as ie:
        con.rollback()
        con.close()
        return jsonify("UserName already exists!"),409
    except Exception as e:
        con.rollback()
        con.close()
        return jsonify("Problem while connecting to database"),500

# Create json object that needs to be returned
    userdata = {
            'username' : username,
            'email' : email,
            'password' : password
        } 
    return jsonify(userdata),201

# Authenticate the user

@app.route('/authenticateUser', methods=["GET","POST"])

def login():
# extract values from json
    username = request.json["username"].replace(" ", "")
    password = request.json["password"]

# connect to databse
    try:
        with sqlite3.connect("users_887352110.db") as con:      
            cursor = con.cursor()
            #Retrieve user from user table.
            cursor.execute("SELECT * FROM user WHERE username = ?", (username,))
            user = cursor.fetchone()
            con.commit()
    except Exception as e:
        con.rollback()
        con.close()
        return jsonify("Problem while executing query!"),500

# check given input with stored hashed value

    if user and check_password_hash(user[2], password):
        return jsonify("Login successful!"),200
    else:
        return jsonify("Unauthorized Login!"),401

# Add Followers

@app.route('/addFollower', methods=["GET","POST"])

def followers():
# extract values from json
    username = request.json["username"].replace(" ", "")
    usernameToFollow = request.json["usernameToFollow"]
    userdata = {
            'username' : username,
            'usernameToFollow' : usernameToFollow
        }
# connect to databse
    try:
        with sqlite3.connect("users_887352110.db") as con:     
            cursor = con.cursor()
            #Check if user already has this follower
            cursor.execute("SELECT * FROM followers WHERE userFollower = ? AND usernameToFollow = ?", (username, usernameToFollow))    
            result = cursor.fetchall()
            if result:
                return jsonify(userdata),200
            cursor.execute('pragma foreign_keys = ON')
            cursor.execute("INSERT into followers (userFollower, usernameToFollow) values (?,?)",(username,
            usernameToFollow))
            con.commit()
    except Exception as e:
        con.rollback()
        con.close()
        return jsonify("Problem while executing query!"),500

    return jsonify(userdata),200

@app.route('/removeFollower', methods=["GET","POST"])

# remove followers 

def removefollowers():
# extract values from json
    username = request.json["username"].replace(" ", "")
    usernameToFollow = request.json["usernameToFollow"]
# connect to databse
    try:
        with sqlite3.connect("users_887352110.db") as con:     
            cursor = con.cursor()
            #Check if user and follower present
            cursor.execute("SELECT * FROM followers WHERE userFollower = ? AND usernameToFollow = ?", (username, usernameToFollow))    
            result = cursor.fetchall()
            if result: 
                #remove follower from database
                cursor.execute('pragma foreign_keys = ON')
                cursor.execute("DELETE FROM followers WHERE userFollower = ? AND usernameToFollow = ?", (username, usernameToFollow))
            else:
                return jsonify("Record not found!"),404
                con.commit()
    except Exception as e:
        con.rollback()
        con.close()
        return jsonify("Problem while executing query!"),500

    return jsonify("Record Deleted!"),200
      
if __name__ == '__main__':
    app.run(debug = True)


  
