import urllib
import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

# END OF IMPORTS #

# START OF STALLHOLDER MODELLING #

class Stall(ndb.Model):
    name = ndb.StringProperty() ## For Stall1
    menu = ndb.TextProperty()
    time = ndb.StringProperty() ## prep time
    description = ndb.StringProperty() ## description of dish
    price = ndb.StringProperty() ## cost of dish
    item = {} ## dictionary to store time,description and price as 1
    waiting_time = ndb.IntegerProperty() ## total waiting time
    food_info = [] ## add different dishes into food_info
    item_add = [] ## list of food in the queue, description only
    
    name2 = ndb.StringProperty() ## For Stall2
    menu2 = ndb.TextProperty()
    time2 = ndb.StringProperty()
    description2 = ndb.StringProperty()
    price2 = ndb.StringProperty()
    item2 = {} 
    waiting_time2 = ndb.IntegerProperty() 
    food_info2 = []
    item_add2 = []
    
    name3 = ndb.StringProperty() ## For Stall3
    menu3 = ndb.TextProperty()
    time3 = ndb.StringProperty()
    description3 = ndb.StringProperty()
    price3 = ndb.StringProperty()
    item3 = {} 
    waiting_time3 = ndb.IntegerProperty() 
    food_info3 = []
    item_add3 = []


class MainPage(webapp2.RequestHandler): #Handler for the main page
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                'stall_name': person.name,
                'stall_name2': person.name2,
                'stall_name3': person.name3,
                }
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
#            curr = ndb.Key('Stall', 'khoongweihao')
            curr = ndb.Key('Stall', 'orbitalthedrunkards')
            person = curr.get()
            template_values = {'stall_name': person.name,
                               'stall_name2': person.name2,
                               'stall_name3': person.name3,
                               }
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
#            self.response.out.write(template.render())

class About(webapp2.RequestHandler): #Handler for the about page
    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())

class stall1(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall1.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name': person.name,
                    'stall_menu': person.menu,
                    'stall_time': person.time,
                    'food_description': person.description,
                    'food_price': person.price,
                    'food_info': person.food_info,
                    'item_add': person.item_add,
                    'waiting_time': person.waiting_time
                    }
                template = jinja_environment.get_template('stall1.html')
                self.response.out.write(template.render(template_values))
        else:
#            curr = ndb.Key('Stall', 'khoongweihao')
            curr = ndb.Key('Stall', 'orbitalthedrunkards')
            person = curr.get()
            template_values = {'stall_name': person.name,
                    'stall_menu': person.menu,
                    'stall_time': person.time,
                    'food_description': person.description,
                    'food_price': person.price,
                    'food_info': person.food_info,
                    'item_add': person.item_add,
                    'waiting_time': person.waiting_time}
            template = jinja_environment.get_template('stall1.html')
            self.response.out.write(template.render(template_values))

class stall1_page(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall1_page.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name': person.name,
                    'stall_menu': person.menu,
                    'stall_time': person.time,
                    'food_description': person.description,
                    'food_price': person.price,
                    'waiting_time': person.waiting_time,
                    'food_info': person.food_info,
                    'item_add': person.item_add
                    }
                template = jinja_environment.get_template('stall1_page.html')
                self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
            
    def post(self):
        curr = ndb.Key('Stall', users.get_current_user().nickname())
        person = curr.get()
        if person == None:
            person = Stall(id=users.get_current_user().nickname())
        stall_name = self.request.get('name')
        stall_menu = self.request.get('menu')
        prep_time = self.request.get('time')
        food_descript = self.request.get('description')
        food_price = self.request.get('price')
        menu_update = self.request.get('menu_update')
        menu_delete = self.request.get('menu_delete')
        item_add = self.request.get('item_add') ## NEW
        waiting_time = self.request.get('waiting_time') ## NEW
        queue_delete = self.request.get('queue_delete')
        items = self.request.get('items')
        item_in_queue = self.request.get('item_in_queue') ## name of field in .html

        if stall_name:
            person.name = stall_name
            person.put()
            
        elif menu_update: #if i click on the button add
            if food_descript not in person.item:
                person.item = dict(descript=food_descript, price=food_price, time=prep_time)
                person.food_info.append(person.item)
            person.put()

        elif item_add: ##
            if person.waiting_time == None:
                person.waiting_time = int(0)
            for item in person.food_info:
                if item_in_queue == item["descript"]: # if item added is in item dictionary
                    person.item_add.append(item_in_queue)
                    person.waiting_time += int(item["time"])
                person.put()
            else:
                person.waiting_time = person.waiting_time
            person.put()

        elif queue_delete:
            if person.item_add == []:
                person.waiting_time = 0
            else:
                person.item_add.remove(item_in_queue)
                for items in person.food_info:
                    if items["descript"] == item_in_queue:
                        person.waiting_time -= int(items["time"])
            person.put()
            
            
        elif menu_delete:
            for item in person.food_info:
                if items == item["descript"]:
                    person.food_info.remove(item)
            person.put()
            

        template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                'stall_menu': person.menu,
                'stall_name': person.name,
                'stall_time': person.time,
                'food_description': person.description,
                'food_price': person.price,
                'waiting_time': person.waiting_time,
                'food_info': person.food_info,
                'item_add': person.item_add
                }
        template = jinja_environment.get_template('stall1_page.html')
        self.response.out.write(template.render(template_values))
        
