# coding: utf-8
import cherrypy

def IsLoggedIn():
	cherrypy.session["Benutzername"] = "Test"
	cherrypy.session["Rolle"] = "Administrator"
	return True
	if 'Rolle' in cherrypy.session and cherrypy.session["Rolle"] is not "Jedermann":
		return True
	else:
		return False

def IsAdmin():
	if 'Rolle' in cherrypy.session and cherrypy.session["Rolle"] == "Administrator":
		return True
	else:
		return False
		
def ValidateAdmin():
	if not IsLoggedIn():
		raise cherrypy.HTTPError(401) 
	if not IsAdmin():
		raise cherrypy.HTTPError(403) 

def ValidateLoggedIn():
	if not IsLoggedIn():
		raise cherrypy.HTTPError(401) 