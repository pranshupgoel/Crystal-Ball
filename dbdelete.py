import mysql.connector
from dbinfo import *

f = mysql.connector.connect(host = "localhost", user = db_username, passwd = db_password)
mycur = f.cursor()
mycur.execute("drop database one_stop_healthcare;")

print("The database has been deleted sucessfully! Thank you for your valuable time!")