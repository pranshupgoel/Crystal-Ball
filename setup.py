import mysql.connector
from dbinfo import *

f = mysql.connector.connect(host = "localhost", user = db_username, passwd = db_password)
mycur = f.cursor()

#Creating the database
mycur.execute("create database One_Stop_Healthcare;")
mycur.execute("use One_Stop_Healthcare;")
print("Database created!")

#Creating a table ccinfo and inserting values
mycur.execute("create table ccinfo(ID INTEGER NOT NULL primary key, NAME varchar(20), LOCATION varchar(20), BEDS integer, DISCHARGED integer, ACTIVE integer, DEAD integer, DOCTORS integer, MONEY integer, PPE_KITS integer, BLANKETS integer, MASKS integer, SANITIZER integer);")

mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, PPE_KITS, BLANKETS, MASKS, SANITIZER)values(1, 'Ward-1', 'KRM', 500, 100, 300, 50, 25, 20, 100, 100, 70);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, PPE_KITS, BLANKETS, MASKS, SANITIZER)values(2, 'Ward-2', 'KRM', 600, 290, 250, 85, 78, 40, 150, 300, 90);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, PPE_KITS, BLANKETS, MASKS, SANITIZER)values(3, 'Ward-3', 'KRM', 600, 210, 300, 75, 57, 40, 200, 250, 40);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, PPE_KITS, BLANKETS, MASKS, SANITIZER)values(4, 'Ward-4', 'HSR', 700, 400, 330, 60, 50, 70, 200, 300, 50);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, PPE_KITS, BLANKETS, MASKS, SANITIZER)values(5, 'Ward-5', 'HSR', 500, 150, 200, 95, 60, 30, 100, 110, 90);") 

#Creating a table donaters and inserting values
mycur.execute("create table donaters(FNAME varchar(20), LNAME varchar(20), PHONE varchar(10), DONATED varchar(100));")

mycur.execute("insert into donaters(FNAME, LNAME, PHONE, DONATED)values('Chandak', 'Sanchal', '7223819302', '30 PPE Kits');")
mycur.execute("insert into donaters(FNAME, LNAME, PHONE, DONATED)values('Manshi', 'Rinta', '6482039182', '30 Masks');")
mycur.execute("insert into donaters(FNAME, LNAME, PHONE, DONATED)values('Ali', 'Mandani', '9273018293', '25 Sanitizers');")
mycur.execute("insert into donaters(FNAME, LNAME, PHONE, DONATED)values('Christine', 'Mandala', '8463729471', '10 Blankets');")
mycur.execute("insert into donaters(FNAME, LNAME, PHONE, DONATED)values('Joseph', 'Rosevelt', '8452637160', '50 Masks');")
mycur.execute("insert into donaters(FNAME, LNAME, PHONE, DONATED)values('Mohan', 'Sheriff', '7463829371', '30 PPE Kits');")

#Creating a table help needed and inserting values
mycur.execute("create table help_needed(FNAME varchar(20), LNAME varchar(20), PHONE varchar(10), NEEDED varchar(100));")

mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Anand', 'Pitchai', '3729950173', '25 Blankets');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Divvela', 'Puma', '8392048193', '50 PPE Kits');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Bargali', 'Cuttlerywalas', '9461033242', '25 Masks');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Krunal', 'Champan', '9916382004', '55 Sanitizers');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Mandeep', 'Saini', '7291028394', '5 PPE Kits');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Lokesh', 'Sundar', '0180182934', '15 Blankets');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Rahul', 'M', '8102839471', '35 Sanitizers');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Vihaan', 'Shroff', '8388251099', '25 Blankets');")
mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('Anil', 'Koti', '7182930183', '45 Masks');")


print("All tables created sucessfully!")
f.commit()