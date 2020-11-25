# One-stop-Healthcare
This README file outlines the steps to install and configure the One-Stop Healthcare Solution for battle against COVID19 pandamic. These steps are for Windows machine, so please apply equivalent commands in case you are installing it on Mac or Linux machines.

- Install python 3
- Install MySQL from: https://www.sitepoint.com/how-to-install-mysql. Use the default configuration while setting up MySQL.
- Open a Windows command prompt (cmd) and go to Python "scripts" folder. This "scripts" folder is located in the directory where Python is installed. Run the following commands one at a time:
  - pip install mysql.connector-python
  - pip install chatterbot-python
  - pip install chatterbot.trainers-python
  - pip install flask-python
  - pip install threading-python
  You can copy/paste the above commands on the command prompt and press enter. This will install the necessary Python packages on your machine.

- Create a new directory (e.g. OSH) and copy all the project files in that folder.
- The default MySQL username is "root" and password is "". In case you have used a different username/password during MYSQL configuration, please open "dbinfo.py" file and set the appropriate values for these.
- Run "dbtest.py" using the command below:
  - python dbtest.py
  This will test if your database connectivity is working fine. If your database (MySQL) connection is working properly, it will show a success message. Otherwise, it will message that the connectivity is not fine. In the latter case, please ensure that your MYSQL setup is done correctly.
- Run "setup.py" using the command below:
  - python setup.py
  It will create a database and the required tables in that database. It will also insert some sample values for the table, so that we can run/demo our application.
- Run "thread.py" using the command below:
  - python thread.py
  This is a multithreaded python program that simulates the working of 5 covid care centers through launching 5 independed threads. Each thread wakes up on sleep timer and adjusts some parameters of the respective covid care center based on a random number. Each thread goes and updates the database table based on that, which gets picked up by the Flask application which displays the real-time data on the web browser.
  Do not close this window, or kill this application. This needs to keep running so that the database receives regular updates.
- Open a new command prompt and go to the directory where you have copied the project files.
- Run "main.py" using the command below:
  - pythin main.py
  This creates a flask application, which connects with the database, retrieves the data about the covid care centers and prepares a Javascripts/HTML/CSS page which will get displayed on the client side browser. This takes a minute or two to load.
- Once the flask application is running, launch a web browser and open the following link:
    http://127.0.0.1:5000/
  This will open the landing page of the OSH application. There are 5 pages on this application, and many of them have child pages. These pages cover details about:
  - Main application page
  - About us
  - Dashboard - this will open a real-time dashboard link which displays tables and charts on information about the 5 covid care centers.
  - Information - this has 2 child pages
    - FAQ: This has many frequently asked questions and answers about the COVID19 pandamic
    - Chatbot: This has an automated chatbot that answers several questions about the pandamic
  - Help - This has 2 child pages
    - Help needed: If someone needs help during the pandamic, they can register it here for someone to come forward to help them.
    - Donate: This page displays the needs of our 5 covid care centers and any individuals who have asked for help. Someone can go here to provide help to them.

- In order to stop the application:
  - Kill the "thread.py" program. This will stop the 5 threads, and also the database updates.
  - Kill the browser window.
  - Kill the main.py application. This will stop the Flask application.
- In order to clean the database and to remove all the OSH application entries, run the following command:
  - python dbdelete.py

