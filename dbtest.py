from dbinfo import *
import mysql.connector

f = mysql.connector.connect(host = "localhost", user = db_username, passwd = db_password)

print("The username and password is correct and now you can move forward! :)")
