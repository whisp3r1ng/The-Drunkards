import urllib
import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/Templates"))

class MainPage(webapp2.RequestHandler): #Handler for the main page

    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

class MainPageUser(webapp2.RequestHandler): #Front page for those logged in

    def get(self):
        user = users.get_current_user()
        if user:
            template_values = {
                'user_nickname': users.get_current_user().nickname(),
                'logout': users.create_logout_url(self.request.host_url),
            }
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(template_values))
        else:
            self.redirect(self.request.host_url)
