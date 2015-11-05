# coding: utf-8
import cherrypy
from app import datenbank,templates

class Request(object):
	exposed = True 
	
	def __init__(self):
		self.db = datenbank.Datenbank()
		
	def GET(self):
		response = templates.RenderTemplate("login.html",title="Login");
		if response == None:
			cherrypy.response.status = 500
		return response
		
	def POST(self,username,password):
		if username is not None and password is not None:
			user = self.db.loginBenutzer(username,password)
			if user is not None and user["Passwort"] == password:
				cherrypy.session['Benutzername'] = username
				cherrypy.session['Rolle'] = user["Rolle"]
				raise cherrypy.HTTPRedirect("/")
		raise cherrypy.HTTPError(401) 
		
	def default(self, *arguments, **kwargs):
		raise cherrypy.HTTPError(404,  str(arguments) + " " + str(kwargs)) 
# EOF