class stall2(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall2.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name2': person.name2,
                    'stall_menu2': person.menu2,
                    'stall_time2': person.time2,
                    'food_description2': person.description2,
                    'food_price2': person.price2,
                    'food_info2': person.food_info2,
                    'item_add2': person.item_add2,
                    'waiting_time2': person.waiting_time2
                    }
                template = jinja_environment.get_template('stall2.html')
                self.response.out.write(template.render(template_values))
        else:
#            curr = ndb.Key('Stall', 'khoongweihao')
            curr = ndb.Key('Stall', 'orbitalthedrunkards')
            person = curr.get()
            template_values = {'stall_name2': person.name2,
                    'stall_menu2': person.menu2,
                    'stall_time2': person.time2,
                    'food_description2': person.description2,
                    'food_price2': person.price2,
                    'food_info2': person.food_info2,
                    'item_add2': person.item_add2,
                    'waiting_time2': person.waiting_time2}
            template = jinja_environment.get_template('stall2.html')
            self.response.out.write(template.render(template_values))

class stall2_page(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall2_page.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name2': person.name2,
                    'stall_menu2': person.menu2,
                    'stall_time2': person.time2,
                    'food_description2': person.description2,
                    'food_price2': person.price2,
                    'waiting_time2': person.waiting_time2,
                    'food_info2': person.food_info2,
                    'item_add2': person.item_add2
                    }
                template = jinja_environment.get_template('stall2_page.html')
                self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
            
    def post(self):
        curr = ndb.Key('Stall', users.get_current_user().nickname())
        person = curr.get()
        if person == None:
            person = Stall(id=users.get_current_user().nickname())
        stall_name2 = self.request.get('name2')
        stall_menu2 = self.request.get('menu2')
        prep_time2 = self.request.get('time2')
        food_descript2 = self.request.get('description2')
        food_price2 = self.request.get('price2')
        menu_update2 = self.request.get('menu_update2')
        menu_delete2 = self.request.get('menu_delete2')
        item_add2 = self.request.get('item_add2') ## NEW
        waiting_time2 = self.request.get('waiting_time2') ## NEW
        queue_delete2 = self.request.get('queue_delete2')
        items2 = self.request.get('items2')

        if stall_name2:
            person.name2 = stall_name2
            person.put()
            
        elif menu_update2: #if i click on the button add
            if food_descript2 not in person.item2:
                person.item2 = dict(descript2=food_descript2, price2=food_price2, time2=prep_time2)
                person.food_info2.append(person.item2)
            person.put()

        elif item_add2: ##
            if person.waiting_time2 == None:
                person.waiting_time2 = int(0)
            for item2 in person.food_info2:
                if item_add2 == item2["descript2"]: # if item added is in item dictionary
                    person.item_add2.append(item_add2)
                    person.waiting_time2 += int(item2["time2"])
                person.put()
            else:
                person.waiting_time2 = person.waiting_time2
            person.put()

        elif queue_delete2:
            for i in range(len(person.item_add2)):
                person.item_add2.pop()
            person.waiting_time2 = 0
            person.put()
            
            
        elif menu_delete2:
            for item2 in person.food_info2:
                if items2 == item2["descript2"]:
                    person.food_info2.remove(item2)
            person.put()
            

        template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                'stall_menu2': person.menu2,
                'stall_name2': person.name2,
                'stall_time2': person.time2,
                'food_description2': person.description2,
                'food_price2': person.price2,
                'waiting_time2': person.waiting_time2,
                'food_info2': person.food_info2,
                'item_add2': person.item_add2
                }
        template = jinja_environment.get_template('stall2_page.html')
        self.response.out.write(template.render(template_values))

class stall3(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall3.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name3': person.name3,
                    'stall_menu3': person.menu3,
                    'stall_time3': person.time3,
                    'food_description3': person.description3,
                    'food_price3': person.price3,
                    'food_info3': person.food_info3,
                    'item_add3': person.item_add3,
                    'waiting_time3': person.waiting_time3
                    }
                template = jinja_environment.get_template('stall3.html')
                self.response.out.write(template.render(template_values))
        else:
