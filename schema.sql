/* Name - Shraddha Yadav 
 CPSC 449 Project - 2
 */

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS followers;
DROP TABLE IF EXISTS user;

CREATE TABLE user( username VARCHAR PRIMARY KEY, email VARCHAR NOT NULL, password VARCHAR NOT NULL);

CREATE TABLE followers(userFollower VARCHAR NOT NULL,usernameToFollow VARCHAR NOT NULL,CONSTRAINT fk_user FOREIGN KEY(userFollower)REFERENCES user(username),CONSTRAINT fk_user FOREIGN KEY(usernameToFollow)REFERENCES user(username));

CREATE TABLE post(authorname VARCHAR NOT NULL,postText TEXT,postTimestamp TEXT,CONSTRAINT fk_user FOREIGN KEY(authorname)REFERENCES user(username));

INSERT INTO user (username, email, password) VALUES
('jake','jake123@gmail.com','pbkdf2:sha256:150000$3lkQmZGS$1cb111b83789b38240b7da433aa2126562e21f868e77af9796a93a40acbf56c3'),
('tom','tom@gmail.com','pbkdf2:sha256:150000$Y2GTIfAK$a6b29a3f90769fc98f91e8c8ac9ccbe5a1de64cfe7e0ef93b8111c0ab0d7768a'),
('stan','stan4@gmail.com','pbkdf2:sha256:150000$B467dacH$fbfe3c8e2823117de31d336c4ecf4b3ad2de11a8677e0e685a6d446299b4d563'),
('rohan','rohan.y@gmail.com','pbkdf2:sha256:150000$Hr64rXke$b971ec9f1a87276d03952dad49ede003f0d5cb19848bd8cc49cbf99bbd3255c8'),
('peter','peterpan@yahoo.com','pbkdf2:sha256:150000$RU7W0TGd$3263bfbfd712873cc016fb5a90f2fe94ce2986c8969904f3a7851413d1e51c26');

INSERT INTO followers(userFollower,usernameToFollow) VALUES ('jake','tom'),('jake','stan'),('jake','peter'),
('tom','peter'),('stan','rohan'),('stan','jake'),('stan','tom'),('rohan','jake'),('rohan','peter'),('rohan','tom'),
('peter','rohan'),('peter','tom'),('peter','stan'),('peter','jake');


INSERT into post (authorname, postText,postTimestamp) values ('jake','blog1','2020-10-04 20:1:58.290501'),('jake','blog2','2020-10-04 20:2:58.290501'),
('jake','blog3','2020-10-04 20:3:58.290501'),('jake','blog4','2020-10-04 20:14:58.290501'),('jake','blog5','2020-10-04 20:5:58.290501'),
('jake','blog6','2020-10-04 20:18:58.290501'),('tom','blog7','2020-10-04 20:19:58.290501'),('tom','blog8','2020-10-04 20:20:58.290501'),
('tom','blog9','2020-10-04 20:21:58.290501'),('tom','blog10','2020-10-04 20:22:58.290501'),('stan','blog11','2020-10-05 20:16:58.290501'),
('stan','blog12','2020-10-05 20:18:58.290501'),('stan','blog13','2020-10-05 20:20:58.290501'),('stan','blog14','2020-10-06 20:16:58.290501'),
('stan','blog15','2020-10-06 20:22:58.290501'),('rohan','blog16','2020-10-05 20:17:58.290501'),('rohan','blog17','2020-10-05 20:23:58.290501'),
('rohan','blog18','2020-10-05 20:11:58.290501'),('rohan','blog19','2020-10-06 20:12:58.290501'),('rohan','blog20','2020-10-05 20:15:58.290501'),
('rohan','blog21','2020-10-02 20:18:58.290501'),('peter','blog22','2020-10-02 20:19:58.290501'),('peter','blog23','2020-10-03 20:15:58.290501'),
('peter','blog24','2020-10-01 18:16:58.290501'),('jake','blog25','2020-10-04 16:16:58.290501'),('jake','blog26','2020-10-04 17:18:58.290501'),
('rohan','blog27','2020-10-01 18:11:58.290501'),('peter','blog28','2020-10-04 16:16:58.290501'),('jake','blog29','2020-10-04 17:12:58.290501');


