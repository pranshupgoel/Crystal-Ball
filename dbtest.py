from dbinfo import *
import mysql.connector

try:
    f = mysql.connector.connect(host = "localhost", user = db_username, passwd = db_password)
except:
    print("Your database username or password is wrong. Please go to dbinfo.py file and change it to the correct username and password.")
else:
    print("The username and password is correct and now you can move forward! :)")