#            curr = ndb.Key('Stall', 'khoongweihao')
            curr = ndb.Key('Stall', 'orbitalthedrunkards')
            person = curr.get()
            template_values = {'stall_name3': person.name3,
                    'stall_menu3': person.menu3,
                    'stall_time3': person.time3,
                    'food_description3': person.description3,
                    'food_price3': person.price3,
                    'food_info3': person.food_info3,
                    'item_add3': person.item_add3,
                    'waiting_time3': person.waiting_time3
                               }
            template = jinja_environment.get_template('stall3.html')
            self.response.out.write(template.render(template_values))

class stall3_page(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            curr = ndb.Key('Stall', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    }
                template = jinja_environment.get_template('stall3_page.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'stall_name3': person.name3,
                    'stall_menu3': person.menu3,
                    'stall_time3': person.time3,
                    'food_description3': person.description3,
                    'food_price3': person.price3,
                    'waiting_time3': person.waiting_time3,
                    'food_info3': person.food_info3,
                    'item_add3': person.item_add3
                    }
                template = jinja_environment.get_template('stall3_page.html')
                self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
            
    def post(self):
        curr = ndb.Key('Stall', users.get_current_user().nickname())
        person = curr.get()
        if person == None:
            person = Stall(id=users.get_current_user().nickname())
        stall_name3 = self.request.get('name3')
        stall_menu3 = self.request.get('menu3')
        prep_time3 = self.request.get('time3')
        food_descript3 = self.request.get('description3')
        food_price3 = self.request.get('price3')
        menu_update3 = self.request.get('menu_update3')
        menu_delete3 = self.request.get('menu_delete3')
        item_add3 = self.request.get('item_add3') ## NEW
        waiting_time3 = self.request.get('waiting_time3') ## NEW
        queue_delete3 = self.request.get('queue_delete3')
        items3 = self.request.get('items3')

        if stall_name3:
            person.name3 = stall_name3
            person.put()
            
        elif menu_update3: #if i click on the button add
            if food_descript3 not in person.item3:
                person.item3 = dict(descript3=food_descript3, price3=food_price3, time3=prep_time3)
                person.food_info3.append(person.item3)
            person.put()

        elif item_add3: ##
            if person.waiting_time3 == None:
                person.waiting_time3 = int(0)
            for item3 in person.food_info3:
                if item_add3 == item3["descript3"]: # if item added is in item dictionary
                    person.item_add3.append(item_add3)
                    person.waiting_time3 += int(item3["time3"])
                person.put()
            else:
                person.waiting_time3 = person.waiting_time3
            person.put()

        elif queue_delete3:
            for i in range(len(person.item_add3)):
                person.item_add3.pop()
            person.waiting_time3 = 0
            person.put()
            
            
        elif menu_delete3:
            for item3 in person.food_info3:
                if items3 == item3["descript3"]:
                    person.food_info3.remove(item3)
            person.put()
            

        template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                'stall_menu3': person.menu3,
                'stall_name3': person.name3,
                'stall_time3': person.time3,
                'food_description3': person.description3,
                'food_price3': person.price3,
                'waiting_time3': person.waiting_time3,
                'food_info3': person.food_info3,
                'item_add3': person.item_add3
                }
        template = jinja_environment.get_template('stall3_page.html')
        self.response.out.write(template.render(template_values))

#class stall2(webapp2.RequestHandler): #Handler for the stores
#    def get(self):
#        template = jinja_environment.get_template('stall2.html')
#        self.response.out.write(template.render())

#class stall2_page(webapp2.RequestHandler): #Handler for the stores
#
#    def get(self):
#        user = users.get_current_user()
#        if user:  # signed in already
#            template_values = {
#                'user_nickname': users.get_current_user().nickname(),
#                'logout': users.create_logout_url(self.request.host_url),
#                }
#            template = jinja_environment.get_template('stall2_page.html')
#            self.response.out.write(template.render(template_values))
#        else:
#            template = jinja_environment.get_template('stall2_page.html')
#            self.response.out.write(template.render())

#class stall3(webapp2.RequestHandler): #Handler for the stores
#    def get(self):
#        template = jinja_environment.get_template('stall3.html')
#        self.response.out.write(template.render())
#
#class stall3_page(webapp2.RequestHandler): #Handler for the stores
#
#    def get(self):
#        user = users.get_current_user()
#        if user:  # signed in already
#            template_values = {
#                'user_nickname': users.get_current_user().nickname(),
#                'logout': users.create_logout_url(self.request.host_url),
#                }
#            template = jinja_environment.get_template('stall3_page.html')
#            self.response.out.write(template.render(template_values))
#        else:
#            template = jinja_environment.get_template('stall3_page.html')
#            self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/thedrunkards', MainPage),
                               ('/about', About),
                               ('/stall1', stall1),
                               ('/stall1_page', stall1_page),
                               ('/stall2', stall2),
                               ('/stall2_page', stall2_page),
                               ('/stall3', stall3),
                               ('/stall3_page', stall3_page)],
                               debug=True)
