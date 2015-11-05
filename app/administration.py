# coding: utf-8
import cherrypy
from app import datenbank,templates,authentifizierung

class Request(object):
	exposed = True 
	
	def __init__(self):
		self.db = datenbank.Datenbank()
		
	def POST(self,originalusername,username,password,role):
		user = self.db.getBenutzer(originalusername)
		if password == "NO CHANGE":
			password = user["Passwort"]
		self.db.editBenutzer(originalusername,username,password,role)
		if originalusername == cherrypy.session["Benutzername"]:
			raise cherrypy.HTTPRedirect("/logout")
		return self.GET()
		
	def GET(self):
		authentifizierung.ValidateAdmin()
		
		response = templates.RenderTemplate("administration.html",title="Administration",benutzer=self.db.getAllBenutzer());
		
		if response == None:
			cherrypy.response.status = 500
			
		return response
      
	def default(self, *arguments, **kwargs):
		raise cherrypy.HTTPError(404, "Invalid request: " + str(arguments) + " " + str(kwargs)) 
		
# EOF