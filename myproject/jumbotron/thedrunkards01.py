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
    name = ndb.StringProperty()
    menu = ndb.TextProperty()
    time = ndb.StringProperty()##
    description = ndb.StringProperty()
    price = ndb.StringProperty()
    item = {} ##
    waiting_time = ndb.IntegerProperty() ##
    food_info = ndb.StringProperty()
    item_add = ndb.StringProperty()


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
                }
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
#            curr = ndb.Key('Stall', 'khoongweihao')
            curr = ndb.Key('Stall', 'test@example.com')
            person = curr.get()
            template_values = {'stall_name': person.name,}
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
            curr = ndb.Key('Stall', 'test@example.com')
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

        if stall_name:
            person.name = stall_name
            person.put()
            
        elif menu_update: #if i click on the button add
            if person.food_info == "" or person.food_info == None:
                if type(food_price) != str: ##
                    person.food_info = food_descript + ": " + str(food_price)
                    person.item[food_descript] = int(prep_time) ##
                else:
                    person.food_info = food_descript + ": " + food_price
                    person.item[food_descript] = int(prep_time) ##
            else:
                if type(food_price) != str: ##
                    person.food_info += ", " + food_descript + ": " + str(food_price) ##
                    person.item[food_descript] = int(prep_time) ##
                else:
                    person.food_info += ", " + food_descript + ": " + food_price ##
                    person.item[food_descript] = int(prep_time) ##
            person.put()

        elif item_add: ##
            if item_add in person.item: # if item added is in item dictionary
                if person.waiting_time == None or person.waiting_time == 0:
                    person.waiting_time = int(0)
                person.waiting_time += person.item[item_add] # add value of key to waiting time
                person.item_add += ", " + str(item_add)
                person.put()
            else:
                person.waiting_time = person.waiting_time
            person.put()

        elif queue_delete:
            person.item_add = ""
            person.waiting_time = 0
            person.put()
            
            
        elif menu_delete:
            person.food_info = ""
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
        template = jinja_environment.get_template('stall2.html')
        self.response.out.write(template.render())

class stall2_page(webapp2.RequestHandler): #Handler for the stores

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                }
            template = jinja_environment.get_template('stall2_page.html')
            self.response.out.write(template.render(template_values))
        else:
            template = jinja_environment.get_template('stall2_page.html')
            self.response.out.write(template.render())

class stall3(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        template = jinja_environment.get_template('stall3.html')
        self.response.out.write(template.render())

class stall3_page(webapp2.RequestHandler): #Handler for the stores

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                }
            template = jinja_environment.get_template('stall3_page.html')
            self.response.out.write(template.render(template_values))
        else:
            template = jinja_environment.get_template('stall3_page.html')
            self.response.out.write(template.render())

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
