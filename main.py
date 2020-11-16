import flask
from flask import request
import time
import mysql.connector
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from dbinfo import *
import os

#Creating the chatbot instance
chatbot = ChatBot(
    'CoronaBot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ]
)
#Training the chatbot with our questions
trainer = ListTrainer(chatbot)
training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()
training_data = training_data_quesans + training_data_personal
trainer.train(training_data)

#Creating the application server
app = flask.Flask(__name__)

#Connecting the pictures folder to pass in the html file
PEOPLE_FOLDER = os.path.join('static', 'pictures')
PICTURES = os.path.join('static', 'pictures')
app.config['UPLOAD_FOLDER'] = PICTURES

#Connecting to the MySQL database 
f = mysql.connector.connect(host = "localhost", user = db_username, passwd = db_password)
mycur = f.cursor()
mycur.execute("use one_stop_healthcare;")

#Home page
@app.route("/")
def index():
    #Getting all the required pictures
    front = os.path.join(app.config['UPLOAD_FOLDER'], 'front.jpg') 
    prisha = os.path.join(app.config['UPLOAD_FOLDER'], 'prisha.jpg')
    pranshu = os.path.join(app.config['UPLOAD_FOLDER'], 'pranshu.jpg')    
    donate1 = os.path.join(app.config['UPLOAD_FOLDER'], 'donate.png')
    donate2 = os.path.join(app.config['UPLOAD_FOLDER'], 'donate2.png')
    donate3 = os.path.join(app.config['UPLOAD_FOLDER'], 'help.jpg')    
    question1 = os.path.join(app.config['UPLOAD_FOLDER'], 'question.png')
    question2 = os.path.join(app.config['UPLOAD_FOLDER'], 'question2.jpg')
    question3 = os.path.join(app.config['UPLOAD_FOLDER'], 'question3.png')    
    hospital1 = os.path.join(app.config['UPLOAD_FOLDER'], 'hospital.jpg')
    hospital2 = os.path.join(app.config['UPLOAD_FOLDER'], 'hospital2.jpg')
    hospital3 = os.path.join(app.config['UPLOAD_FOLDER'], 'hospital3.jpg')
    
    return flask.render_template("index.html", front=front, pranshu=pranshu, prisha=prisha, donate1=donate1, donate2=donate2, donate3=donate3, question1=question1, question2=question2, question3=question3, hospital1=hospital1,hospital2=hospital2,hospital3=hospital3)

#Chatbot pages
@app.route("/chatbot")
def home():
    return flask.render_template("chatbot.html")

@app.route("/get")
def get_bot_response():
    #Gets user question and returns appropiate answer
    userText = flask.request.args.get('msg')
    return str(chatbot.get_response(userText))

#FAQ page
@app.route("/faq")
def faq_page():
    return flask.render_template("faq.html")

#Covidcare centres
@app.route("/dashboard")
def charts():
    
    mycur.execute("select NAME, ACTIVE, DISCHARGED, DEAD, BEDS, DOCTORS from ccinfo;")
    dat = mycur.fetchall()

    active=[[]]
    for i in range(0,5,1):
        for j in range(0,6,1):
            active[i].append(dat[i][j])
        active.append([])
    del active[5]    
    active.insert(0, [' ', 'Active cases', 'Disharged', 'Dead', 'Beds', 'Doctors'])

    mycur.execute("select NAME, LOCATION, BEDS, DISCHARGED, ACTIVE, DEAD, DOCTORS from ccinfo;")
    lines = mycur.fetchall()
    return flask.render_template("dashboard.html", active=active, lines=lines)

#Donate page
@app.route("/donate")
def donation():
    mycur.execute("select NAME, PPE_KITS, BLANKETS, MASKS, SANITIZER from ccinfo;")
    dat = mycur.fetchall()
    info=[[]]
    
    for i in range(0,5,1):
        for j in range(0,5,1):
            info[i].append(dat[i][j])
        info.append([])
    del info[5]
    info.insert(0, ['Ward names', 'PPE Kits', 'Masks', 'Blankets', 'Sanitizers'])
    
    mycur.execute("select * from help_needed;")
    lines = mycur.fetchall()
    
    return flask.render_template("donation.html", info=info, lines=lines)
    
#Get the donaters information
@app.route("/donater_info")
def info():
    return flask.render_template("info.html")

#Get their response and store in database
@app.route("/thanks", methods=["POST"])
def thank():
    first_name = request.form.get("fname") 
    last_name = request.form.get("lname")  
    email = flask.request.form.get("ename")
    donated = flask.request.form.get("dname")
    
    mycur.execute("use one_stop_healthcare;")    
    mycur.execute("insert into donaters(FNAME, LNAME, PHONE, DONATED)values('{}','{}','{}','{}')".format(first_name, last_name, email, donated))
       
    return flask.render_template("thanks.html", message="{}, thank you for your generous contributions. Your details have been registered suceesfully and our representatives will get in touch with you shortly.".format(first_name + " " + last_name)) 

#Get the details of a person who wants help
@app.route("/help_needed")
def details():
    return flask.render_template("details.html")

#Store their details in database
@app.route("/stored", methods=["POST"])
def store():
    first_name = request.form.get("fname") 
    last_name = request.form.get("lname")  
    email = flask.request.form.get("ename")
    needed = flask.request.form.get("dname")

    mycur.execute("insert into help_needed(FNAME, LNAME, PHONE, NEEDED)values('{}','{}','{}','{}')".format(first_name, last_name, email, needed))
    
    return flask.render_template("thanks.html", message="{}, your request has been submitted suceesfully and the same will be displayed on our website. Our representatives will get in touch with you as in when we recieve any donations to help you.".format(first_name + " " + last_name)) 

#Running and executing the application
app.run()  