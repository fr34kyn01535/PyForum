# coding: utf-8
import cherrypy
from app import datenbank,templates

class Request(object):
	exposed = True 
	
	def __init__(self):
		self.db = datenbank.Datenbank()
		
	def GET(self, id=None):
		response = templates.RenderTemplate("themen.html",title="Themen",themen=self.db.getThemen());
		if response == None:
			cherrypy.response.status = 500
		return response
      
	def default(self, *arguments, **kwargs):
		raise cherrypy.HTTPError(404, "Invalid request: " + str(arguments) + " " + str(kwargs)) 
		
# EOF 