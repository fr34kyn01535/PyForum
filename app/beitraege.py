# coding: utf-8
import cherrypy
from app import datenbank,templates,authentifizierung

class Request(object):
	exposed = True 
	
	def __init__(self):
		self.db = datenbank.Datenbank()
	
	def POST(self,action,thema,discussionname,beitragID=None,title=None,newtitle=None,text=None,newtext=None):
		authentifizierung.ValidateLoggedIn()
		if action == "create":
			self.db.createBeitrag(thema,discussionname,title,text)
			return self.GET(thema,discussionname)
		else:
			authentifizierung.ValidateAdmin()
			if action == "edit":
				self.db.edit(thema,discussionname,beitragID,newtitle,newtext)
				discussionname = newtitle
				return self.GET(thema,discussionname)
			else:
				if action == "delete":
					self.db.deleteBeitrag(thema,discussionname,beitragID)
				return self.GET(thema,discussionname)
		#authentifizierung.ValidateAdmin()
		
	def GET(self,thema,discussionname):
		response = self.getBeitraege(thema,discussionname);
		if response == None:
			cherrypy.response.status = 500
		return response
      
	def default(self, *arguments, **kwargs):
		raise cherrypy.HTTPError(404, "Invalid request: " + str(arguments) + " " + str(kwargs)) 
		
	def getBeitraege(self,thema,discussionname):
		return templates.RenderTemplate("beitraege.html",title="Beitraege",beitraege=self.db.getBeitraege(thema,discussionname), thema = thema,discussionname = discussionname);

	
# EOF