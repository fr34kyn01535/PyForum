# coding: utf-8
import cherrypy

class Request(object):
	exposed = True 
	
	def __init__(self):
		pass
		
	def GET(self):
		cherrypy.session.clear()
		raise cherrypy.HTTPRedirect("/")
		
# EOF