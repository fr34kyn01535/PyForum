# coding: utf-8
import cherrypy
from app import datenbank,templates,authentifizierung

class Request(object):
	exposed = True 
	
	def __init__(self):
		self.db = datenbank.Datenbank()

	def POST(self,action,thema, discussionname,text=None,newdiscussionname=None):
		authentifizierung.ValidateLoggedIn()
		if action == "create":
			self.db.createDiskussion(thema,discussionname, text)
			return self.GET(thema)
		else:
			authentifizierung.ValidateAdmin()
			if action == "edit":
				self.db.editDiskussion(thema,discussionname,newdiscussionname,text=None)
				return self.GET(thema)
			else:
				if action == "delete":
					self.db.deleteDiskussion(thema, discussionname)
					return self.GET(thema)
			
		
	def GET(self, thema):
		response = self.getDiskussionen(thema);
		if response == None:
			cherrypy.response.status = 500
		return response
      
	def default(self, *arguments, **kwargs):
		raise cherrypy.HTTPError(404, "Invalid request: " + str(arguments) + " " + str(kwargs)) 
		
	def getDiskussionen(self, thema):
		return templates.RenderTemplate("diskussionen.html",title="Diskussionen",diskussionen=self.db.getDiskussionen(thema), thema = thema);

	
# EOF