import threading 
import time
import random
import mysql.connector
from dbinfo import *

#Total ward count
TC=5

count = 0
thr = [0 for i in range(TC)]
db_data = [[] for i in range(TC+1)]

def simulation(): 
    global count
    global db_data
    
    count = count + 1
    mylocal = count  
    i = 0

    #Randimizing the addition and reduction of supplies 
    while True:
        i = i+1
        x = random.randint(1,350)

        if x == 1:
            db_data[mylocal][3] = db_data[mylocal][3] + 50
            st = "UPDATE ccinfo SET BEDS = {} where ID = {}".format(db_data[mylocal][3], mylocal)
        elif x == 2 and db_data[mylocal][3] > 50:
            db_data[mylocal][3] = db_data[mylocal][3] - 50
            st = "UPDATE ccinfo SET BEDS = {} where ID = {}".format(db_data[mylocal][3], mylocal)
        elif x == 3:
            db_data[mylocal][7] = db_data[mylocal][7] + 1
            st = "UPDATE ccinfo SET DOCTORS = {} where ID = {}".format(db_data[mylocal][7], mylocal)
        elif x == 4 and db_data[mylocal][7] > 7:
            db_data[mylocal][7] = db_data[mylocal][7] - 1
            st = "UPDATE ccinfo SET DOCTORS = {} where ID = {}".format(db_data[mylocal][7], mylocal)
        elif x > 4 and x < 101:
            db_data[mylocal][4] = db_data[mylocal][4] + 1
            st = "UPDATE ccinfo SET DISCHARGED = {} where ID = {}".format(db_data[mylocal][4], mylocal)
        elif x > 100 and x < 201:
            db_data[mylocal][5] = db_data[mylocal][5] + 1
            st = "UPDATE ccinfo SET ACTIVE = {} where ID = {}".format(db_data[mylocal][5], mylocal)
        elif x > 200 and x < 211:
            db_data[mylocal][6] = db_data[mylocal][6] + 1
            st = "UPDATE ccinfo SET DEAD = {} where ID = {}".format(db_data[mylocal][6], mylocal)            
        elif x > 230 and x < 241:
            db_data[mylocal][9] = db_data[mylocal][9] + 5
            st = "UPDATE ccinfo SET PPE_KITS = {} where ID = {}".format(db_data[mylocal][9], mylocal)
        elif x > 240 and x < 251 and db_data[mylocal][9] > 10:
            db_data[mylocal][9] = db_data[mylocal][9] - 5
            st = "UPDATE ccinfo SET PPE_KITS = {} where ID = {}".format(db_data[mylocal][9], mylocal)
        elif x > 250 and x < 261:
            db_data[mylocal][10] = db_data[mylocal][10] + 5
            st = "UPDATE ccinfo SET BLANKETS = {} where ID = {}".format(db_data[mylocal][10], mylocal)
        elif x > 260 and x < 271 and db_data[mylocal][10] > 10:
            db_data[mylocal][10] = db_data[mylocal][10] - 5
            st = "UPDATE ccinfo SET BLANKETS = {} where ID = {}".format(db_data[mylocal][10], mylocal)
        elif x > 270 and x < 281:
            db_data[mylocal][11] = db_data[mylocal][11] + 5
            st = "UPDATE ccinfo SET MASKS = {} where ID = {}".format(db_data[mylocal][11], mylocal)
        elif x > 280 and x < 291 and db_data[mylocal][11] > 10:
            db_data[mylocal][11] = db_data[mylocal][11] - 5
            st = "UPDATE ccinfo SET MASKS = {} where ID = {}".format(db_data[mylocal][11], mylocal)
        elif x > 290 and x < 301:
            db_data[mylocal][12] = db_data[mylocal][12] + 5
            st = "UPDATE ccinfo SET SANITIZER = {} where ID = {}".format(db_data[mylocal][12], mylocal)
        elif x > 300 and x < 311 and db_data[mylocal][12] > 10:
            db_data[mylocal][12] = db_data[mylocal][12] - 5
            st = "UPDATE ccinfo SET SANITIZER = {} where ID = {}".format(db_data[mylocal][12], mylocal)
        elif x >310:
            continue
        mycur.execute(st)
        f.commit()
        time.sleep(7)
        
        '''elif x > 210 and x < 221:
            db_data[mylocal][8] = db_data[mylocal][8] + 10000
            st = "UPDATE ccinfo SET MONEY = {} where ID = {}".format(db_data[mylocal][8], mylocal)
        elif x > 220 and x < 231 and db_data[mylocal][8] > 20000:
            db_data[mylocal][8] = db_data[mylocal][8] - 10000
            st = "UPDATE ccinfo SET MONEY = {} where ID = {}".format(db_data[mylocal][8], mylocal)'''
            

if __name__ == "__main__": 
    #Connecting to the database
    f = mysql.connector.connect(host = "localhost", user = db_username, passwd = db_password)
    mycur = f.cursor()
    mycur.execute("use one_stop_healthcare;")
    
    mycur.execute("select * from ccinfo;")
    dat = mycur.fetchall()
    
    #Handling the threads
    for val in dat:
        i = val[0]
        db_data[i] = list(val)  

    for i in range(TC):
        thr[i] = threading.Thread(target=simulation)
        thr[i].start()
        time.sleep(1)
        
    for i in range(TC):
        thr[i].join()
