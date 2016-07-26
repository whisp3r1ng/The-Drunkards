# The-Drunkards
#
For NUS Orbital 2016
#
Team Members: Khoong Wei Hao & Low Yee Seng
#
Targeted Level of Achievement: Gemini 
#
Scope of the Project: To create a web application that monitors the present queue and waiting time of a particular stall in a canteen, in particular those within NUS itself.
#
Target Audience: All students and staff
#
Overview of our Project: 
Our web application utilizes the Google App Engine based on the syntax of Python 2.7.11 and also html5. All stalls are able to create an account and will have to log in to access the more exclusive features of the web application, such as adding orders to the queue assigned to that particular stall. Currently, all stalls will be able to edit their menus and add/ delete items in their stall’s queue using a common account (Provided in the Project Log below for user testing). Also, anyone will be able to view the present waiting time of each stall registered with the web application, and through that decide which stall they should go to, to make their order in real-time. Each food or drink item will be assigned an estimated amount of time taken to be prepared in minutes. To store all these data in real time, each stall will have a terminal that inputs the order placed by the customer and edits the web application via Google App Engine in real-time. For example, we make use of Object Oriented Programming (OOP) such that every item in the stall’s menu will have a price tag as well as a preparation time tag. When an order is made, every food item in that order is appended to the stall’s queue and the total estimated waiting time (total time left to prepare all the food that is currently in queue) will be updated at the same time. Once the order has been prepared, it is removed from the order queue, and the remaining time left for the other orders will be updated as well.

Features: 
#
1.	Home Page (For the general public)

  o	Find the stall's name to view the current estimated waiting time left in preparing all the food that are currently in queue.

  o	Click on the stall's name to view the menu, current food items in queue, estimated waiting time, and special offers by the stall if any (we can incorporate the stock availability of the item on the menu, depending on our project progress).

2.	Log in Page (For stalls only)

  o	Once logged-in, the stall can add orders to the queue assigned to them and then update their stall page in the web application in real-time.

  o	Stallholders are also able to add and remove items in their menu, as well as include any special offers.

3.	About Page

4.	Stall's page which is accessible by the public (To view food queue in real time, estimated time left till your order is reached, special offers)

Problem(s): 

When we are working or studying at locations not in close proximity to the nearest canteen, we often find ourselves in long queues in the canteen after we make our way down for a meal. This results in time wasted and having our mood dampened when faced with such long waiting times due to the lack of proper planning. For students, especially when exams are drawing near, the need for proper time allocation into studies and breaks are of utmost importance. 

Proposed Solutions:

1.	Make the web application known to all students and staff via email, fliers, social media, news posts, etc.

2.	Students and staff can firstly access the webpage from their computers or mobile devices once their meal breaks start from all around NUS. 

3.	To improve the estimation of the waiting times, we can incorporate locations, such as the travelling time to the nearest or desired canteen (dependent on our project progress).

4.	By utilizing the Google App Engine, we make it hassle free for the vendors to use the web application - they do not need to know Python to append an order to the queue. They can simply add an order to the queue assigned to their stall after logging in with their stall's account via a terminal at their stall or simply their mobile phone.

Current build: https://thedrunkards01.appspot.com/

Note: 

Testing is currently available only for Orbital evaluators and supervising staff only.

Should testers encounter any problems while testing, such as being unable to log in to the testing account, please do let our team know asap via slack or through our adviser Chen Di.
