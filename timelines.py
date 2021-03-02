# Name - Shraddha Yadav [CWID - 887352110]
# Email - shraddhayadav@csu.fullerton.edu
# CPSC 449 Project - 2


from flask import Flask,jsonify,request
import sqlite3
import datetime

app = Flask(__name__)

# Post a new tweet

@app.route('/postTweet', methods=["POST"])
def tweets():
# extract values from json
    username = request.json["username"]
    post = request.json["post"]
    timestamp = datetime.datetime.now()

# Create json object that needs to be returned
    userdata = {
            'username' : username,
            'post' : post,
            'timestamp' : timestamp
        }
# insert into database
    try:
        with sqlite3.connect("users_887352110.db", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES) as con:     
            cursor = con.cursor()
            cursor.execute('pragma foreign_keys = ON')
            cursor.execute("INSERT into post (authorname, postText,postTimestamp) values (?,?,?)",(username,
            post,timestamp))
            cursor.fetchall()
            con.commit()
    except Exception as e:
        con.rollback()
        con.close()
        return jsonify("Problem while executing query!"),500

    return jsonify(userdata),200

# get the recent tweets of all the users

@app.route('/getPublicTimeline', methods=["GET"])
def publictimeline():
# connect to database
    try:
        with sqlite3.connect("users_887352110.db") as con:     
            cursor = con.cursor()
            cursor.execute('pragma foreign_keys = ON')
            #Sort posts by time and retrieve only most recent 25 entries.
            cursor.execute("SELECT * FROM post ORDER BY postTimestamp DESC LIMIT 25")
            result = cursor.fetchall()
            con.commit()
    except Exception as e:
        con.rollback()
        con.close()
        return jsonify("Problem while executing query!"),500

    return jsonify(result),200

# get the recent tweets of a perticular user

@app.route('/getUserTimeline', methods=["POST"])
def usertimeline():
# extract values from json
	username = request.json['username']

# Create json object that needs to be returned
	userdata = {
            'username' : username  
        }
# connect to database
	try:
		with sqlite3.connect("users_887352110.db") as con:
			cursor = con.cursor()
			cursor.execute('pragma foreign_keys = ON')
			#Check if user is present
			cursor.execute("SELECT * FROM user WHERE username = ?",(username,)) 
			if not cursor.fetchall():
				return jsonify("User not found!!"),404
			else:
				#Select 25 most recent post from given user
				cursor.execute('pragma foreign_keys = ON')
				cursor.execute("SELECT * FROM post WHERE authorname = ? ORDER BY postTimestamp DESC LIMIT 25",(username,)) 
				result = cursor.fetchall()
				con.commit()
	except Exception as e:
		con.rollback()
		con.close()
		return("Problem while executing query!"),500

	return jsonify(result),200

# recent tweets from all users that a user follows

@app.route('/getHomeTimeline', methods=["POST"])

def hometimeline():
# extract values from json
	username = request.json['username']

# Create json object that needs to be returned
	userdata = {
            'username' : username  
        }
# connect to database
	try:
		with sqlite3.connect("users_887352110.db") as con:
			cursor = con.cursor()
			#Check if user has any followers, if not retrun 404
			cursor.execute("SELECT * FROM followers WHERE userFollower = ?", (username,))
			if not cursor.fetchall():
				return jsonify("This user is not following any user !!"),404
			else:
				cursor.execute('pragma foreign_keys = ON')
				cursor.execute("SELECT post.* FROM post INNER JOIN followers ON followers.usernameToFollow = post.authorname WHERE followers.userFollower =? ORDER BY postTimestamp DESC LIMIT 25",(username,))
				result = cursor.fetchall()
				con.commit()
	except Exception as e:
		con.rollback()
		con.close()
		return("Problem while executing query!"),500

	return jsonify(result),200

if __name__ == '__main__':
	app.run(debug = True)