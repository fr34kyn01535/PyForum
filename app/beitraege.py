# coding: utf-8
import cherrypy
from app import datenbank,templates,authentifizierung

class Request(object):
	exposed = True 
	
	def __init__(self):
		self.db = datenbank.Datenbank()
	
	def POST(self,action,thema,id,title=None,text=None,beitragID=None):
		authentifizierung.ValidateLoggedIn()
		if action == "create":
			self.db.createBeitrag(thema,id,title,text)
			return self.GET(thema,id)
		else:
			authentifizierung.ValidateLoggedIn()
			if action == "edit":
				self.db.edit(thema,id,title,text,beitragID)
				return self.GET(thema,id)
			else:
				authentifizierung.ValidateAdmin()
				if action == "delete":
					self.db.delete(thema, id,beitragID)
					raise cherrypy.HTTPRedirect("/diskussionen?thema="+thema)
		
	def GET(self,thema,id):
		response = templates.RenderTemplate("beitraege.html",title="Beitraege",diskussion=self.db.getDiskussion(thema,id), thema = thema);
		if response == None:
			cherrypy.response.status = 500
		return response
      
	def default(self, *arguments, **kwargs):
		raise cherrypy.HTTPError(404, "Invalid request: " + str(arguments) + " " + str(kwargs)) 
		
# EOF