Team Name: The Drunkards
Team Members: Khoong Wei Hao & Low Yee Seng
Targeted Level of Achievement: Gemini
Scope of the Project: To create a web application that monitors the present waiting time of a particular stall in a canteen, in particular those within NUS itself.
Target Audience: All students and staff
Overview of our Project: 
Our web application utilizes the Google App Engine based on the syntax of Python 2.7.11 and also html5. All stalls are able to create an account and will have to log in to access the more exclusive features of the web application, such as adding orders to the queue assigned to that particular stall. Also, anyone will be able to view the present waiting time of each stall registered with the web application, and through that decide which stall they should go to, to make their order. Each food or drink item will be assigned an estimated amount of time taken to be prepared in minutes. To store all these data in real time, each stall will have a terminal that inputs the order placed by the customer and edits the web application via Google App Engine in real-time. For example, we make use of Object Oriented Programming (OOP) where in this case, the stall has the food and drink items as its sub-classes. When an order is made under your name, it is appended/ added to the queue in the Stall class and also tagged with your name as stated in your account registered with the web application. Once the order has been prepared, it is removed from the order queue. The web application will also be capable in returning the location of your order in the queue.
Features: 
1.	Home Page (For the general public)
o	Key in Find the stall's name to view the current estimated waiting time before your order is reached, should you place an order
o	Key in your name/ queue number to view the state of your order (if any). For example, the location of your order in the queue and the estimated amount of time remaining till your order is ready.
o	Click on the stall's name to view the menu, current food items in queue, estimated waiting time should you place an order, and special offers by the stall if any (we can incorporate the stock availability of the item on the menu, depending on our project progress).
2.	Log in Page (For stalls only)
o	Once logged-in, the stall can add orders to the queue assigned to them and then update their stall page in the web application in real-time.
3.	About Page
4.	Stall's page which is accessible by the public (To view food queue in real time, estimated time left till your order is reached, special offers)
Problem(s): 
When we are working or studying at locations not in close proximity to the nearest canteen, we often find ourselves in long queues in the canteen after we make our way down for a meal. This results in time wasted and having our mood dampened when faced with such long waiting times due to the lack of proper planning. For students, especially when exams are drawing near, the need for proper time allocation into studies and breaks are of utmost importance. On the other hand, not all canteen stalls in NUS are equipped with equipments sophisicated enough to handle such web application in real time.
Proposed Solutions:
1.	Make the web application known to all students and staff via email, fliers, social media, news posts, etc.
2.	Students and staff can firstly access the webpage once their meal breaks start from all around NUS. 
3.	To improve the estimation of the waiting times, we can incorporate locations, such as the travelling time to the nearest or desired canteen (dependent on our project progress).
4.	By utilizing the Google App Engine, we make it hassle free for the vendors to use the web application - they do not need to know Python to append an order to the queue. They can simply add an order to the queue assigned to their stall after logging in with their stall's account.
Current Progress:
1.	Html for the Main, About, and Stalls (We chose 3 stalls as a sample) done. For this we modified Bootstrap’s Jumbotron, theme and stylesheets.
2.	Required CSS, .yaml and .py files have been set up.
3.	Web application tested and runs with Google App Engine.
4.	Figuring out how we can minimize hardcoding by allowing stallholders to create forms when updating the queues.
5.	Trying to incorporate means as to how we can store data with minimal hard coding involved (Similar to point 4, where stallholders will utilize forms instead).
# Sadly we over estimated our abilities and due to the lack of proper planning, we were not able to implement data storage and log in features by the end of milestone 2.
Aims:
In our next sprint, we aim to complete:
1.	Basic interface of the website Done
2.	Users login (For Stallholders only)
3.	Storing of accounts
4.	Storing of data
5.	Creating form submissions for the stallholders when they log in to update their stall data (To minimize hard coding)
6.	Users login
7.	Look at how we can work with vendors to get the information we need (Some sample data has been included)
In the 3rd sprint, we will attempt to make our website live. In the sense that we are able to input data/have options for stallholders to login and input orders, and for the website to be able to display the waiting time for each store.
S/N	Date	Description	Yee Seng	Wei Hao	Remarks:
1	09/05/16	Liftoff Day 1	7	0	 
2	10/05/16	Liftoff Day 2	3	9	 
3	24/05/16	Mission Control 2 (Game Dev)	3	5	 
4	24/05/16 (Online)	Project discussion	2	2	Workload distribution
5	31/05/16	Mission Control 3 (Offensive Web Security)	4	4	 
6	02/06/16 - 04/06/16	-	-	-	Yee Seng in SCAMP Prep camp
7	05/06/16	Project discussion	4	4	Familiarization with some basic aspects of html, i.e. templates, stylesheets.
8	06/06/16	Project discussion	8	8	Researched on html and created main page for web application with pictures and finetuned the relative positions of the images and icons. I.e. "main.html". 
9	09/06/16	Project discussion	3	3	Further discussion on how to breakdown the webapp for development
10	10/06/16 (Online)	Project discussion	3	3	Researching on datastore and how to incorporate it.
11	 13/06/16 - 17/06/16	-	-	-	Yee Seng in SCAMP
12	18/06/16 - 19/06/16	-	-	-	Wei Hao overseas
13	21/06/16	Project discussion	10	10	Created respective html pages for some sample stalls, about page, and linked them to one another and that of the home page. Attempted and successfully created python docs for home page and about page. (Edited .yaml and css files too)
14	23/06/16	Project discussion	8	8	Went on to create python docs for the other htmls such then when run on Google App Engine, the app is up and running and all htmls/ pages can be accessed from one another. (Editied .yaml and css files too)
15	26/06/16	Project discussion	5	5	Researched and discussed about data storage, and experimented with the tutorials provided by google. I.e. Guestbook.
16	27/06/16	Project discussion	10	10	Further research and discussion on data storage, and continued learning from the tutotrials provided by google. Started recording of video of our web app but we are not able to complete it on time (as of 2311 hrs).

Total Hours	70	71	 
While we have only completed 70/71 hours out of the required 130, we believe that before the 3rd milestone, we should be able to complete much of the required hours.
This is as both of us will have lesser commitments in the june/july period, as such we will have more time to focus on our project.
In addition, while we have the basic idea of what we want to accomplish, this is still in the ideation stage.
In our next sprint, we aim to complete (as stated in README above):
1.	Basic interface of the website
2.	Storing of accounts (Datastore)
3.	Users login
4.	Look at how we can work with vendors to get the information we need
We will finally incorporate the data input from stall vendors into our website by the 3rd sprint.
Video Link: https://youtu.be/7IlsQmB-BoU

# The-Drunkards
# Use the Jumbotron template
# important websites:
http://getbootstrap.com/
https://github.com/knmnyn/orbital16-bootstrap
https://www.youtube.com/watch?v=mosYVJdyVBo&list=PLllwxvcS7ca4ABnwy0MEFjH0wmQpXVM2S&index=9
http://getbootstrap.com/css/
