import mysql.connector

f = mysql.connector.connect(host = "localhost", user = "root", passwd = "")
mycur = f.cursor()
mycur.execute("create database One_Stop_Healthcare;")
f.commit()
mycur.execute("use One_Stop_Healthcare;")
print("database created")
#Donation field is yet to be added 
que = "create table ccinfo(ID INTEGER NOT NULL primary key, NAME varchar(20), LOCATION varchar(20), BEDS integer, DISCHARGED integer, ACTIVE integer, DEAD integer, DOCTORS integer, MONEY integer, PPE_KITS integer, BLANKETS integer, MASKS integer, SANITIZER integer);"
mycur.execute(que)
print("table created")

mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, MONEY , PPE_KITS, BLANKETS, MASKS, SANITIZER)values(1, 'Ward-1', 'KRM', 500, 100, 300, 50, 25, 100000, 20, 100, 100, 70);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, MONEY , PPE_KITS, BLANKETS, MASKS, SANITIZER)values(2, 'Ward-2', 'KRM', 1000, 290, 700, 150, 78, 250000, 40, 600, 300, 130);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, MONEY , PPE_KITS, BLANKETS, MASKS, SANITIZER)values(3, 'Ward-3', 'KRM', 50, 10, 30, 5, 5, 80000, 7, 50, 30, 40);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, MONEY , PPE_KITS, BLANKETS, MASKS, SANITIZER)values(4, 'Ward-4', 'HSR', 1500, 400, 1300, 250, 100, 400000, 70, 500, 300, 150);") 
mycur.execute("insert into ccinfo(ID, NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS, MONEY , PPE_KITS, BLANKETS, MASKS, SANITIZER)values(5, 'Ward-5', 'Bellandur', 500, 50, 100, 25, 40, 90000, 30, 100, 90, 90);") 

mycur.execute("create table donaters(FNAME varchar(20), LNAME varchar(20), EMAIL varchar(50), DONATED varchar(100));")
mycur.execute("create table help_needed(FNAME varchar(20), LNAME varchar(20), EMAIL varchar(50), NEEDED varchar(100));")

f.commit()
