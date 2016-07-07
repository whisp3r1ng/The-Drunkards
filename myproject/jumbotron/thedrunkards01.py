import urllib
import webapp2
import jinja2
import os
import datetime ##NEW

from google.appengine.ext import ndb
from google.appengine.api import users


jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

### Some of these # indicates orginal code before experimenting!
# Globals
max_days = 30
psi_query = ndb.Query()

class Preference(ndb.Model):
    # Models a person's preference. Key is the nickname.
    email = ndb.StringProperty() # user email
    psi_limit = ndb.IntegerProperty()  # max acceptable PSI
    day_limit = ndb.IntegerProperty()  # max day above acceptable PSI before reminder
    last_reminder = ndb.DateProperty() # the last time reminder was sent

class MainPage(webapp2.RequestHandler): #Handler for the main page

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
                }
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render())

class About(webapp2.RequestHandler): #Handler for the about page

    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())

class stall1(webapp2.RequestHandler): #Handler for the stores

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already            # Retrieve person
            curr = ndb.Key('Preference', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'max_limit': max_days,
                    }
                template = jinja_environment.get_template('stall1.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'curr_psi_limit': person.psi_limit,
                    'curr_day_limit': person.day_limit,
                    'max_limit': max_days,
                    }

                template = jinja_environment.get_template('stall1.html')
                self.response.out.write(template.render(template_values))
        else:
            curr = ndb.Key('Preference', 'test@example.com')
            person = curr.get()
            template_values = {
                    'curr_psi_limit': person.psi_limit,
                    'curr_day_limit': person.day_limit,
                    'max_limit': max_days,
                    }
            template = jinja_environment.get_template('stall1.html')
            self.response.out.write(template.render(template_values))

#    def get(self):
#        template = jinja_environment.get_template('stall1.html')
#        self.response.out.write(template.render())

class stall1_page(webapp2.RequestHandler): #Handler for the stores

    def get(self):
        user = users.get_current_user()
        if user:  # signed in already            # Retrieve person
            curr = ndb.Key('Preference', users.get_current_user().nickname())
            person = curr.get()
            if person == None:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'max_limit': max_days,
                    }
                template = jinja_environment.get_template('stall1_page.html')
                self.response.out.write(template.render(template_values))
            else:
                template_values = {
                    'user_nickname': users.get_current_user().nickname(),
                    'logout': users.create_logout_url(self.request.host_url),
                    'curr_psi_limit': person.psi_limit,
                    'curr_day_limit': person.day_limit,
                    'max_limit': max_days,
                    }

                template = jinja_environment.get_template('stall1_page.html')
                self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)

#    def get(self):
#        user = users.get_current_user()
#        if user:  # signed in already
#            template_values = {
#                'user_nickname': users.get_current_user().nickname(),
#                'logout': users.create_logout_url(self.request.host_url),
#                }
#            template = jinja_environment.get_template('stall1_page.html')
#            self.response.out.write(template.render(template_values))
#        else:
#            template = jinja_environment.get_template('stall1_page.html')
#            self.response.out.write(template.render())

    def post(self):
        # Retrieve person
        curr = ndb.Key('Preference', users.get_current_user().nickname())
        person = curr.get()
        if person == None:
            person = Preference(id=users.get_current_user().nickname())
            person.email = users.get_current_user().email()
        psi_limit = self.request.get_range('psilimit')
        day_limit = self.request.get_range('daylimit')
        singapore_time = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
        person.last_reminder = singapore_time.date()
        if (psi_limit > 0) and (day_limit > 0) and (day_limit <= max_days):
            person.psi_limit = psi_limit
            person.day_limit = day_limit
            person.put()

        template_values = {
            'user_nickname': users.get_current_user().nickname(),
            'logout': users.create_logout_url(self.request.host_url),
            'curr_psi_limit': person.psi_limit,
            'curr_day_limit': person.day_limit,
            'max_limit': max_days,
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
