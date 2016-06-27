import urllib
import webapp2
import jinja2
import os

from google.appengine.api import users
from google.appengine.ext import ndb



jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'))

class MainPage(webapp2.RequestHandler): #Handler for the main page

    def get(self):
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render())

class About(webapp2.RequestHandler): #Handler for the about page

    def get(self):
        template = jinja_environment.get_template('about.html')
        self.response.out.write(template.render())

class stall1(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        template = jinja_environment.get_template('stall1.html')
        self.response.out.write(template.render())

class stall2(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        template = jinja_environment.get_template('stall2.html')
        self.response.out.write(template.render())

class stall3(webapp2.RequestHandler): #Handler for the stores
    def get(self):
        template = jinja_environment.get_template('stall3.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([('/', MainPage),
                               ('/about', About),
                               ('/stall1', stall1),
                               ('/stall2', stall2),
                               ('/stall3', stall3)],
                               debug=True)
