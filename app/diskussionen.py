# coding: utf-8
import cherrypy
import json
from app import datenbank,templates,authentifizierung

class Request(object):
	exposed = True 
	
	def __init__(self):
		self.db = datenbank.Datenbank()

	def dumper(obj):
		try:
			return obj.toJSON()
		except:
			return obj.__dict__
		
	def POST(self,action,thema,id=None, title=None,text=None,beitragID=None):
		authentifizierung.ValidateLoggedIn()
		if action == "create":
			self.db.createDiskussion(thema,title, text)
			
			#result = {};
			#result["diskussionen"] = self.db.getDiskussionen(thema)
			#result["thema"] = thema
			#cherrypy.response.headers['Content-Type']= 'text/plain'
			#return json.dumps(result)
			
			return templates.RenderTemplate("diskussionen-liste.html",diskussionen=self.db.getDiskussionen(thema), thema = thema)

		else:
			authentifizierung.ValidateLoggedIn()
			if action == "edit":
				self.db.edit(thema,id,title,text,beitragID)
				return self.GET(thema)
			else:
				authentifizierung.ValidateAdmin()
				if action == "delete":
					self.db.delete(thema, id,beitragID)
					return templates.RenderTemplate("diskussionen-liste.html",diskussionen=self.db.getDiskussionen(thema), thema = thema)

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